# Real-Time Updates in System Design

## Mechanisms for Real-Time Communication

### 1. Long Polling
- **How It Works**:  
  Client sends a request → Server holds it open until data is available → Responds → Client repeats.
- **Use Cases**:  
  Simple notifications, legacy chat systems, order status updates.
- **Pros**:  
  - Reduces empty responses vs. regular polling.  
  - Works with basic HTTP infrastructure.  
- **Cons**:  
  - Higher latency (waits for server response before reconnecting).  
  - Scalability challenges (open connections consume server resources).  
- **Staff Engineer Considerations**:  
  - Timeout/retry strategies to avoid hung connections.  
  - Load balancers must handle long-lived requests.  

---

### 2. SSE (Server-Sent Events)
- **How It Works**:  
  Client opens a persistent HTTP connection → Server streams updates via `text/event-stream`.  
- **Use Cases**:  
  Live feeds (sports scores, news), dashboards, progress tracking.  
- **Pros**:  
  - Simple client implementation (browser-native `EventSource` API).  
  - Efficient for unidirectional server→client updates.  
- **Cons**:  
  - No bidirectional communication.  
  - Browser limits (e.g., ~6 concurrent SSE connections per origin).  
- **Staff Engineer Considerations**:  
  - Auto-reconnect with ==`last-event-id`== for resilience.  (client passes this)
  - Use compression (gzip) for high-frequency updates.  

---

### 3. WebSockets

[Check This](redis_pubsub_websockets_chat.md)
- **How It Works**:  
  Full-duplex communication over a single TCP connection (HTTP upgrade handshake → `ws://` or `wss://`).  
- **Use Cases**:  
  Chat apps, live collaboration (e.g., Google Docs), multiplayer gaming.  
- **Pros**:  
  - Low latency, bidirectional communication.  
  - Efficient for high-frequency messages (small overhead).  
- **Cons**:  
  - Stateful connections complicate horizontal scaling.  
  - Requires protocol-aware load balancers (e.g., HAProxy).  
- **Staff Engineer Considerations**:  
  - Securing with TLS (wss://) and rate limiting to prevent DDoS.  
  - Use Redis Pub/Sub or Kafka for broadcasting messages across instances.  

---

### 4. WebRTC
- **How It Works**:  
  Peer-to-peer (P2P) data/video streaming over UDP. Relies on:  
  - **STUN**: Discovers public IP/port for direct P2P connections.  
  - **TURN**: Relays traffic if direct P2P fails (e.g., behind strict NAT).  
- **Use Cases**:  
  Video conferencing (Zoom, Meet), live streaming, P2P file sharing.  
- **Pros**:  
  - Ultra-low latency (ideal for media).  
  - Reduces server costs with P2P.  
- **Cons**:  
  - Complexity (NAT traversal, ICE candidate negotiation).  
  - TURN servers introduce bandwidth costs.  
- **Staff Engineer Considerations**:  
  - Use encryption (SRTP for media, DTLS for data).  
  - Monitor TURN server costs and optimize fallback logic.  

---

## Key Considerations for Staff Engineers

### 1. Scalability
- **Connection Density**:  
  - SSE/WebSockets: Handle 10K+ connections per node (use async I/O like epoll).  
  - WebRTC: Offload P2P traffic to reduce server load.  
- **State Management**:  
  - Avoid sticky sessions with shared state (e.g., Redis for WebSocket session data).  

### 2. Protocol Selection
- **Bidirectional vs. Unidirectional**:  
  - WebSockets for chat (bidirectional).  
  - SSE for stock tickers (server→client only).  
- **Latency vs. Reliability**:  
  - WebRTC (UDP) for real-time voice/video.  
  - WebSockets (TCP) for guaranteed delivery (e.g., financial transactions).  


### 3. Fallback Strategies
- Graceful degradation:  
  - WebSockets → SSE → Long Polling.  
- Feature detection:  
  ```javascript
  if (window.WebSocket) { /* Use WebSockets */ }
  else if (window.EventSource) { /* Use SSE */ }
  ```

### 4. Security
- **Authentication**:  
  - Use tokens (JWT) over WebSocket handshakes.  
  - Validate CORS headers for SSE.  
- **Encryption**:  
  - Enforce TLS (wss://, HTTPS for SSE).  

### 5. Operational Challenges
- **Monitoring**:  
  - Track open connections, message rates, and error types (e.g., STUN failures).  
- **Cost Optimization**:  
  - Minimize TURN usage (prioritize P2P).  
  - Compress JSON payloads (e.g., Protocol Buffers).  

### 6. Edge Cases
- **Backpressure**:  
  - Throttle messages if the client can’t keep up (e.g., WebSocket buffer limits).  
- **Network Partitions**:  
  - Design idempotent APIs for retries.  

### 7. Emerging Trends
- **HTTP/2/3**:  
  - HTTP/2 Server Push (alternative to SSE).  
  - HTTP/3 (QUIC) for lower-latency connections.  
- **gRPC-Web**:  
  - Bidirectional streaming over HTTP/2.  

---

## Interview Discussion Points
- **Trade-offs**:  
  *"Why use WebSockets over SSE for a live trading app?"*  
  → Bidirectional needs (e.g., placing orders + receiving updates).  

- **Architecture**:  
  *"Design a global chat app with 1M concurrent users."*  
  → Regional WebSocket clusters, Redis Pub/Sub for cross-region sync.  

- **Troubleshooting**:  
  *"Users report lag in a video call. How to debug?"*  
  → Check TURN usage, STUN failures, network hops, and packet loss.  

- **Innovation**:  
  *"Could WebRTC replace WebSockets?"*  
  → Only for P2P use cases (e.g., file sharing), not client-server (e.g., chat).  

---

**Tips for Staff Engineers**:  
- Focus on **trade-offs** (e.g., "Why not use WebSockets everywhere?").  
- Highlight **operational experience** (e.g., scaling WebSockets in past roles).  
- Discuss **cost vs. latency** (e.g., TURN servers vs. P2P optimization).  
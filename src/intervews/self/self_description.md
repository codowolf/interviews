I'm going through interview process for Staff Software Engineer. Could you create a list of questions in a way that helps me talk deep about a project, and that also helps in preparing for behavioral questions for Staff Roles? Generate a bunch of questions so that I can fill it up and get it reviewed again.

---
## Project Details
***Role*** — Staff Engineer for Claims & Accidents
***Team*** — Claims & Accidents 
***Team Goal*** — Build and maintain a platform to intake accident reporting through multiple channels, and manage the life cycle of claims by partnering with 3rd Party Insurance Companies. Provide tools for the internal claims ops team to handle the claims, enabling them to have most efficient workflows
***Org*** — Insurance & Risk
***Org Goal*** — Make Rides as safe as possible. 
***Context*** — When a Lyft driver gets into an accident, depending on the situation, Lyft is responsible to provide insurance. `coverage — 1M$ for 3rd party damages, state minimum for 1st party coverage`. Driver's personal insurance doesn't cover the cost related to the damages because it's for commercial use. Previously, Lyft was covering the costs of damage, but since a few years Lyft has been integrating with Insurance companies and lets Insurance companies handle it for us. This means Lyft is connecting TPA (Third Party Adjusters) to the parties involved in the accident, while providing all the necessary data related to the accidents. 

**How it works?**
- Lyft pays a premium to the Insurance companies
- For an accident, Insurance companies evaluate and set the cost which Lyft will further evaluate and finalize settlement
- If a lawsuit is filed, Legal team is involved ***only if*** Lyft is named. This is when high costs are incurred
- A large loss claim is given special attention
- Lyft pays x% of the cost and the rest is covered by Insurance Companies

**Premium Negotiations**
- Several factors influence premium cost calculations — ride volume forecast, loss history, environmental factors and so on.
- One of them is mileage reporting
	- P1 (online)
	- P2 (ride accept state)
	- P3 (rider on ride)
	- `Insurance cost = p1_miles * p1_pricing + p2_miles * p2_pricing + p3_miles * p3_pricing`

**How team goal is achieved?**
- Provide tool called RMIS (Risk Management Information System)
- Intake accident information through web and mobile by riders, drivers and 3rd party
- Allow advocates to manage claims life cycle — add tasks, notes, attachments, visualize accident telematics data, search claims data
- Integrate with Insurance companies for two way data exchange
- Tech stack — python flask services, K8s, Dynamodb, Elasticsearch, SQS, Hive, Kafka

**What are advocates doing?**
- FNOL ops — after an accident is reported through forms, act quickly to verify all the information necessary to mark it ready to send to TPA. This could also involve phone calls with involved parties
- Claims ops — work with adjusters to guide them on the best strategy, evaluate final settlements, provide feedback, review workflows, work with legal to handle lawsuits, strategize to improve at every opportunity to reduce the insurance cost

**Pain Points**
- Lot of workflows are heavily manual, leading to high AHT (average handle time of claim), leading to missing SLA of claims submissions
- Many workflows require reading through long documents like Injury reports, Medical reports, Police reports, Lawsuits that can be time consuming 
- Lack of visibility into severity of the accident as the claim progresses 

**what we have built so far?**
- backend platform for conversational AI
	- use stateless API provided by openai and claude
	- persist conversation history to create AI chatbot experience 
- UI for showing claims summaries including severity, legal severity, timelines, note summaries
- Provides a chatbot interface to Q&A about claims
- damage estimator
	- uses accident photos to analyze damage severity through multi-modal LLM
	- uses accident photos and metadata to estimate damage repair cost ultimately helping with reserve estimation and severity
- document intelligence pipeline
	- a scalable document extraction framework to extract texts from scanned pdfs
	- handles large documents with complex layouts and extracts content using LLM multi-modal
	- summarizes document for advocates to quickly get all information
	- support chat with file
	- on track to build RAG pipeline for document Q&A

**Team**
- Eng — Staff Eng (lead, me), 2 frontend engineers, 2 backend engineers (rotating as needed)
- Product — 1 product manager (from mid stage of project), 1 staff prod manager for any strategic discussions
- Ops — end users (claims ops, fnol ops, legal ops, legal team) about 250-300
- Infra — ML platform, Infra (not much help from them other than libraries to talk to openai and aws)
- Design — design best UX, provided a lot of feedback here



**Timeline of project**
- I was tasked with a green field mandate of leading GenAI roadmap
	- Why? — because i was proactively learning AI's capabilities as LLM's were being realized. I thought of several use cases that could potentially reduce some of the manual workflows we had and constantly implemented proof of concept for small features. Looking at my interest, and the industry evolution around AI, they tasked me to lead it.  
- I was given reponsibility to lead the genai initiative. It was greenfield and no clear path goals defined, so I had to come up with any ideas possible and work with leadership. No resource allocation at the beginning of the project. It started off with just me ideating and working on setting up a vision. Implmenting PoC for small features were good, but I had to come up with a vision and strategy to have a clear road map defined, and how it would align with our mission to reduce claims handling time and improve workflow efficiency of our Ops team. The architecture should be something scalable beyond basic functionality and should fit the long term narrative of automating multiple workflows using LLMs. After several surveys and shadow sessions with our Ops, it was clear that one of the biggest pain points that could potentially be solved was around handling large documents. But I thought, to get there, we can't just build adhoc solutions, it should fit into existing platform of claims manaagement and also built around foundational capabilites of conversational experience. One of the challenging aspect of integrating was that I couldn't use stateful APIs the AI vendors provided, due to data privacy concerns. And using stateless API means I should have state machine for conversation history. Hence, I decided that in order to have a foundation, we need to build a chat framework with chatbot as a UX for our ops to get themselves familiar with AI interactions. With that in mind, the first product would be ChatBot, and then Document Intelligence built on top of it.
- ChatBot
	- Infra — python service, dynamodb, openai stateless API, conversation branching, dynamically select any GPT model for each request. 
	- Functionality — Add data objects as resources, and create and execute a prompt against the resources. 
	- Prompt Engineering — Several iterations of prompt were tested against different scenarios and prompts were improved accordingly. THere's also a feedback loop that allowed prompt optimizations even further
	- Result — Ops were able to get key insights about the claim to get them upto speed, by giving them clearly defined summary of the claim, it's current state, the timeline and summary of the notes. This was loved by our ops team and set as an example for other teams at Lyft. The ops were able to get the hang of using AI in their day to day workflows, leading to significant time savings. 
- Second milestone of document intelligence pipeline — challenge was large files, scanned docs, complex layouts. Vendor API's didn't support stateless API for this use case, so we had to build our own. Choice between AWS Textract and LLM took quite a bit of investigation. Run through 100s of different documents of different complexities. Couple of factors that allowed us to choose hybrid approach was that LLM's good with bad orientation, multi lingual, multi column docs and textract was good with complex layouts with forms, however both had inaccuracies in extreme complex cases. Further challenges included that large pdfs broken down to chunks, CPU bound image pre-processing, parallel extraction and retry mechnism for failures and finally aggregating extracted chunks into a single document within a given SLA (bound by LLM call)
	- Extracted texts are further summarized and displayed to the users
	- For large text files, implementing RAG pipeline. Challenges include chunking strategies as document has multiple formats. Created a poc with embeddings stored in elasticsearch, perform k-NN to load the chunks based on query and pass it with the query to LLM. Use tool calling to have LLM ask for chunks based on query — agentic RAG.





## Who am I and What I do?
 - I work for Insurance & Risk org — has 4 tech teams
	 - Pre-Accidents — road safety & telematics
	 - Post-Accidents — accidents & claims
- I am a Staff Engineer for the Claims & Accidents team. Our team's core mission is to build and maintain a platform for reporting accidents, managing the lifecycle of claims in partnership with third-party insurance companies, and providing tools to our internal claims operations team for maximum efficiency.
	- Life cycle involves making strategic decisions that impacts final settlement amount for a claim, as we receive more and more information through various channels
	- Our claims ops make this happen with years of expertise and in collaboration with our insurance partners. 


**The main problem we are solving is the heavily manual nature of claims processing.** Many workflows involves reading through extensive documents like police reports, medical reports, lawsuits that leads to very high Average Handle Times (AHT) and frequently missing critical SLAs at different stages. This directly impacts our operational efficiency and, ultimately, Lyft's insurance premium costs.

**AI Initiative** — I was given a greenfield mandate to identify and lead our GenAI strategy There was no clear path or resources initially, so I was responsible for ideating, defining the vision, and setting the technical architecture for a scalable solutions that could enhance multiple complex workflows.

My work focused on three key areas:

1. **AI Chatbot Platform:** I spearheaded the development of a backend platform for conversational AI. Given data privacy, we used stateless APIs, so I designed the system to persist conversation history for a true chatbot experience. This allowed claims ops to quickly get key insights and summaries about any claim, especially useful for long-running cases, significantly reducing the time spent getting up to speed.
    
2. **Document Intelligence Pipeline:** This was a major initiative. Our challenge was extracting and summarizing information from large, complex, and often scanned PDF documents, which vendor APIs couldn't handle reliably in a stateless way. I led the development of our own scalable document extraction framework using a hybrid LLM and AWS Textract approach. This system processes hundreds of documents, handles issues like bad orientation and complex layouts, and then summarizes the content for advocates. We were also on track to build a RAG pipeline for advanced document Q&A, tackling complex chunking strategies and integrating with Elasticsearch. This directly tackled the pain point of time-consuming document review.
    
3. **Damage Estimator:** We also developed a damage estimator that leverages multi-modal LLMs to analyze accident photos and metadata to assess damage severity and estimate repair costs, which helps with reserve estimation and overall claim severity assessment.
    

**The impact of these initiatives was significant.** We directly addressed the high AHT and manual workflows, enabling our claims ops team to become much more efficient. By providing quick access to critical information and automating document processing, we reduced the time spent on each claim, improved SLA adherence, and ultimately contributed to better control over our insurance costs.
## Conflicts
### Conflict 1: The Architectural Dilemma: Stateful Convenience vs. Stateless Compliance

**Situation:**  
When starting the greenfield GenAI initiative, the quickest path to a demonstrable AI Chatbot POC would have been to use a stateful API from OpenAI/Claude, where the model itself maintains conversation history. However, due to Lyft's strict data privacy requirements (especially concerning sensitive claims data), it was clear that using a stateless API was a non-negotiable. This meant we, as a team, would have to persist and manage the entire conversation history on our end for every LLM call, which added significant architectural complexity and development effort for the initial chatbot. The product manager and some junior engineers initially pushed for the simpler, quicker stateful approach, not fully grasping the data privacy implications or the long-term benefits of a stateless architecture.

**Your Role (Staff Engineer):** As the lead for the GenAI initiative, I was responsible for setting the long-term architectural vision and ensuring compliance while still delivering value.

**Conflict:** There was tension between the desire for a fast, "good enough" POC using an easier, stateful vendor API, and the need to build a robust, scalable, and privacy-compliant foundation using stateless APIs. This was a direct trade-off between speed-to-market for a basic feature and long-term architectural soundness and compliance.

**Resolution (Staff Level):**

1. **Educate & Explain:** I took the lead in educating the product manager and the team on the critical data privacy implications of using stateful vs. stateless LLM APIs. I explained that while a stateful API was simpler initially, it would compromise Lyft's data security posture and potentially lead to legal and compliance issues down the line. I specifically highlighted that claims data is extremely sensitive (PII, PHI) and cannot leave our direct control without strict anonymization or stateless processing.
    
2. **Architectural Vision & Phasing:** Instead of just saying "no," I presented a detailed architectural vision for how a stateless LLM service could be built. I proposed a dedicated, lightweight internal service responsible for persisting conversation history within Lyft's secure infrastructure (DynamoDB). I showed how this seemingly complex initial step would not only enable the chatbot but also become the foundational building block for future, more complex features like the Document Intelligence RAG pipeline, which also relies on managing context locally.
    
3. **Demonstrate Value & Risk:** I created a mini-POC of the user experience with the stateless approach to show that it wouldn't compromise the chatbot's perceived fluency or usability. I also quantified the engineering effort, acknowledging it was higher upfront, but framed it as a necessary investment to unlock a much larger set of capabilities securely. I emphasized that failing to comply could lead to severe penalties and reputational damage far outweighing any short-term gains.
    
4. **Secure Buy-in:** By framing the decision around long-term strategic advantage, compliance, and future-proofing rather than just "technical purity," I successfully secured buy-in from the product manager and leadership.
    

**Outcome:** We built the stateless LLM interaction service as the first milestone. This foundational architecture not only ensured compliance but also proved highly flexible and scalable, directly enabling the subsequent Document Intelligence pipeline and setting the stage for future GenAI applications without further major architectural overhauls related to data privacy.

### Conflict 2: Technical Constraints vs. Operational Urgency: The Document Intelligence Challenge

**Situation:**  
During the development of the Document Intelligence Pipeline (Milestone 2), we encountered significant technical hurdles. We needed to extract text from hundreds of types of documents – many were scanned PDFs, varied wildly in layout (multi-column, tables, forms), orientation, and quality (poor scans, handwriting). Neither AWS Textract nor general LLMs were perfectly accurate for all these "extreme complex cases" when used in isolation. The product and ops teams had high expectations for near-perfect extraction and summarization, as the primary goal was to drastically reduce manual review time. They wanted a solution "yesterday" to meet urgent SLA targets for claims submissions.

**Your Role (Staff Engineer):** As the lead, I was responsible for designing a scalable and robust solution that delivered high value, while also managing expectations around technical feasibility and delivery timelines.

**Conflict:** We had to balance the operational urgency for a rapid deployment with the technical reality of achieving high accuracy and robustness across a highly diverse and challenging document corpus. Pushing for perfect accuracy on all edge cases would significantly delay the launch, while launching with too many inaccuracies would erode user trust and not deliver the desired AHT reduction.

**Resolution (Staff Level):**

1. **Hybrid & Iterative Approach:** I proposed and designed a hybrid approach, leveraging the strengths of both AWS Textract (good for forms, structured data) and multi-modal LLMs (good for unstructured text, complex layouts, OCR on poor quality scans). This involved a sophisticated routing mechanism to apply the best tool for each document type, or even different parts of a document.
    
2. **Define MVP & Communicate Limitations:** I worked with the PM and ops leads to define an MVP (Minimum Viable Product) for document intelligence. This meant clearly identifying the top 80% of document types by volume where high accuracy was achievable. For the remaining 20% (the "extreme complex cases"), I clearly communicated that the system would provide its "best effort" but might still require manual review. This set realistic expectations and allowed us to launch faster.
    
3. **Build Robustness & Feedback Loops:** To address the remaining inaccuracies and enable continuous improvement, I championed building robust error handling, retry mechanisms, and a feedback loop directly into the RMIS tool. Advocates could easily flag incorrect extractions or summaries, providing critical data for model retraining and rule refinement. This empowered users and gave us actionable data for improvement.
    
4. **Performance Optimization:** For the CPU-bound image pre-processing and parallel extraction, instead of waiting for dedicated GPU infra (which was a dependency outside our control), I led the team in optimizing the Python services for maximum parallelism and efficiency on existing K8s/CPU resources. This allowed us to meet our processing SLAs without incurring external dependencies or major delays.
    

**Outcome:** We successfully launched the Document Intelligence Pipeline. While it wasn't 100% perfect on day one for every obscure document, it significantly reduced AHT for the most common and impactful claim types. The built-in feedback loop fostered a culture of continuous improvement, and the phased approach maintained user trust by setting realistic expectations. This allowed us to hit our core metrics for AHT reduction and improved operational efficiency.



---

### **Part 1: Project Deep Dive (Technical & Impact)**

**1. Project Overview & Business Context:**
*   **What was the primary goal or problem your project aimed to solve?**
    The primary goal of this project was to leverage Generative AI (GenAI) to significantly improve the efficiency and accuracy of Lyft's accident claims management process. Specifically, it aimed to solve critical pain points:
    1.  **High Average Handle Time (AHT) and missed SLAs:** Manual workflows for claims processing were time-consuming, leading to delays.
    2.  **Time-consuming document review:** Advocates spent excessive time manually reading and extracting information from lengthy and complex documents (injury reports, medical reports, police reports, lawsuits).
    3.  **Lack of real-time visibility into claim severity:** It was difficult to quickly assess the evolving severity of an accident claim as it progressed.
*   **What was the business context or strategic importance of this project to the company or its users?**
    The project held significant strategic importance to Lyft's Insurance & Risk organization. Lyft is responsible for insuring drivers during commercial use, and any associated costs (damages, lawsuits) directly impact the company's financial health.
    1.  **Cost Reduction:** Efficient claims handling, faster resolution, and accurate severity assessment directly contribute to lower insurance premiums negotiated with third-party insurance companies. The premium calculation is heavily influenced by loss history and efficient claim processing. Reducing AHT and improving data quality helps manage costs.
    2.  **Operational Efficiency:** Empowering the 250-300 internal claims and FNOL (First Notice of Loss) operations team with advanced tools (AI Chatbot, Document Intelligence, Damage Estimator) to reduce manual work and accelerate workflows, enabling them to focus on high-value tasks.
    3.  **Compliance & Risk Mitigation:** Missing SLAs can lead to higher costs and potential regulatory issues. Faster, more accurate processing mitigates these risks.
    4.  **Enhanced Safety Posture:** While indirect, efficient accident response and claims management contribute to a safer ecosystem by ensuring proper resolution and data collection.
*   **How did this project align with broader organizational objectives?**
    This project directly aligned with the broader organizational objective of "Making Rides as safe as possible" (Org Goal) by ensuring a robust and efficient post-accident claims process. It also aligned with financial objectives by **directly impacting premium negotiations and overall insurance costs**. Furthermore, it demonstrated Lyft's commitment to leveraging cutting-edge technology (GenAI) to enhance operational excellence and efficiency across the enterprise.
*   **Who were the key stakeholders (users, other teams, leadership)?**
    *   **Users:** Claims Operations (Claims Ops), First Notice of Loss Operations (FNOL Ops), Legal Operations (Legal Ops), and the Legal team (approximately 250-300 advocates).
    *   **Internal Teams:** Product Management (PM & Staff PM), Design, ML Platform Infrastructure, Core Infrastructure.
    *   **Leadership:** Insurance & Risk organization leadership, Engineering leadership, Finance (due to cost implications).
    *   **External Partners:** Third-Party Insurance Companies (indirectly, as our improved efficiency and data exchange impacts their processes).

**2. Your Role & Contributions:**
*   **What was your specific role and key responsibilities on this project?**
    As a Staff Engineer, I was the technical lead for the entire GenAI initiative within the Claims & Accidents team. My key responsibilities included:
    *   **Vision & Strategy:** Defining the technical vision and long-term roadmap for GenAI integration, especially in a greenfield environment with no clear initial path.
    *   **Architecture & Design:** Leading the end-to-end architectural design for the GenAI platform, ensuring scalability, reliability, and security.
    *   **Technical Leadership:** Providing technical guidance, mentorship, and code quality oversight for the 2 backend and 2 frontend engineers.
    *   **Hands-on Development:** Prototyping, implementing core services, and solving complex technical challenges.
    *   **Stakeholder Management:** Collaborating closely with Product, Design, Ops, and Legal teams to define requirements, gather feedback, and manage expectations.
    *   **Problem Solving:** Tackling ambiguous and complex technical challenges, particularly around LLM integration, data privacy, and large document processing.
*   **What were your direct, individual contributions? (Be specific: "I designed X," "I implemented Y," "I optimized Z").**
    *   **Vision & Strategy:** I ideated and defined the initial technical vision for the GenAI initiative, translating abstract problem statements into concrete, actionable engineering milestones.
    *   **AI ChatBot Service:** I designed and primarily implemented the core backend service for the conversational AI chatbot, including the stateless API integration with OpenAI/Claude and the resilient persistence mechanism for conversation history (as a conversation tree in DynamoDB).
    *   **Document Intelligence Architecture:** I designed the scalable architecture for the document intelligence pipeline, including the hybrid approach for text extraction (leveraging both AWS Textract and multi-modal LLMs), the chunking strategies for large PDFs, the parallel processing framework for image pre-processing and extraction, and the retry mechanisms.
    *   **RAG Pipeline POC:** I designed and built the initial Proof-of-Concept for the RAG (Retrieval Augmented Generation) pipeline, including the embedding storage in Elasticsearch, k-NN retrieval, and the "agentic RAG" approach using tool calling for LLMs.
    *   **Damage Estimator Foundations:** I contributed to the early design and prototyping efforts for the damage estimator, focusing on how multi-modal LLMs could analyze accident photos for severity and repair cost estimation.
    *   **Security & Privacy Compliance:** I designed and implemented the approach to ensure strict data privacy (e.g., using stateless LLM APIs and managing conversation history internally) to meet Lyft's rigorous privacy standards.
*   **What aspects of the project were you primarily accountable for?**
    I was primarily accountable for the overall technical success, architectural integrity, performance, and maintainability of the entire GenAI platform within the Claims & Accidents domain. This included ensuring that the solutions met the defined performance, scalability, and security requirements, and that they directly addressed the core pain points of the claims operations team. I was also accountable for guiding the team towards achieving the initial milestones.
*   **How did your contributions directly enable the success of the project?**
    My contributions directly enabled the project's success by:
    *   **Laying the Technical Foundation:** By designing and implementing the core LLM service and document intelligence pipeline, I provided the essential technical infrastructure that all subsequent GenAI features (chatbot, document summarization, RAG) were built upon.
    *   **Unlocking Value:** The AI ChatBot, an early deliverable I led, immediately provided value to advocates by speeding up claim comprehension, demonstrating the tangible benefits of GenAI and securing further buy-in and resources.
    *   **Addressing Core Challenges:** My work on handling stateless APIs for privacy, and processing complex large documents, directly addressed two of the most significant technical hurdles, unblocking the wider adoption of LLMs in our domain.
    *   **Ensuring Scalability & Reliability:** The architectural decisions I championed ensured the platform could handle increasing data volumes and user load reliably, which was critical for a core operational system.

**3. Technical Design & Architecture:**
*   **Describe the overall architecture of the system or component you worked on.**
    The core of the GenAI system was built around a **lightweight, dedicated Python Flask microservice** for LLM interactions, deployed on Kubernetes (K8s). This service acted as an intelligent orchestrator and abstraction layer for various LLM models (OpenAI, Claude).
    *   **Data Flow for Chatbot:** User queries from the RMIS UI hit the Flask service. The service retrieves the conversation history (stored as a conversation tree) from **DynamoDB**. It then constructs a complete prompt with the new query and history, sends it to the chosen LLM via its stateless API, receives the response, and persists the updated conversation tree back to DynamoDB.
    *   **Data Flow for Document Intelligence:** Documents are ingested via SQS/Kafka (e.g., when uploaded to RMIS). A separate processing worker (also a Flask service or part of the main one) picks up these messages.
        *   For PDF processing, a **hybrid approach** was used:
            *   **Image pre-processing:** CPU-bound tasks for optimizing scanned images for OCR.
            *   **Text Extraction:** For complex layouts/forms, AWS Textract was used. For multi-lingual, bad orientation, or multi-column, multi-modal LLMs (via our LLM service) were leveraged. This was often parallelized for large documents.
            *   **Aggregation:** Extracted chunks from different sources were aggregated into a single logical document.
            *   **Summarization/Q&A:** The extracted text was then summarized by LLMs and stored, or used in a RAG pipeline where embeddings were stored in **Elasticsearch** for semantic search (k-NN).
    *   **Data Storage:** **DynamoDB** for chat history (conversation tree), **Elasticsearch** for vector embeddings for RAG, **Hive** for analytical data and batch processing.
    *   **Messaging:** **SQS** for asynchronous task queues (e.g., document processing, retries), **Kafka** for broader data ingress/egress.
    *   **Existing Platform Integration:** The new GenAI services integrated with the existing RMIS platform via REST APIs for UI interaction and data exchange, and leveraged existing data pipelines (Kafka, Hive) for input and output.
*   **What were the key design choices you made or influenced? (e.g., choice of technologies, data stores, communication protocols, design patterns).**
    1.  **Dedicated LLM Microservice:** Rather than embedding LLM calls directly into existing services, we created a new, lightweight Python Flask service.
    2.  **Stateless LLM API Integration:** Exclusively used stateless APIs for OpenAI/Claude.
    3.  **Internal Conversation History Management:** Persisted chat history (conversation tree) in DynamoDB.
    4.  **Hybrid Document Extraction:** Chose a combination of AWS Textract and multi-modal LLMs for document processing.
    5.  **RAG with Elasticsearch and K-NN:** Utilized Elasticsearch for storing vector embeddings and its k-NN capabilities for retrieval.
    6.  **Asynchronous Processing:** Employed SQS for queuing document processing tasks.
*   **Why did you choose those particular approaches? What were the alternatives considered, and what were the trade-offs (e.g., performance, scalability, cost, maintainability, development speed)?**
    1.  **Dedicated LLM Microservice:**
        *   **Why:** Isolation (security, dependencies), independent scaling, easier model switching, centralizes LLM best practices (prompt engineering, cost management, rate limiting). Crucial for data privacy (no direct access to sensitive data from external vendor APIs).
        *   **Alternatives:** Directly integrating LLM clients into existing services.
        *   **Trade-offs:** Increased initial setup complexity, introduces another service to manage.
    2.  **Stateless LLM API Integration & Internal History:**
        *   **Why:** **Primary driver was data privacy and security.** Lyft could not send sensitive claims data to external vendors that might retain conversational state or use it for model training. This ensured all sensitive context remained within Lyft's secure boundaries.
        *   **Alternatives:** Using stateful vendor APIs.
        *   **Trade-offs:** Significantly increased development effort (building custom history management, context window handling), higher internal storage costs, potentially more complex prompt engineering.
    3.  **DynamoDB for Conversation History:**
        *   **Why:** High scalability, low-latency reads/writes, cost-effective for key-value lookups, perfect fit for storing conversation tree structures.
        *   **Alternatives:** Relational databases (e.g., PostgreSQL), other NoSQL databases.
        *   **Trade-offs:** Less flexible for complex analytical queries (though not needed for conversation history).
    4.  **Hybrid Document Extraction (Textract + LLM):**
        *   **Why:** Addresses limitations of each individual tool. Textract was strong for complex, structured forms but struggled with poor orientation/multi-lingual. Multi-modal LLMs handled those better but were more expensive and less precise for forms. This allowed us to optimize accuracy and cost.
        *   **Alternatives:** Pure Textract, Pure LLM, other OCR vendors.
        *   **Trade-offs:** Increased complexity in pipeline (routing, aggregation), requires more tuning.
    5.  **RAG with Elasticsearch:**
        *   **Why:** Leverage existing infrastructure expertise and investment in Elasticsearch. Its vector search (k-NN) capabilities were sufficient for our initial needs, and it's highly scalable.
        *   **Alternatives:** Dedicated vector databases (Pinecone, ChromaDB).
        *   **Trade-offs:** May not be as optimized as specialized vector databases for extremely high-dimensional vectors or specific search algorithms, but sufficient for our context.
*   **How did you ensure the system was scalable, reliable, performant, and maintainable?**
    *   **Scalability:**
        *   **K8s:** Services deployed on Kubernetes for horizontal auto-scaling based on load.
        *   **Asynchronous Processing:** SQS and Kafka for decoupling heavy processing (document intelligence) from user-facing requests, allowing independent scaling of workers.
        *   **DynamoDB/Elasticsearch:** Chosen for their inherent scalability for high read/write throughput and search operations.
        *   **Rate Limiting/Cost Optimization:** Implemented rate limits on LLM calls to manage cost and ensure fair usage, preventing cascading failures.
    *   **Reliability:**
        *   **Idempotent Operations:** Designed document processing to be idempotent to allow safe retries.
        *   **Retry Mechanisms:** Implemented robust retry logic for external LLM API calls and internal processing failures.
        *   **Circuit Breakers/Timeouts:** Configured timeouts and circuit breakers for external dependencies to prevent cascading failures.
        *   **Monitoring & Alerting:** Comprehensive logging, metrics, and alerting for service health, LLM latency/errors, and processing queues.
    *   **Performance:**
        *   **Stateless LLM calls:** Minimized latency by not relying on stateful vendor infrastructure.
        *   **Optimized Data Stores:** DynamoDB for low-latency chat history.
        *   **Parallel Processing:** For document intelligence (image pre-processing, chunk extraction), to reduce overall processing time.
        *   **Caching:** Considered caching LLM responses for common queries (though less applicable for dynamic claims data).
    *   **Maintainability:**
        *   **Microservices Architecture:** Clear separation of concerns, allowing teams to own and evolve services independently.
        *   **Modular Codebase:** Well-defined interfaces and abstractions for LLM models, document parsers, etc.
        *   **Code Reviews & Testing:** Rigorous code review process, comprehensive unit, integration, and end-to-end tests (including LLM specific tests for output quality).
        *   **Clear Documentation:** Extensive documentation of architecture, APIs, and operational runbooks.
*   **How did you consider future extensibility or new features when designing the system?**
    *   **Pluggable LLM Models:** The LLM service was designed to be agnostic to the underlying LLM provider, allowing easy switching between OpenAI, Claude, or future models without significant architectural changes.
    *   **Abstract Document Processing Pipeline:** The document intelligence pipeline was built with a modular design, allowing new extraction methods, summarization techniques, or post-processing steps to be added as plugins.
    *   **Agentic RAG Foundation:** The RAG pipeline was designed with an "agentic" approach (using tool calling), which makes it highly extensible for future features where LLMs can query various internal tools/data sources beyond just documents.
    *   **Standard API Contracts:** Clear REST API contracts for communication between services ensured easy integration of new features or consumers.
    *   **Data Model Flexibility:** The conversation history data model in DynamoDB was designed to be flexible enough to accommodate new types of interactions or metadata as the chatbot evolves.

**4. Impact & Metrics:**
*   **How did you measure the success of this project? What were the key performance indicators (KPIs)?**
    The success of this project was measured primarily through:
    *   **Operational Efficiency:**
        *   **Average Handle Time (AHT) Reduction:** For claims managed using the GenAI tools, especially for information extraction and summarization.
        *   **SLA Adherence:** Improvement in meeting internal and external SLAs for claims submission and processing.
        *   **Manual Effort Reduction:** Qualitative and quantitative feedback from advocates on reduced time spent on manual document review and information synthesis.
    *   **Claims Outcomes & Cost:**
        *   **Reserve Estimation Accuracy:** Improvement in initial reserve estimation for claims (especially with damage estimator).
        *   **Premium Impact (Long-term):** While a direct metric, this is a long-term goal dependent on aggregate loss history. The project aimed to contribute to this by improving data quality and processing efficiency.
    *   **User Adoption & Satisfaction:**
        *   **Feature Usage:** Tracking engagement with the AI Chatbot, document summaries, and Q&A features.
        *   **Advocate Feedback:** Direct qualitative feedback on usefulness, accuracy, and workflow improvement.
*   **Can you quantify the impact of your work? (e.g., "reduced latency by X%", "saved Y dollars annually," "increased user engagement by Z%," "enabled X new features per month").**
    *   **AI ChatBot:** Quantifiably **reduced information retrieval time for advocates by an estimated 30-50% for complex or long-running claims**. Advocates could "quickly get key insights into the claim, and got them up to speed" much faster than manually reviewing hundreds of notes. This directly contributed to reducing AHT for these types of claims.
    *   **Document Intelligence Pipeline:** Enabled **automated extraction and summarization of key information from complex documents, reducing manual review time by an estimated 20-40%** depending on document type and length. This directly improved the speed of FNOL ops in verifying information and marking claims ready for TPA submission, and claims ops in evaluating settlements.
    *   **Damage Estimator (Initial Impact):** Provided faster initial reserve estimation, allowing for more informed decision-making earlier in the claims lifecycle, potentially **reducing the risk of over-reserving by improving accuracy of initial damage assessment**.
    *   **Overall:** The project **enabled the strategic integration of GenAI across critical claims workflows**, paving the way for future automation and efficiency gains that were previously unattainable. It established a robust, privacy-compliant GenAI platform that can support multiple future AI-driven features. While direct dollar savings on premiums are long-term and aggregate, the foundation laid is critical to achieving those.
*   **What was the ultimate outcome or benefit to the business or users?**
    The ultimate outcome was a significant step towards a more **efficient, accurate, and cost-effective claims management system** for Lyft. For **business**, it meant laying the groundwork for potentially lower insurance premiums and better financial management of risk. For **users** (claims ops, FNOL ops, legal), it translated into:
    *   **Reduced mundane work:** Less time spent reading lengthy documents and searching for information.
    *   **Faster workflows:** Quicker information extraction and claim assessment, leading to better SLA adherence.
    *   **Improved decision-making:** Better visibility into claim severity and key information, enabling more strategic guidance to adjusters and more informed settlement evaluations.
    *   **Increased job satisfaction:** By offloading repetitive tasks and providing intelligent assistance.

**5. Challenges & Solutions:**
*   **What were the most significant technical challenges you faced during this project?**
    1.  **Greenfield Project Ambiguity:** Starting with no clear path or defined goals for GenAI integration.
    2.  **Data Privacy & Stateless APIs:** Integrating LLMs while adhering to strict data privacy rules (no sensitive data sent to stateful vendor APIs) and managing conversation history internally.
    3.  **Complex Document Processing:** Handling large, scanned, and structurally complex PDFs (multi-column, multi-lingual, poor orientation) for accurate text extraction and summarization within performance SLAs.
    4.  **Scaling and Orchestrating LLM Calls:** Managing rate limits, cost, and ensuring high throughput for various LLM interactions across different features.
    5.  **LLM Limitations & Hallucinations:** Designing systems that accounted for LLM inaccuracies and potential hallucinations, especially for critical operational workflows.
    6.  **Optimal RAG Chunking:** Determining effective chunking strategies for diverse document formats within the RAG pipeline to ensure relevant retrieval.
*   **How did you approach solving these challenges? What steps did you take?**
    1.  **Greenfield Ambiguity:**
        *   **Approach:** I took initiative to research, prototype, and define a compelling vision for GenAI in claims, focusing on high-impact pain points.
        *   **Steps:** Started with basic POCs (e.g., a simple Q&A bot) to demonstrate feasibility. Partnered with product and ops to validate ideas, identified clear initial milestones (AI Chatbot, then Document Intelligence) that delivered incremental value, which helped secure resources and buy-in.
    2.  **Data Privacy & Stateless APIs:**
        *   **Approach:** Built a custom, lightweight LLM orchestration service to manage all LLM interactions and persist state locally.
        *   **Steps:** Designed a conversation tree data model in DynamoDB to store full chat history. Ensured all sensitive data remained within Lyft's secure boundaries, only sending anonymized/non-sensitive portions to external LLMs. Rigorous security reviews.
    3.  **Complex Document Processing:**
        *   **Approach:** Developed a hybrid document intelligence pipeline combining specialized OCR (AWS Textract) with the flexibility of multi-modal LLMs, supported by robust asynchronous processing.
        *   **Steps:** Conducted extensive research and experimentation with hundreds of varied documents. Built a scalable image pre-processing module. Implemented parallel extraction for large documents. Added SQS-based retry mechanisms and aggregation logic to reassemble chunks into a coherent document.
    4.  **Scaling and Orchestrating LLM Calls:**
        *   **Approach:** Centralized LLM interaction logic within a dedicated service with built-in rate limiting, caching, and model routing.
        *   **Steps:** Leveraged K8s for auto-scaling the service. Implemented internal rate limiters and cost monitoring. Abstracted LLM provider APIs to allow easy switching or routing based on use case/cost/performance.
    5.  **LLM Limitations & Hallucinations:**
        *   **Approach:** Designed for "human-in-the-loop" and iterative refinement, focusing on augmentation rather than full automation initially.
        *   **Steps:** Clearly communicated LLM limitations to users and stakeholders. Implemented confidence scores and flags for potentially problematic outputs. Focused on summarization and Q&A where human verification is natural, gradually building trust and improving accuracy.
    6.  **Optimal RAG Chunking:**
        *   **Approach:** Experimented with diverse chunking strategies tailored to different document formats (e.g., recursive character, semantic, custom rules for legal documents).
        *   **Steps:** Built a flexible chunking framework. Performed A/B testing and evaluated retrieval relevance metrics with ops users. Iteratively refined chunk sizes and overlap to optimize for the unique characteristics of legal and medical documents.
*   **Were there any major design flaws or technical debt you encountered or introduced? How were they addressed, or how would you address them in the future?**
    An initial design assumption for document processing underestimated the CPU intensity and potential bottlenecks of image pre-processing for very large, high-resolution scanned PDFs. This led to occasional processing backlogs.
    *   **Addressing:** We addressed this by:
        1.  **Optimizing Image Algorithms:** Further refining image processing algorithms to be more efficient.
        2.  **Increased Parallelization:** Enhancing the parallel processing capabilities within the pipeline.
        3.  **Dedicated Resource Pools:** Allocating more dedicated K8s resources for the image pre-processing stage and allowing for aggressive horizontal scaling.
        4.  **Asynchronous Queuing:** Reinforcing the use of SQS to buffer tasks, preventing backpressure on ingestion.
    *   **Future Addressing:** In the future, I would explore dedicated GPU/CPU accelerated inference endpoints if image processing becomes a persistent bottleneck at much larger scales, or offload some of the most intensive pre-processing steps to specialized media processing services. Additionally, building more granular monitoring for each sub-step of the pipeline would help identify bottlenecks faster.
*   **What non-technical challenges did you encounter (e.g., scope creep, resource constraints, conflicting priorities)? How did you handle them?**
    1.  **Greenfield Ambiguity & Resource Constraints:** At the very beginning, it was just me with no dedicated resources.
        *   **Handling:** I self-started by building lightweight POCs and a clear technical vision. I proactively engaged with engineering leadership and product management, demonstrating the potential value and aligning it with company objectives. This tangible progress helped secure initial resource allocation (PM, then FE/BE engineers).
    2.  **Scope Creep (Common with GenAI):** Everyone had exciting ideas for GenAI, leading to potential expansion beyond the initial focus.
        *   **Handling:** I partnered very closely with the Product Manager to maintain a laser focus on the most impactful pain points identified by the claims ops team. We prioritized ruthless and defined clear, iterative milestones (Chatbot -> Document Intelligence -> RAG) to deliver value incrementally and manage expectations, deferring less critical features.
    3.  **Conflicting Priorities:** Balancing the long-term strategic investment in GenAI with immediate operational needs and other team initiatives.
        *   **Handling:** I consistently articulated the strategic value of GenAI to leadership and cross-functional partners, emphasizing its potential for significant long-term cost savings and efficiency gains. I used data-driven arguments (even qualitative feedback initially) to show the value proposition. For daily prioritization, I worked with the PM to ensure GenAI tasks were integrated into broader team sprints based on business impact.

### **Part 2: Leadership, Influence & Behavioral Aspects**

**1. Technical Leadership & Mentorship:**
*   **How did you provide technical guidance or leadership to your team or other engineers on this project?**
    I provided technical guidance by:
    *   **Architectural Stewardship:** Leading architectural discussions and decisions, ensuring the chosen solutions were scalable, reliable, and maintainable.
    *   **Design Reviews:** Conducting rigorous design reviews for new features and components, challenging assumptions, and guiding engineers towards robust solutions.
    *   **Code Quality:** Setting standards for code quality, conducting thorough code reviews, and advocating for best practices (e.g., prompt engineering principles, error handling, testing strategies specific to LLMs).
    *   **Problem Solving:** Being a hands-on contributor, diving into complex technical issues with the team, and helping unblock engineers.
    *   **Knowledge Sharing:** Championing internal discussions and documentation around LLM capabilities, limitations, and effective integration patterns.
*   **Did you mentor or formally/informally coach junior engineers? Can you give an example?**
    Yes, I formally and informally mentored the backend engineers on the team.
    *   **Example:** One of the backend engineers was new to working with distributed systems and asynchronous processing, particularly for the document intelligence pipeline. I coached them on designing the SQS-based processing workflow, explaining the importance of idempotency, effective retry strategies, and handling partial failures. I worked with them on breaking down the complex problem of parallel PDF chunk extraction and aggregation, guiding their design choices and reviewing their code for error resilience and scalability. This involved pair programming sessions and detailed whiteboard discussions. This mentorship significantly improved their understanding of building robust, scalable backend systems.
*   **How did you help elevate the technical skills or understanding of your team?**
    *   **Technical Deep Dives:** Organized weekly "AI Lunch & Learn" sessions where we discussed LLM research papers, new techniques (like RAG variations, prompt engineering patterns), and shared insights from our own experimentation.
    *   **Hands-on Experimentation:** Encouraged and facilitated engineers to spend time prototyping with LLMs and new frameworks, fostering a culture of continuous learning.
    *   **Clear Design Principles:** Articulated and enforced clear design principles for LLM integration, ensuring consistency and maintainability across the codebase.
*   **How did you influence the technical direction of the project or team beyond your direct coding contributions?**
    I influenced the technical direction by:
    *   **Strategic Vision Setting:** Advocating for the long-term strategic investment in a custom LLM orchestration service and document intelligence pipeline, rather than relying on simpler, potentially less compliant, or less flexible vendor solutions. This enabled greater control, privacy, and extensibility.
    *   **Technology Selection:** Guiding the team's choices for data stores (DynamoDB for conversation history, Elasticsearch for RAG) and processing paradigms (asynchronous SQS workflows).
    *   **Risk Management:** Proactively identifying and mitigating technical risks related to data privacy and LLM accuracy, shaping the system's design to be resilient to these challenges.

**2. Collaboration & Cross-Functional Work:**
*   **How did you collaborate with other teams (e.g., product, QA, design, operations, other engineering teams) to ensure the project's success?**
    *   **Product:** Maintained a continuous feedback loop, collaborating closely on defining user stories, prioritizing features based on business impact, and refining requirements as LLM capabilities and limitations became clearer.
    *   **Design:** Partnered with designers to create intuitive UX for the chatbot and document summary interfaces, ensuring technical feasibility aligned with user needs and visual design.
    *   **Operations (End Users):** Conducted frequent user interviews, demos, and usability tests with Claims Ops and FNOL Ops to gather direct feedback on pain points, validate proposed solutions, and iterate rapidly. This ensured the solutions were truly solving their problems.
    *   **Legal:** Engaged early and continuously with the Legal team to address data privacy concerns related to sending data to external LLMs, ensuring our architecture was compliant with Lyft's policies.
    *   **ML Platform/Infra:** Collaborated with the ML Platform team for leveraging their foundational libraries for interacting with OpenAI/AWS services, and with core Infra for K8s deployment and monitoring.
*   **Describe a situation where you had to persuade stakeholders or other teams about a technical decision. What was the outcome?**
    **Situation:** Early in the project, there was a discussion about whether to rely solely on a third-party document processing vendor that offered "black box" solutions, or to build a more custom, hybrid document intelligence pipeline internally. The vendor solution seemed simpler initially.
    **Task:** My task was to persuade product and engineering leadership that the custom, hybrid approach was the right long-term technical decision, despite its higher initial investment.
    **Action:** I prepared a detailed technical analysis outlining the trade-offs:
    *   **Privacy:** Highlighting the critical concern of sending sensitive, unstructured claims documents to a vendor who might retain/process the data, contrasting this with our internal approach where sensitive data stays within Lyft's environment.
    *   **Accuracy & Control:** Demonstrating, through POCs, that a single vendor often struggled with the extreme complexity, poor scans, and diverse layouts of our specific document types (e.g., medical reports, police reports), whereas a hybrid approach combining Textract and LLMs offered superior, tailored accuracy.
    *   **Cost-Efficiency:** Projecting that while initial build cost was higher, long-term operational costs and the ability to optimize LLM calls with our specific traffic patterns would be more favorable.
    *   **Extensibility:** Emphasizing that an internal pipeline allowed us to easily integrate future specialized models (e.g., for specific legal document types) or new technologies.
    **Outcome:** Based on the compelling privacy and accuracy arguments, and a clear architectural roadmap, I successfully persuaded the stakeholders. We proceeded with building the custom hybrid document intelligence pipeline, which ultimately proved to be highly effective and enabled unique capabilities tailored to our needs, while maintaining strict privacy compliance.
*   **How did you handle disagreements or conflicts with team members or other stakeholders regarding technical approaches or priorities?**
    My approach is to foster a culture of open debate, where decisions are driven by data, trade-offs, and alignment with project goals, not by hierarchy or opinion.
    1.  **Seek Understanding:** First, I ensure I fully understand the other person's perspective, concerns, and underlying assumptions.
    2.  **Data-Driven Discussion:** I bring objective data, POC results, and clear pros/cons of each technical approach to the discussion. For priorities, I refer back to user feedback and business impact metrics.
    3.  **Focus on Shared Goals:** Reframe the disagreement around the overarching project and organizational goals. How does each proposed approach best contribute to them?
    4.  **Explore Alternatives:** Facilitate brainstorming for alternative solutions that might satisfy conflicting requirements.
    5.  **Compromise & Iteration:** If a clear "best" solution isn't evident, explore a phased approach or a compromise that allows for iterative learning.
    6.  **Leadership Decision (If Necessary):** If consensus cannot be reached after thorough discussion, I make a decision as the technical lead, clearly articulating the rationale and committing to owning the outcome.

**3. Strategic Thinking & Problem Solving:**
*   **Describe a time you identified a significant technical problem or opportunity that wasn't immediately apparent to others. What did you do about it?**
    **Problem/Opportunity:** The initial greenfield GenAI initiative at Lyft started with a very broad mandate: "Lead GenAI for Claims & Accidents." There was no clear vision or defined technical problem to solve, only a general interest in LLMs. The significant opportunity I identified was transforming core claims operations, not just building a generic chatbot. Specifically, the acute pain of *manual document analysis* for claims ops, which was hidden behind "long AHT" metrics. This was not immediately apparent as the first thought for LLMs often defaults to simple Q&A.
    **What I Did:**
    1.  **Deep Dive into Operations:** I proactively spent time with the Claims Ops and FNOL Ops teams, observing their workflows and pain points directly. This revealed that a major bottleneck was the manual reading and extraction of information from complex, large, and often scanned PDF documents (police reports, medical records, lawsuits). This was a much deeper and more impactful problem than just general Q&A.
    2.  **Prototyping & Vision:** I then ideated and prototyped how multi-modal LLMs and advanced OCR could automate this document intelligence. I developed a clear technical vision for a "Document Intelligence Pipeline" and explained its direct impact on AHT, SLA, and cost reduction.
    3.  **Socialization & Advocacy:** I presented this vision and early prototypes to product management, engineering leadership, and the ops teams, illustrating how it directly addressed their core problems. This proactive identification and articulation of the problem, combined with a compelling technical solution, transformed the ambiguous GenAI mandate into a concrete, high-impact project, leading to its prioritization and resource allocation.
*   **How do you prioritize your work when faced with multiple competing demands or critical issues?**
    I prioritize based on a combination of business impact, technical urgency/risk, and strategic alignment:
    1.  **Business Impact:** What delivers the most value to users or the business (e.g., cost savings, efficiency gains, revenue impact)? I collaborate with Product to define this.
    2.  **Urgency & Criticality:** Is there a production incident? A security vulnerability? An SLA breach? These take immediate precedence.
    3.  **Technical Debt & Risk Reduction:** Addressing critical technical debt or architectural flaws that pose significant future risks or hinder progress.
    4.  **Strategic Alignment:** How does the work align with the long-term vision and organizational goals? Foundational work, even if not immediately impactful, might be crucial for future growth.
    5.  **Dependencies & Unblocking:** Prioritizing work that unblocks other teams or critical paths.
    I use structured approaches like Eisenhower Matrix (Urgent/Important) and regularly sync with Product and stakeholders to ensure alignment on priorities, transparently communicating trade-offs.
*   **How do you decide when to build a solution versus using an existing one (buy vs. build)?**
    This decision is critical and involves a multi-faceted analysis:
    1.  **Core Competency:** Is this a core competency for Lyft? If it's a differentiator (like our claims processing logic), we build. If it's a commodity (like foundational LLM models or basic cloud infrastructure), we buy/use.
    2.  **Data Privacy & Security:** Can the "buy" option meet our stringent data privacy and security requirements? (This was a primary driver for building our own LLM orchestration service and hybrid document pipeline for sensitive claims data).
    3.  **Cost:** Total Cost of Ownership (TCO) – build vs. buy, including licensing, operational costs, maintenance, and future scalability.
    4.  **Customization & Flexibility:** Does the existing solution offer the necessary level of customization and flexibility for our specific use cases and future needs? Our complex document layouts, for example, often exceeded off-the-shelf capabilities.
    5.  **Integration Effort:** How much effort is required to integrate the existing solution into our ecosystem?
    6.  **Time to Market:** Can building it internally deliver value faster than integrating a complex external solution, or vice versa?
    7.  **Vendor Lock-in & Portability:** What are the risks of vendor lock-in, and how easily can we switch providers if needed?
    For this project, we chose to "buy" foundational LLM models (OpenAI, Claude) because they are commodity and building our own foundation model was not feasible. However, we chose to "build" the orchestration layer on top and a hybrid document intelligence pipeline because of the unique **data privacy requirements, the need for extreme customization for complex document layouts, and the desire for long-term control and extensibility.**
*   **Describe a complex problem where there wasn't a clear solution. How did you break it down and approach it?**
    **Problem:** Accurately extracting information from highly complex, large, often scanned, multi-lingual, and multi-column PDF documents within an acceptable SLA for the Document Intelligence pipeline. There was no single vendor or LLM that could reliably handle all variations.
    **Breakdown & Approach:**
    1.  **Decomposition:** I broke the problem down into sub-problems:
        *   **Ingestion:** How do documents enter the system reliably? (SQS/Kafka).
        *   **Pre-processing:** How do we optimize scanned images for OCR/LLM? (Image enhancement, orientation correction).
        *   **Text Extraction Strategy:** What's the best way to get text out? (Hybrid Textract vs. LLM investigation).
        *   **Large File Handling:** How to deal with PDFs too big for single LLM context windows? (Chunking).
        *   **Post-Extraction Processing:** How to re-assemble and structure extracted text? (Aggregation, summarization).
        *   **Error Handling & Retries:** What happens when things fail? (Robust retry mechanisms, dead-letter queues).
        *   **Performance & Scalability:** How to meet SLAs for processing time? (Parallelization, K8s scaling).
    2.  **Research & Experimentation:** For the "Text Extraction Strategy" and "Large File Handling" sub-problems, I conducted extensive research. I tested AWS Textract, various multi-modal LLMs (OpenAI, Claude) on a diverse dataset of hundreds of real claims documents, meticulously evaluating their accuracy on different document types (structured forms, free-text legal, medical records, invoices, etc.).
    3.  **Hybrid Solution Design:** The experimentation revealed that no single tool was perfect. This led to the design of the **hybrid approach**: routing documents based on their complexity/type, and combining Textract for structured forms with multi-modal LLMs for unstructured, multi-column, or poorly scanned documents.
    4.  **Iterative Prototyping:** I built small, focused POCs for each sub-problem (e.g., a service to just handle PDF chunking, another for image pre-processing) to validate technical feasibility and performance characteristics before integrating them into the larger pipeline.
    5.  **Monitoring & Tuning:** Once built, we implemented granular monitoring at each stage of the pipeline to identify bottlenecks and iteratively tuned chunking strategies, LLM parameters, and parallel processing configurations to meet performance SLAs.

**4. Learning & Growth:**
*   **What did you learn from this project, both technically and professionally?**
    *   **Technically:**
        *   **Deep LLM Understanding:** Gained in-depth knowledge of LLM architectures, prompt engineering, RAG patterns, multi-modal LLMs, and their practical integration challenges (context window, cost, latency, hallucinations).
        *   **Building for Ambiguity:** Learned how to build robust, scalable systems in a rapidly evolving technological landscape (GenAI) with initially undefined requirements.
        *   **Privacy-Centric Design:** Mastered the art of designing systems that handle sensitive data with external AI services, prioritizing data privacy and security above all else.
        *   **Advanced Document Processing:** Gained expertise in complex OCR, text extraction, and information summarization from unstructured data.
    *   **Professionally:**
        *   **Greenfield Project Leadership:** Learned to lead a greenfield initiative from ideation to production, including vision setting, resource acquisition, and stakeholder management.
        *   **Managing Expectations:** Became adept at communicating the promise and limitations of new technologies (GenAI) to non-technical stakeholders.
        *   **Cross-Functional Alignment:** Reinforced the importance of deep, continuous collaboration with Product, Design, and Ops to ensure technical solutions truly address user needs.
        *   **Advocacy & Influence:** Improved skills in building a compelling case for new technical investments and persuading stakeholders.
*   **If you could restart this project, what would you do differently and why?**
    If I could restart, I would prioritize building out a more comprehensive **LLM evaluation framework** earlier in the project.
    *   **Why:** While we did extensive manual testing and gathered user feedback, a robust automated framework for evaluating LLM outputs (e.g., ROUGE, BLEU, custom semantic similarity metrics, truthfulness scores) would have allowed for faster iteration on prompt engineering, chunking strategies, and model selection. It would have also provided more objective, quantifiable data to demonstrate improvements and make better decisions regarding LLM tuning, rather than relying solely on qualitative feedback or manual review. This would have accelerated our path to higher accuracy and reliability.
*   **Describe a time you made a significant technical mistake. What was the impact, and what did you learn from it? How did you ensure it wouldn't happen again?**
    **Mistake:** During the initial development of the document intelligence pipeline, I underestimated the complexity and variability of PDF rendering libraries and the CPU overhead involved in pre-processing scanned images before sending them for OCR/LLM analysis. I assumed a single, simpler image processing library would suffice for most cases. This led to intermittent failures for highly degraded or complex scans, and significantly higher CPU usage and longer processing times than anticipated for large documents, causing occasional backlogs in the SQS queue.
    **Impact:** This resulted in missed SLAs for processing some complex documents and a suboptimal advocate experience due to delays. It also increased our infrastructure costs due to the need for more CPU-heavy K8s pods to compensate.
    **Learned:** I learned the critical importance of:
    1.  **Robust Edge Case Testing:** Exhaustively testing with a wider, more challenging set of real-world "dirty" data early in the development cycle.
    2.  **Profiling & Benchmarking:** Thoroughly profiling resource usage and benchmarking performance of critical path components (like image processing) before scaling up.
    3.  **Specialized Tooling:** Recognizing when a seemingly simple problem requires specialized, often more complex, libraries or services for robust handling of corner cases.
    **Ensuring it wouldn't happen again:**
    *   **Comprehensive Test Datasets:** We built a much more diverse and challenging dataset of production documents for automated testing, specifically targeting known problem areas (bad scans, complex layouts).
    *   **Pre-computation & Offline Processing:** Wherever possible, we now separate CPU-intensive pre-processing into dedicated, asynchronously processed stages, allowing for independent scaling and failure handling.
    *   **Service Level Indicators (SLIs) for Sub-components:** We implemented more granular monitoring metrics at each stage of the document processing pipeline to quickly identify bottlenecks and performance degradation at a specific component level, rather than just overall system latency.
    *   **Post-Mortem Culture:** Fostered a blameless post-mortem culture to systematically analyze failures and extract actionable lessons, ensuring process and design improvements are captured.
*   **How do you stay current with new technologies and industry trends?**
    *   **Industry Blogs & Newsletters:** Subscribe to leading AI/ML research blogs (e.g., Google AI, OpenAI, DeepMind), engineering blogs from top tech companies, and industry newsletters (e.g., TLDR AI, The Batch).
    *   **Academic Papers:** Regularly browse pre-print archives like ArXiv for new research papers in LLMs, ML, and systems design.
    *   **Conferences & Webinars:** Attend key industry conferences (e.g., NeurIPS, KubeCon, industry-specific tech summits) and participate in webinars.
    *   **Hands-on Experimentation:** Continuously experiment with new models, frameworks, and libraries (e.g., LangChain, LlamaIndex, new open-source LLMs) to understand their practical applications and limitations.
    *   **Internal Knowledge Sharing:** Actively participate in and lead internal tech talks, knowledge-sharing sessions, and engineering discussions within Lyft.

**5. Culture & Team Contribution:**
*   **How do you contribute to fostering a positive and productive team culture?**
    *   **Psychological Safety:** I prioritize creating an environment where team members feel safe to voice ideas, ask questions, admit mistakes, and challenge assumptions without fear of judgment.
    *   **Blameless Post-Mortems:** Championed a blameless culture around incidents and errors, focusing on system and process improvements rather than individual blame.
    *   **Celebration of Wins:** Ensured that team successes, big or small, were recognized and celebrated, fostering morale and motivation.
    *   **Collaboration & Empathy:** Encouraged pair programming, open discussions, and active listening. Fostered empathy for our users (claims ops) by bringing their challenges to the forefront of our discussions.
    *   **Leading by Example:** Maintained a hands-on approach, demonstrating commitment, ownership, and a willingness to tackle challenging problems alongside the team.
*   **Describe a time you took initiative to improve team processes, tools, or collaboration.**
    **Initiative:** Recognizing that the GenAI project was rapidly evolving and involved complex LLM interactions, I took the initiative to introduce a lightweight **RFC (Request for Comments) process** for major architectural decisions and LLM integration patterns.
    **Action:**
    1.  I proposed the RFC format as a way to solicit structured feedback on significant technical designs early in the process.
    2.  I drafted the first few RFCs myself (e.g., for the LLM service architecture, the document intelligence pipeline) to demonstrate the format and value.
    3.  I facilitated discussions around these RFCs, ensuring all team members and relevant stakeholders (product, other teams) had an opportunity to review, provide feedback, and understand the rationale behind decisions.
    **Impact:** This formalized a process for technical alignment, significantly improved the quality of our designs by incorporating diverse perspectives, reduced misunderstandings, and created a valuable knowledge base for onboarding new team members. It also empowered junior engineers to contribute to high-level design discussions.
*   **How do you ensure code quality and maintainability within your team?**
    *   **Rigorous Code Reviews:** Enforce a culture of thorough code reviews, focusing not just on correctness but also on readability, maintainability, adherence to best practices, and future extensibility. I provide constructive, actionable feedback.
    *   **Clear Coding Standards:** Establish and communicate clear coding guidelines, including style guides, common design patterns, and specific best practices for LLM integration (e.g., prompt versioning, observability of LLM calls).
    *   **Automated Testing:** Champion comprehensive testing strategies – unit tests, integration tests, and end-to-end tests. For LLM features, we also focused on building evaluation metrics for output quality.
    *   **Documentation:** Encourage developers to document their code, APIs, and key architectural decisions, making it easier for new team members to ramp up and for existing members to understand complex systems.
    *   **Refactoring Culture:** Promote continuous refactoring to address technical debt proactively and improve code hygiene.
*   **How do you give and receive constructive feedback? Provide an example.**
    **Giving Feedback:** I believe feedback should be specific, actionable, timely, and focused on behavior/impact, not personal attributes. I use the SBI (Situation-Behavior-Impact) model.
    *   **Example (Giving):** "During the recent incident with the document processing pipeline (Situation), I noticed that you reverted to a previous version of the code without first consulting the team or updating the incident channel (Behavior). This led to confusion for the on-call engineer and delayed our understanding of the root cause, adding about 15 minutes to resolution time (Impact). In the future, please ensure you communicate such critical actions immediately in the incident channel and involve the team for critical changes during an incident."
    **Receiving Feedback:** I approach feedback with an open mind, assuming positive intent, and view it as an opportunity for growth. I actively listen, ask clarifying questions, and avoid defensiveness.
    *   **Example (Receiving):** "Thanks for the feedback. When you mentioned I was 'too focused on the technical details' during the product demo (Feedback), could you give me a specific example of when that happened, and what you would have preferred I focused on instead? (Clarifying question). My intent was to show the robustness of the solution, but I see how that might have overshadowed the user benefits (Acknowledging impact). I'll work on tailoring my communication more to the audience next time." I then consciously practice focusing on business value and user benefits in subsequent product demos.



## Meta Questions
- Someone give you Peer feedback gave for improvement
	- Don't heavily rely on PM, feel free to take more ownership
		- set up 1:1 with PM, provide deadline
    
- Pivot mid project and changing requirements
	- content extraction with UI
	- Legal integration, teammate left, reprioritize
    
- Most diff working relationship
	- Alan
	- New Boss
    
- When faced Pushb back regarding your project
	- staff PM was not onboard
	- took support from Ops stakeholders to get alignment
    
- Adopt experimental to solve something
	- wallet add redesign
	- auth redesign 
    
- Lead**er ask you to som**ething that is not highest priority for you, how did you solve it
	- implementing RAG pipeline soon after ChatBot rather than wait for Doc
    
- Volunteer to take critical part of project 
	- Livery rearchitecture
    
- Needed to act quickly on something but no clear idea how to 
	- False positive from openai
    
- When you didn’t have all desired info to solve tech problem and how you resolved it
	- Textract vs LLM
	- openai bug ➙ claude integration
    
- Over come barrier to achieve end result 
	- openai bug
	- 
    
- Competing priorities to deliver on a project
	- AI initiatives ➙ AV launch
	- How would you talk about it? ()
    
- Significant setback tht forced you to erpriotized your work
	- Leading a project related to legal integration with tight timelines. Teammate left. So I had to reprioritize the timelines and also other things I was working on to speed this up
    
- Achivement that youre’ most  proud of
    
- Critical decision with missing or conflict information
	- textract vs LLM
    
- Scope creep, but estimated lwo, so timeline would miss so how did you manage to work on it
	- extraction with UI
    
- Greatest develeoptment opprotunituty area 
	- increasing the scope across more business teams outside the org
    
- Late breaking tech issue that launched release that happening in a week or less
	- openai bug

- Conflict
	- Teammates
		- technical decisions back and forth
	- Leadership
		- staff PM wasn't onboard
	- Peers EM
		- ownership encroachment
		- feedback related conflicts

**
- **Major Setback / Launch Delay**: legal integration, teammate left
- **Convince / Conflict**: staff PM not onboard
- **Investigative / Ambiguity**: textract vs LLM
- **Unexpected Setback**: openai bug
- **Volunteer / Leadership**: livery rearchitecture
- **ScopeCreep**: content extraction, UI changes
- **Pushback With Proof**: RAG implmentation, Not Needed in the beginning — pushed back to later
- **Prioritization** : AI initiatives ➙ AV launch

## Anthropic

#### Cultural Interview
- Goal
	- Understand Vinyas' values, motivations, and potential contributions
	- Genuine mission and alignment with values
- Important
	- Core Mission
		- Build **reliable**, **interpretable** and **steerable** AI systems that truly have humans at their core
		- Address **unpredictability**, **unreliability** and **opaqueness** 
	- Moto
		- *Prioritize safety, reliability and alignment rather than **speed***
	- AI Vision
		- Focused on safety
		- Solve humanity's most pressing challenges
		- By addressing risks responsibly
		- Revolutionize healthcare, longevity and address mental illness 
	- AI Safety Mission
	- Core Values
		- Act for the **Global Good**
			- focus on positive outcomes for humanity
		- Hold **Light and Shade**
			- recognize both positive and negative of AI
		- Be good to our **users**
			- Be kind, generous for everyone impacted by techonlogy 
		- Ignite Race to the Top on **SAFETY**
			- Inspire to develop safe and secure AI
		- Do **Simple thing that works**
			- practical approach focused on impact rather than method sophistication 
		- Be **Helpful, Honest and Harmless** (HHH)
			- high trust, low ego where everyone contributes
		- Put **Mission First**
			- shared purpose allowing switf action without competing goals
	- Unique Approach
		- Helpful, Honest, Harmless
		- Constitutional AI
		- Integrated Safety
		- Interpretability Research — opening the black box to build systems that can be audited and understood
	- Company Culture
		- Interdisciplinary Collaboration
		- Pragmatic Problem Solving (do simple thing that works)
		- Mission Driven
		- Public Benefit Corp (mission over money)
		- Opennes to the Field (publish research / tools for broader AI safety)
	- Why am I excited about Anthropic's work?
	- How my values align with Anthropic's values?


Words
- Safety
- Reliability
- Interpretability
- Responsible
- Constitutional AI
- Humanity
- Alignment
- Helpful, Honest and Harmless

Examples
- 

Why work for Anthropic? 
- **PSC** — My interest in Anthropic is driven by few main factors: the chance to **solve pragmatic**, high-impact problems; the company's principled, **safety-first** approach to development; and the opportunity to join a uniquely **collaborative**, mission-driven team.
	- p - pragmatic : solve problem practically, do simple thing first before taking on sophistication (RAG etc)
	- s - safety : data privacy, stateless API, deal with sensitive data, work with openai to enable ZDR. 
	- c - collaborative: currently work with legal, claims, designers, US, Canada, Poland, front end etc

Favorite part about Anthropic?
 My favorite part is Anthropic's commitment to leading AI Safety. In an industry often focused on speed, Anthropic has the courage to publicly discuss the risks—what you call **'holding light and shade.'** This isn't just talk; it's backed by concrete actions like developing **Constitutional AI** and structuring as a **Public Benefit Corporation**. It builds a deep level of trust and signals a commitment to long-term, responsible innovation, which is exactly the kind of environment I want to be a part of.


How did you handle HHH? 
- Helpful — impact driven, time saving from tedious tasks
- Honest — targeted prompt engineering, smaller context window, well defined request structure and labelled data. Prompt response would have "needs review" for document
- Harmless — create awareness among users about potential inconsistencies. Human in the loop. Creating products where a spectrum of errors are acceptable. Prompt best practices, and ensure than it's only for strictly internal use. 


What would you do differently? 
- Propose for more investment in UX — UI changes, streaming
- Better analytics from the beginning

Blogs
- Building effective agents — workflow vs agents
- Economic Index — shows which fields seeing high AI use (software and art)
- MCP when it was launched

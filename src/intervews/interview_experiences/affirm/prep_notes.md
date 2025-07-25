# Affirm
## Company Specifics
- **Business Model:**
    - Primary focus: Buy Now, Pay Later (BNPL) financing for consumers.
    - Revenue: Earns fees from merchants and interest from longer-term consumer loans.
    - Underwriting: Uses proprietary data-driven models beyond traditional credit scores.
    - Transparency: Emphasizes no late fees; simple interest for longer terms.
- **Market Position:**
    - Leading player in the competitive BNPL industry.
    - Known for significant partnerships with major retailers.
- **Key Competitors:**
    - Direct BNPL rivals: Klarna, Afterpay (Block), Zip, Sezzle.
    - Broader landscape: Traditional lenders, credit card companies, and payment platforms (e.g., PayPal, Apple Pay) integrating BNPL.
- **Regulatory Environment:**
    - Increasing scrutiny globally, especially on consumer protection.
    - Key concerns: Disclosure of terms, responsible lending practices, and potential classification as credit products.

## Tech Challenges
- **Core Products:**
    - **Point-of-Sale Financing:** Flagship offering, allowing consumers to pay in installments. Includes
        - "Pay in 4": Interest-free, bi-weekly payments.
        - Longer-term monthly installment options: With simple interest (0% to 36% APR).            
    - **Adaptive Checkout:** Personalizes payment options based on user profiles and cart contents.
    - **Affirm Card:** A physical and virtual debit card that allows users to convert eligible debit transactions into installment payments via the app
    - **Savings Account:** Offers a savings product
    - **Personal Loans:** Provides unsecured personal loans for various consumer need
- **Underlying Technology/Architecture:**
    - **Architecture Style:** Primarily uses a **microservices architecture**, which aids in independent scaling, development, and fault isolation
    - **Cloud Provider:** Heavily leverages **AWS** (Amazon Web Services) for its infrastructure
    - **Containerization:** Services run on **Amazon EKS (Kubernetes)**
    - **Database Strategy:** Focuses on highly durable and strongly consistent database architectures, utilizing **AWS Aurora MySQL** and exploring **Distributed SQL** (e.g., Spanner, Vitess, TiDB, CockroachDB), DynamoDB, and caching solutions
    - **Real-time Decisioning:** Critical for credit underwriting and fraud detection, requiring low-latency processing during checkout
    - **High Availability:** Aims for 99.99% availability (four 9s) for its checkout service, implementing multi-availability zone redundancy within a single region and having a Disaster Recovery plan for cross-region failover
    - **API Design:** Uses presentation-oriented APIs and Backend for Frontends (BFFs) to optimize performance and security for various client applications
    - **Data-Driven Core:** Extensive use of data analytics and machine learning for underwriting, risk management, and sophisticated fraud detection models
- **Tech Stack (Specifics):**
    - **Programming Languages:**
        - **Backend:** Primarily **Python** (with Flask and Django frameworks) and **Kotlin**, also Java, Ruby. Python is key for data science (scikit-learn, pandas, NumPy)
        - **Frontend:** JavaScript (with React, jQuery, Redux), HTML5, CSS3
        - **Mobile:** Swift (iOS), Kotlin (Android), React Native/Flutter
    - **Databases:** AWS Aurora (MySQL), Postgres, DynamoDB, S3
    - **Tools & Frameworks:** Docker, Kubernetes, Jenkins, Gradle, Webpack, Buildkite, Istio VirtualService, RabbitMQ, Celery, NGINX
- **Scalability Challenges:**
    - **High Transaction Volume & Real-time Processing:** Handling massive and fluctuating transaction loads, especially for instantaneous credit decisions at checkout
    - **Distributed Systems Complexity:** Managing and scaling distributed databases across regions, including challenges like active resharding and ensuring global availability
    - **Fraud and Risk Management:** Continuously evolving machine learning models to detect and prevent sophisticated fraud patterns in real-time, balancing fraud prevention with minimizing false positives and maintaining a smooth user experience
    - **Data Consistency & Integrity:** Ensuring the correctness and integrity of data that drives critical financial decisions, both online and for offline model training
    - **System Reliability & Availability:** Maintaining extremely high uptime (e.g., 99.99%) in a complex, distributed environment for financial services

## Why Affirm?
- Passionate about payments domain — as I've worked on payment transaction engine at PayPal along with PPWC (working capital). 
	- Expertise in payment provider integrations — banks and providers. 
	- Expertise in distributed payment systems with order management, payment ledger, wallet management and payment disputes.
- 

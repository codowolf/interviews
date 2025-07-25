***Role*** — Staff Engineer for Claims & Accidents
***Team*** — Claims & Accidents 
***Team Goal*** — Build and maintain a platform to intake accident reporting through multiple channels, and manage the life cycle of claims by partnering with 3rd Party Insurance Companies. Provide tools for the internal claims ops team to handle the claims, enabling them to have most efficient workflows
***Org*** — Insurance & Risk
***Org Goal*** — Make Rides as safe as possible. 
***Context*** — When a Lyft driver gets into an accident, depending on the situation, Lyft is responsible to provide insurance. `coverage — 1M$ for 3rd party damages, state minimum for 1st party coverage`. Driver's personal insurance doesn't cover the cost related to the damages because it's for commercial use. Previously, Lyft was covering the costs of damage, but since a few years Lyft has been integrating with Insurance companies and lets Insurance companies handle it for us. This means Lyft is connecting TPA (Third Party Admin) to the parties involved in the accident, while providing all the necessary data related to the accidents. Our Claims Management System manages life cycle of a claim and also connects Lyft to several insurance companies across Canada and US.

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
- Provide platform for Claims Management System called RMIS (Risk Management Information System)
- Intake accident information through web and mobile by riders, drivers and 3rd party
- Allow advocates to manage claims life cycle — add tasks, notes, attachments, visualize accident telematics data, search claims data
- Integrate with Insurance companies for two way data exchange
- Tech stack — python flask services, K8s, Dynamodb, Elasticsearch, SQS, Hive, Kafka

**What are advocates doing?**
- FNOL ops — after an accident is reported through forms, act quickly to verify all the information necessary to mark it ready to send to TPA. This could also involve phone calls with involved parties to gather as much data as possible. They are supposed to act within SLA requirements to submit FNOL to our Insurance Partners
- Claims ops, strategists — work with adjusters to guide them on the best strategy, evaluate final settlements, provide feedback, review workflows, work with legal to handle lawsuits, strategize to improve at every opportunity to reduce the insurance cost

**Pain Points**
- Lot of workflows are heavily manual, leading to high AHT (average handle time of claim), leading to missing SLA of claims submissions
- Many workflows require reading through long documents like Injury reports, Medical reports, Police reports, Lawsuits that can be time consuming for comprehensive review for Claims Strategists
- Lack of visibility into severity of the accident as the claim progresses 

**what we have built so far?**
- backend platform for conversational AI
	- use stateless API provided by openai and claude
	- separate service to handle conversational LLM interaction
	- persist conversation history to create AI chatbot experience 
	- capability to switch models during conversation
	- provides foundational framework to handle next set of features
- UI for showing claims summaries including severity, legal severity, timelines, note summaries
- Chatbot 
	- Provides a chatbot interface to Q&A about claims
- damage estimator
	- uses accident photos to analyze damage severity through multi-modal LLM
	- uses accident photos and metadata to estimate damage repair cost ultimately helping with reserve estimation and severity
- document intelligence
	- a scalable document extraction framework to extract texts from scanned pdfs
	- handles large documents with complex layouts and extracts content using LLM multi-modal
	- summarizes document for advocates to quickly get all information
	- support chat with file
	- on track to build RAG pipeline for document Q&A

**Team Worked on this**
- Eng — Staff Eng (lead, me), 2 frontend engineers, 2 backend engineers (rotating as needed)
- Product — 1 product manager (from mid stage of project), 1 staff prod manager for any strategic discussions
- Design — design best UX, I provided a lot of feedback here
- Ops — 5 ops from different verticals to gather continuous feedback and inputs
- Leadership — Eng director / VP / Ops Director
- Other collaboration — 
	- Infra — ML platform, Infra (not much help from them other than libraries to talk to openai and aws)
	- Vendors — OpenAI
- End Users
	- Ops — end users (claims ops, fnol ops, legal ops, legal team) about 250-300



**Detailed timeline of the project**
- I was tasked with a green field mandate of leading GenAI roadmap
	- Why? — because i was proactively learning AI's capabilities as LLM's were being realized. I thought of several use cases that could potentially reduce some of the manual workflows we had and constantly implemented proof of concept for small features. Looking at my interest, and the industry evolution around AI, they tasked me to lead it.  
- It was greenfield and no clear path goals defined, so I had to come up with any ideas possible and work with leadership. No resource allocation at the beginning of the project. It started off with just me ideating and working on setting up a vision. Implementing PoC for small features were good, but I had to come up with a vision and strategy to have a clear road map defined, and how it would align with our mission to reduce claims handling time and improve workflow efficiency of our Ops team. The architecture should be something scalable beyond basic functionality and should fit the long term narrative of automating multiple workflows using LLMs. After several surveys and shadow sessions with our Ops, it was clear that one of the biggest pain points that could potentially be solved was around handling large documents. But I thought, to get there, we can't just build adhoc solutions, it should fit into existing platform of claims management and also built around foundational capabilites of conversational experience. One of the challenging aspect of integrating was that I couldn't use stateful APIs the AI vendors provided, due to data privacy concerns. And using stateless API means I should have state machine for conversation history. Hence, I decided that in order to have a foundation, we need to build a chat framework with chatbot as a UX for our ops to get themselves familiar with AI interactions. With that in mind, the first product would be ChatBot, and then Document Intelligence built on top of it.
- ChatBot
	- Infra — python service, dynamodb, openai stateless API, conversation branching, dynamically select any GPT model for each request. 
	- Functionality — Add data objects as resources, and create and execute a prompt against the resources. 
	- Prompt Engineering — Several iterations of prompt were tested against different scenarios and prompts were improved accordingly. THere's also a feedback loop that allowed prompt optimizations even further
	- Result — Ops were able to get key insights about the claim to get them upto speed, by giving them clearly defined summary of the claim, it's current state, the timeline and summary of the notes. This was loved by our ops team and set as an example for other teams at Lyft. The ops were able to get the hang of using AI in their day to day workflows, leading to significant time savings. 
	- what did we improve as we launched? What were the pain points after launch? 
		- Collect detailed usage metrics on clicks, time spent and feedback around what worked, and what didn't. It was stateless from UX perspective, meaning refreshing page would erase summaries and other data. Prompt were fine tuned based on user feedback to include / exclude more info. Metadata added for prompts so that LLM could have better context on internal Acronyms. Responses were enhanced to include references to the data used to response, especially Q&A. 
- Second milestone of document intelligence — a scalable document extraction, summarization and conversational framework around documents. Challenge was large files(100s of pages), scanned docs, complex layouts. Vendor API's didn't support stateless API for this use case, so we had to build our own. Choice between AWS Textract and LLM took quite a bit of investigation. Run through 100s of different documents of different complexities. Couple of factors that allowed us to choose hybrid approach was that LLM's good with bad orientation, multi lingual, multi column docs and textract was good with complex layouts with forms, however both had inaccuracies in extreme complex cases. Further challenges included that large pdfs broken down to chunks, CPU bound image pre-processing, parallel extraction and retry mechnism for failures and finally aggregating extracted chunks into a single document within a given SLA (bound by LLM call). Extracted texts are further summarized and displayed to the users in less than 30s after uploading file regardless of the size
	- what did we improve as we launched? What were the pain points after launch?
		- After launch, 5% error rate on sensitive docs. Escalations didn't help, so we quickly integrated with Bedrock -> Claude models. Issue resolved
		- Leads to long context and known issue of accuracy challenges and higher latency — "needle in the haystack" benchmark (5-15% error rate is plausible)
		- Including multiple files would go out of context in some cases or as conversation grows
		- How we mitigated this? 
			- Using RAG, we are able to retrieve and pass relevant data. We do several optimization for retrieval by re-generating multiple queries using LLM from original query and then retrieve it, the retrieved data is then ranked again using LLM.
## Who am I and What I do?
 - I work for Insurance & Risk org — has 4 tech teams
	 - Pre-Accidents — road safety & telematics
	 - Post-Accidents — accidents & claims
- I am a Staff Engineer for the Claims & Accidents team, a total of 15 engineers. Our team's core mission is to build and maintain a platform for reporting accidents, managing the lifecycle of claims in partnership with third-party insurance companies, and providing tools to our internal claims operations team to manage the strategy with maximum efficiency.
	- Life cycle involves making strategic decisions that impacts final settlement amount for a claim, as we receive more and more information through various channels
	- Our claims ops make this happen with years of expertise and in collaboration with our insurance partners. 
	- Earlier claim closure the better, since it leads to settlement before it leads to Litigation which could then cost significantly if Lyft losses the battle.
- 50% of my time was for AI initiative, and rest was for over seeing other projects, helping with architecture decisions, approve tech specs and constant mentorship of engineers




#### [Exclude this from prompt]
**The main problem we are solving is the heavily manual nature of claims processing.** Many workflows involves reading through extensive documents like police reports, medical reports, lawsuits that leads to very high Average Handle Times (AHT) and frequently missing critical SLAs at different stages. This directly impacts our operational efficiency and, ultimately, Lyft's insurance premium costs.

**AI Initiative** — I was given a greenfield mandate to identify and lead our GenAI strategy There was no clear path or resources initially, so I was responsible for ideating, defining the vision, and setting the technical architecture for a scalable solutions that could enhance multiple complex workflows.

My work focused on three key areas:

1. **AI Chatbot Platform:** I spearheaded the development of a backend platform for conversational AI. Given data privacy, we used stateless APIs, so I designed the system to persist conversation history for a true chatbot experience. This allowed claims ops to quickly get key insights and summaries about any claim, especially useful for long-running cases, significantly reducing the time spent getting up to speed.
    
2. **Document Intelligence Pipeline:** This was a major initiative. Our challenge was extracting and summarizing information from large, complex, and often scanned PDF documents, which vendor APIs couldn't handle reliably in a stateless way. I led the development of our own scalable document extraction framework using a hybrid LLM and AWS Textract approach. This system processes hundreds of documents, handles issues like bad orientation and complex layouts, and then summarizes the content for advocates. We were also on track to build a RAG pipeline for advanced document Q&A, tackling complex chunking strategies and integrating with Elasticsearch. This directly tackled the pain point of time-consuming document review.
    
3. **Damage Estimator:** We also developed a damage estimator that leverages multi-modal LLMs to analyze accident photos and metadata to assess damage severity and estimate repair costs, which helps with reserve estimation and overall claim severity assessment.

**The impact of these initiatives was significant.** We directly addressed the high AHT and manual workflows, enabling our claims ops team to become much more efficient. By providing quick access to critical information and automating document processing, we reduced the time spent on each claim, improved SLA adherence, and ultimately contributed to better control over our insurance costs.
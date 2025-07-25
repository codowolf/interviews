# Rounds
**TPS**
- Implement 3 methods for a parking garage
	- `{python}  def park(vehicle_id)`
	- `{python} def unpark(vehicle_id)`
	- `{python} def get_vehicle(spot_id)`
		- Given a spot id, returns vehicle_id and level it's parked at
 
 **Coding 1**
	 - `Get next palindrome for a given integer`
 
 **System Design** 
	 - `Uber eats feed page — user just needs to see a list of near by restaurants`
		 - order by ratings
		 - order by new businesses
	 - Interviewer was too communicative — everything i mentioned was having a followup
	 - **HLD**
		 - Talked about geohashing
			 - range granularity
			 - indexing on : (geohash), (geohash, rating), (geohash, created_at)
		 - Use postgres 
			 - Asked Why? 
				 - geospatial capabilities on range based query on bounded box (say 5 mile)
				 - no joins needed, so any NoSQL with same capabilities are okay
		 - Handling load
			 - cache will store `geohash:search_type` (rating vs new_business)
			 - multiple users within the same geohash will reuse the query results
		 - 
	 - **Issues**
		 - Talked too much about Users + Address table until intervened to take live location
		 - Created Business and Locations table separately 
			 - Kept asking why separate table?
				 - Said logical separation from "business" metadata
				 - Interviewer pushed me to keep them in same table, so changed design
		 - When asked about how reads are handled at scale?
			 - Mentioned caching but not `Read Replicas`
			 - Said Cache would need geohash capabilities to mimic table's capabilites 
				 - This isn't true
				 - It's only needed in case of tracking real-time data like moving users / drivers / friends
		 - Didn't talk about what is the key value for redis data
			 - Instead said query -> results are cached
		 - Didn't get time to talk about how new businesses show up in search
			 - Gave one liner
		 - Didn't talk about DB sharding strategy
			 - Although in case of geospatial use cases, sharding isn't heavily needed

**Deep Dive**
- Seem to be impressed, no questions asked other than basic
- Called out running out of time
- [Presentation](https://app.excalidraw.com/s/3egtamAtXkF/8honhhOEFoC)
### Practice
#### Alien Dictionary
```python
def alienOrder(self, words: List[str]) -> str:
	graph = defaultdict(set)
	indeg = {c: 0 for w in words for c in w}
	for i, w1 in enumerate(words[:-1]):
		w2 = words[i + 1]
		w1_has_full_prefix_match = True
		for c1, c2 in zip(w1, w2):
			if c1 == c2: continue
			if c2 not in graph[c1]:
				indeg[c2] += 1
			graph[c1].add(c2)
			w1_has_full_prefix_match = False
			break
		if w1_has_full_prefix_match and len(w1) > len(w2):
			# case when "abc" followed by "ab"
			return ''
	res = []
	start = [c for c in indeg if not indeg[c]]
	deq = deque(start)
	while deq:
		c = deq.popleft()
		res.append(c)
		for nc in graph[c]:
			indeg[nc] -= 1
			if not indeg[nc]:
				deq.append(nc)
	if any(filter(lambda x: indeg[x] != 0, indeg.keys())):
		return ''
	return ''.join(res)
```

#### Find Robots

```
/*
Given two inputs,

First input is the location map, a 2D array

| O | E | E | E | X | 
| E | O | X | X | X |
| E | E | E | E | E |
| X | E | O | E | E |
| X | E | X | E | X | 

O = Robot, E = Empty, X = Blocker

Alternative inputs: 

For Java/C++: {{'O','E','E','E','X'},{'E','O','X','X','X'},{'E','E','E','E','E'},{'X','E','O','E','E'},{'X','E','X','E','X'}} 


Second input is the query. It’s a 1D array consisting of distance to the closest blocker in the order from left, top, bottom and right

[2, 2, 4, 1] -> This means distance of 2 to the left closest blocker, 2 to the top closest blocker, 4 to the bottom closest blocker and 1 to the right closest blocker

Note: The location map boundary is also considered blocker, meaning if the robot hits the boundary it also means it’s hitting the blocker.

Write a function that takes these two inputs and returns the index of the robots (if any) that matches the query that we’re looking for.

Solution for the example above would be the robot located at index [1, 1]


| O | E | E | E | X | 
| E |*O*| X | X | X |
| E | E | E | E | E |
| X | E | O | E | E |
| X | E | X | E | X | 

*/
```

##### LLM Solution
```python
def find_matching_robots(location_map, query):
    rows = len(location_map)
    cols = len(location_map[0])
    
    # Initialize distance arrays
    left = [[0] * cols for _ in range(rows)]
    right = [[0] * cols for _ in range(rows)]
    top = [[0] * cols for _ in range(rows)]
    bottom = [[0] * cols for _ in range(rows)]
    
    # Calculate distances from left and top
    for i in range(rows):
        for j in range(cols):
            if location_map[i][j] == 'X':
                left[i][j] = 0
                top[i][j] = 0
            else:
                left[i][j] = left[i][j-1] + 1 if j > 0 else 1
                top[i][j] = top[i-1][j] + 1 if i > 0 else 1
    
    # Calculate distances from right and bottom
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            if location_map[i][j] == 'X':
                right[i][j] = 0
                bottom[i][j] = 0
            else:
                right[i][j] = right[i][j+1] + 1 if j < cols-1 else 1
                bottom[i][j] = bottom[i+1][j] + 1 if i < rows-1 else 1
    
    # Find matching robots
    matching_robots = []
    for i in range(rows):
        for j in range(cols):
            if location_map[i][j] == 'O':
                distances = [left[i][j], top[i][j], bottom[i][j], right[i][j]]
                if distances == query:
                    matching_robots.append([i, j])
    
    return matching_robots

# Test with the example
location_map = [
    ['O', 'E', 'E', 'E', 'X'],
    ['E', 'O', 'X', 'X', 'X'],
    ['E', 'E', 'E', 'E', 'E'],
    ['X', 'E', 'O', 'E', 'E'],
    ['X', 'E', 'X', 'E', 'X']
]
query = [2, 2, 4, 1]

result = find_matching_robots(location_map, query)
print(result)  # Should output [[1, 1]]
```


#### Shortest Path
```
/*
You a given a graph, that has nodes which are word in oxford dictionary and two nodes are directly connected if one word can be generated by other by just replacing a char (like CAT and COT). In such a graph, find the shortest path between two given words.

Dict = {CAT, COT, TOT, POT, POP, MOP, MAP}

input: CAT, COT
output: [CAT, COT]


input: CAT, MAP
output: [CAT, COT, POT, POP, MOP, MAP]


*/
```

#### Leadership Practice

##### Interview 3: Collaboration & Leadership (60 min)
This interview evaluates your ability to build and sustain trusting, collaborative, and strategic relationships within and across teams or organizations, while working with integrity.

**Scope & impact expectation:**
- Directly responsible for one or more cross-team projects from inception to production readiness.

**How to prepare:**
- **Reflect on past projects:** Identify key examples you want to share. Use the STAR format (Situation-Task-Action-Results) to structure your answers. Avoid hypothetical situations or lacking depth in your responses.

**Be ready to discuss topics like:**
- Your ability to work with determination and urgency.
- Collaboration within and across teams.
- Handling conflicts and leading projects end-to-end.
- Stakeholder management (e.g., working with Product, Data, or Design).
- Task prioritization and building trusting relationships.
- Examples of mentoring others and providing or receiving feedback.

###### Answers
###### **Collaboration and Leadership**
1. Describe a complex, cross-functional project you led from inception to production readiness. What was the situation, what was your specific role, what actions did you take to ensure alignment and progress across the different teams (e.g., Product, Data, Design), and what were the results?
	1. **who** — insurance & risk — post accident claims management
	2. **users** — claims ops, legal, insurance partners, claimaints (riders/drivers/3rd party)
	3. **what** — Claims Management = reporting, reserve estimation, mileage calculation, lawsuit, settlement, partner integrations
	4. **goal** — **Minimize Loss** =  **Early Claim Closure** + **Efficient Strategy** 
		1. **Closure** — Fast/Accurate/Reliable reporting, Early/Accurate reserve estimation, Claims Severity Rating
		2. **Strategy** — Claim Handling, Settlement Evaluation and Negotiation, Insurance Partnerships 
	5. **pain-points** — delayed claims severity rating, delayed reserve estimation, slow settlement
	6. **role** — Lead AI strategy from ideation, vision, strategy, technical road map and execution
	7. **actions** 
		1. **Ideation** — explore AI capabilities, survey for pain-points, proof of concepts to get ops-buy-in
		2. **Vision** — Provide AI tools to **Improve Claims Closure**
		3. **Strategy** — ChatBot >> Document Intelligence >> Agents
		4. **Execution** — clear milestones and expectations, road map, feedback loop, foundation ➙ incremental work
2. Tell me about a time you had to build a strong, collaborative relationship with a team or stakeholder who had different priorities or a conflicting perspective. How did you build trust and find common ground?
	1. **S** — No PM, Staff PM didn't have full context. Was not onboard (not in favor of AI, not many use cases)
	2. **T** — Lead initiative with full transparency and get buy-ins
	3. **A** — **data driven approach** show AI capabilities, provide PoCs, show the surveys, support from other leaders, start small
	4. **R** — convinced both leadership, and PM to the point that we got a dedicated PM

3. Conflict is inevitable in cross-functional projects. Describe a situation where a significant conflict arose between team members or stakeholders. What was your approach to resolving it, and what was the outcome?
	1. **S** — complex business logic added into a service which lead to hard dependency of routing logic — slow, error prone
	2. **T** — Took the lead to solve the issue
	3. **A** — warned ➙took ownership, provide solution, agree mid-way, short/long solution, lead to async solution
	4. **R** — short solution done, mitigated | Long solution, EM working with other EMs

###### **Stakeholder Management and Influence**

4.  Can you provide an example of a time you had to influence stakeholders without having direct authority over them? How did you align them with your project's goals and what was the result?
	1. Legal Integration [Fox Trax] build solutions for us the way we want.

5.  Describe a situation where you had to manage competing priorities from different stakeholders. How did you prioritize tasks and communicate your decisions to ensure everyone remained aligned and committed?
	1. Legal Integration | Ops Pain Points  

 **Determination, Urgency, and Problem-Solving**

6.  Tell me about a time you faced a significant setback or unexpected obstacle in a project. How did you maintain a sense of urgency and determination to get the project back on track?
	1. Legal Integration — attrition delays
	2. Content Moderation

7.  Describe a situation where you had to make a critical decision with incomplete information. What was your process, who did you consult, and what was the outcome?
	1. Choice between OCR vs LLM
	2. Partner Evaluation X vs. Y

 **Mentorship and Feedback**

8.  Share an experience where you mentored a colleague. What was the context, what specific actions did you take to support their growth, and what was the impact of your mentorship?

9.  Tell me about a time you received difficult feedback. How did you process it, what actions did you take as a result, and how did it impact your work or professional development?

10. Can you give an example of a time you had to provide constructive feedback to a team member or a peer? How did you approach the conversation to ensure it was productive and well-received?

##### Interview 6: Impact - Efficiency & Quality (60 min)
In this interview, we assess how you scale yourself and the organization by making others better, enhancing productivity, and raising the quality of what the organization produces. We evaluate how systems are built for long-term extensibility, how you have led efforts to leverage and improve existing solutions, and more.
    
**Coding languages to prepare:**
- N/A

**Scope & impact expectation:**
- Directly responsible for multiple projects from inception to production readiness.

**How to prepare:**
- **Reflect on specific examples** where you’ve scaled yourself and your organization (your manager’s sub-tree) by:
	- **Making others better:** Examples of mentoring, coaching, or improving team collaboration.
	- **Improving productivity:** Initiatives or strategies that increased efficiency for you or the team.
	- **Raising quality:** Efforts to enhance the quality of work produced by the team or organization.
- **Identify instances where you:**
	- Built or influenced systems designed for long-term extensibility.
	- Leveraged and improved existing solutions to create scalable and impactful outcomes. 

**During your interview:**
- **Showcase your impact:**
	- Share concrete examples of how you scaled your contributions and made a measurable difference for the organization.
	- Highlight how your efforts improved team performance, collaboration, and output quality.
- **Discuss long-term solutions:**
	- Explain how you built systems for extensibility and ensured solutions were sustainable and adaptable.
	- Provide examples of leveraging and enhancing existing systems for greater efficiency and scalability.
- **Communicate leadership:**
	- Highlight your role in leading efforts to raise team standards, enable growth, and create scalable processes.
	- Share how you mentored or influenced others to improve their skills and productivity.
- **Frame around organizational impact:** Tie your examples back to organizational priorities, showing how your actions positively affected your manager’s sub-tree and beyond.
- **Demonstrate a data-driven mindset:** Share how you establish goals for yourself or your team, considering the broader context and using data to validate your assumptions.
- **Highlight strategic leadership:** Be prepared to discuss your influence on organizational impact, long-term vision, and your ability to lead effectively across functions.
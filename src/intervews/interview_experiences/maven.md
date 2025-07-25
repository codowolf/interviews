- R1 — Project Round
	- Was asked background
	- Talked about leading LLM (no slides)
- R2 — Coding

```python
Given mxn grid of 
'x' — obstacle
'p' — patient (single)
'c' — clinics

there's only one patient, 
1. find nearest hospital 

Extension
— Trace the path of nearest hospital to patient
  - Essentially you have to keep hashmap of chain of previous node

Extension 
- There are multiple patients, and no obstacles. Find a spot in mxn which is the minimum sum distance to all patients
- HINT: Can be done in O(m x n)
- This required DP
- 
```

- R3 — Onsite — Leadership
	- Questions about breakdown monolith 
	- Questions about feedback I received 
- R4 — Onsite — Behavioral 
- R5 — Onsite — Coding
	- Currency Converter
		- Given chain of currency conversions, like [(USD, CAD, 1.5), (USD, JPY, 1.7), (MEX, JPY, 3.4)] and so on
		- Given a query, return conversion rate ex: [(JPY to CAD)]
- R6 — Onsite — Architecture
	- Telehealth Appointment Booking System
		- There are providers who can add their schedules
		- There are members who can search for schedules between time range and submit request
		- Upon submission, the doctors (providers) can accept or rejected the selected schedules
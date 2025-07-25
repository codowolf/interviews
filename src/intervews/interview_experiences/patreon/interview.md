**TPS**
- Employee Reporting — Org Chart
- Given an employee nested structure, implement a method `def find(employee)` which would give back the role, and "total" direct reports for that employee
- Followup implement `def add_direct_report_ic(manager, report_name)`
	- note that this would require computing direct report for everyone above the manager, so the structure would change to have parent node for each node
```python
class Employee:
	def __init__(name):
		self.name = name
		self.total_reports = 0
		self.reports = []

	@property
	def role(self):
		return 'Manager' if len(self.total_reports) else 'IC'

def create_org_chart(org_map):
	reports = []
	ceo = Employee(name=ceo, reports=reports, total_reports=0)
	def add_employees(manager, reports_map):
		for emp in reports_map[manager.name]:
			employee = Employee(name=emp)
			manager.reports.append(employee)
			add_employees(employee, reports_map[emp])
	add_employees(ceo, org_map)
	return ceo
# AND SO ON. I DON"T REMEMBER HOW I COMPUTED THE TOTAL

```

**Onsite** 
- out of way 
- learning experience
- ownership
- collaboration and comms
- systems prepared to scale | expansion 

Coding
- More real world based questions

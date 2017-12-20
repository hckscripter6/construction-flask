from models.projects import Project

project = Project.query.all()

for r in project:
	a = (r.tag, r.name)
	b = ", ".join(a)
	print(b)
		



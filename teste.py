from panoptes_client import Panoptes, Project, Subject, SubjectSet

Panoptes.connect(username='******', password='******')

project = Project(18892)
print(project.display_name)

project.save()


SubSet = SubjectSet()

SubSet.links.project = project
SubSet.display_name = 'Tutorial subject set'
SubSet.save()
project.reload()




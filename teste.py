from panoptes_client import Panoptes, Project, Subject, SubjectSet

Panoptes.connect(username='Vincas2539', password='Simagivi@123')

project = Project(18892)
print(project.display_name)

project.save()


SubSet = SubjectSet()
# s = Subject(106173)
SubSet.links.project = project
SubSet.display_name = 'Tutorial subject set'
# SubSet.add_location("C:/Users/alber/Desktop/GitHub/ZooniverseTest/Imagens/Logo Bluemind Só o B Preto.png")
SubSet.save()
project.reload()
print(project.links.SubSet)



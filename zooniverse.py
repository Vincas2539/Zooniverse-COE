from panoptes_client import Panoptes, Project, Subject, SubjectSet
import os

Panoptes.connect(username='******', password='******')

project = Project(18892)
print(project.display_name)


os.chdir("C:/Users/alber/Desktop/GitHub/ZooniverseTest/Imagens")
local_files = os.listdir()
qtd = 0
try:
    SubSet = SubjectSet()
    SubSet.links.project = project
    SubSet.display_name = 'Tutorial subject set'
    SubSet.save()

    with Subject.async_saves():
        for filename in local_files:
            if filename.endswith(".png" or ".jpg"):
                qtd += 1
                s = Subject()
                s.links.project = 18892
                s.add_location(filename)
                s.save()
                SubSet.add(s)
                SubSet.save()
                print("Uploaded ", qtd)

    print(SubSet.subjects)

except Exception as Erro:
    print("Error!")
    print(Erro)

finally:
    print("Finish")

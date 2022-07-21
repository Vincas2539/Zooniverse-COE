from panoptes_client import Panoptes, Project, Subject
import os

Panoptes.connect(username='Vincas2539', password='Simagivi@123')

project = Project(18892)
print(project.display_name)


os.chdir("C:/Users/alber/Desktop/GitHub/ZooniverseTest/Imagens")
local_files = os.listdir()
qtd = 0
try:

    with Subject.async_saves():
        for filename in local_files:
            if filename.endswith(".png" or ".jpg"):
                qtd += 1
                s = Subject()
                s.links.project = project
                s.add_location(filename)
                s.save()
                print("Uploaded ", qtd)

except:
    print("Error!")

finally:
    print("Finish")


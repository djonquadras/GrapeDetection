from roboflow import Roboflow
import os

#rf = Roboflow(api_key="pqWmEUd47vLlriKYHQXr")
#project = rf.workspace("grappes-detection").project("grapes-detection-g36ar")
#version = project.version(3)
#dataset = version.download("yolov5")




# Defina o caminho da pasta que deseja verificar
pasta = 'yolov5/runs/detect'

# Verifica se a pasta existe
if not os.path.exists(pasta):
    # Cria a pasta se ela não existir
    os.makedirs(pasta)
    print(f'Pasta {pasta} criada com sucesso!')
else:
    print(f'A pasta {pasta} já existe.')
    

pasta = 'yolov5/runs/train'

# Verifica se a pasta existe
if not os.path.exists(pasta):
    # Cria a pasta se ela não existir
    os.makedirs(pasta)
    print(f'Pasta {pasta} criada com sucesso!')
else:
    print(f'A pasta {pasta} já existe.')

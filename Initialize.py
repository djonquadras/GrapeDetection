from roboflow import Roboflow
from git import Repo
import shutil
import os
import re
import torch
from tqdm import tqdm 
import os
import shutil
import stat
import time


# Verificar CUDA
if(torch.cuda.is_available()):
    print("CUDA is working! :D")
    print("PyTorch version:", torch.__version__)
    print("TorchVision version:", torchvision.__version__)
    print(torch.cuda.device_count())
    print(torch.cuda.current_device())
    print(torch.cuda.get_device_name(0))
else:
    print("CUDA not working!")
    
    
############################################################################################
# Download Images
############################################################################################

rf = Roboflow(api_key="pqWmEUd47vLlriKYHQXr")
project = rf.workspace("grappes-detection").project("grapes-detection-g36ar")
version = project.version(3)
dataset = version.download("yolov5")


############################################################################################
# Update YAML file
############################################################################################

path = 'grapes-detection-3/data.yaml'

with open(path, 'r') as file:
    linhas = file.readlines()

newLines = []
for linha in linhas:
    if re.match(r'^test:', linha):
        newLines.append('test: ../grapes-detection-3/test/images\n')
    elif re.match(r'^train:', linha):
        newLines.append('train: ../grapes-detection-3/train/images\n')
    elif re.match(r'^val:', linha):
        newLines.append('val: ../grapes-detection-3/valid/images\n')
    else:
        newLines.append(linha)

with open(path, 'w') as file:
    file.writelines(newLines)

############################################################################################
# Clone yolov5
############################################################################################

repo_url = 'https://github.com/ultralytics/yolov5'
clone_path = 'yolov5'
version = "e8a30cf"

print("Cloning YOLOv5 repository...")
with tqdm(total=100, desc="Cloning YOLOv5") as pbar:
    Repo.clone_from(repo_url, clone_path)
    pbar.update(50)  
repo = Repo(clone_path)
#repo.git.checkout(version)
#time.sleep(10) 
repo.close()

pbar.update(50) 
print(f'Done!')

############################################################################################
# Cleaning Folders and Files
############################################################################################

# Lista dos arquivos e pastas a serem removidos
files_to_remove = [
    "yolov5/.dockerignore",
    "yolov5/.gitattributes",
    "yolov5/.gitignore",
    "yolov5/README.md",
    "yolov5/README.zh-CN.md",
    "yolov5/tutorial.ipynb"
]



def on_rm_error(func, path, exc_info):
    # Change the file to writable and try again.
    os.chmod(path, stat.S_IWRITE)
    func(path)

print("Cleaning up files...")
total_files = len(files_to_remove) + 1  # +1 para a pasta .github
with tqdm(total=total_files, desc="Cleaning files") as pbar:
    shutil.rmtree("yolov5/.github")
    shutil.rmtree("yolov5/.git", onerror=on_rm_error)
    pbar.update(1)
    
    for file_path in files_to_remove:
        if os.path.exists(file_path):
            os.remove(file_path)
        pbar.update(1)
print("Done!")

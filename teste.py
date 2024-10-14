import torch
import torchvision


print("PyTorch version:", torch.__version__)
print("TorchVision version:", torchvision.__version__)


# Verificar CUDA
if(torch.cuda.is_available()):
    print("CUDA is working! :D")
    print(torch.cuda.device_count())
    print(torch.cuda.current_device())
    print(torch.cuda.get_device_name(0))
else:
    print("CUDA not working!")
    
"""

import os
import shutil
import stat

def on_rm_error(func, path, exc_info):
    # Change the file to writable and try again.
    os.chmod(path, stat.S_IWRITE)
    func(path)

shutil.rmtree("yolov5/.git", onerror=on_rm_error)


import torchvision
print(torchvision.__version__)
"""
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print("installed:"+package)

modules = ['bs4','pandas','requests']
print("checking system requirements")

for m in modules:
    install(m)

import glob 
import os

os.chdir('/home/Axizeaus/Projects/codewars-exercises/python/')
print(os.getcwd())

python_files = glob.glob('*.py')
print(python_files)

all_python_files = glob.glob('**/*.py' ,recursive=True)
print(all_python_files)
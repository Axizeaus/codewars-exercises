import os
from datetime import datetime
# print(dir(os))
print(os.getcwd())
print(os.system('mkdir learnOSLib'))
# os.chdir("/home/Axizeaus")
print(os.getcwd())
print(os.listdir())

try:
    os.mkdir('mkdir')
except FileExistsError:
    os.rmdir('mkdir')
    os.mkdir('mkdir')
    
print(os.listdir())

try:
    os.makedirs('folder/subfolder')
except:
    os.rmdir('folder/subfolder')
    os.makedirs('folder/subfolder')


print(os.listdir())
try:
    os.rmdir('folder/')
except:
    os.removedirs('folder/subfolder')
    
print(os.listdir())
    
os.rename('mkdir/','rename/')
try:
    os.rename('test.txt', 'demo.txt')
    print(os.listdir())
except FileNotFoundError:
    os.rename('demo.txt', 'test.txt')
    os.rename('test.txt', 'demo.txt')
    print(os.listdir())
    
print(os.stat('demo.txt'))
last_mod_time = os.stat('demo.txt').st_mtime
print(last_mod_time)
print(datetime.fromtimestamp(last_mod_time))

print(os.getcwd())
    
os.chdir('/home/Axizeaus/Projects/codewars-exercises/python/')
print(os.getcwd())
homeDir = str(os.environ.get('HOME'))
os.chdir(homeDir)
file_path = os.path.join(homeDir, 'test.txt')
print(os.getcwd())
print(file_path)

# with open(file_path, 'w') as f:
#     f.write("This is done from a python script")
    
# os.system('open test.txt')

# for dirpath, dirname, filename in os.walk(os.getcwd()):
#     print('current dir:', dirpath)
#     print('dirname:', dirname)
#     print('filename:', filename)

os.chdir('/home/Axizeaus/Projects/codewars-exercises/python/briefTourLib')
print(os.getcwd())

print(os.path.basename(os.getcwd()))
print(os.path.dirname(os.getcwd()))
print(os.path.split(os.getcwd()))

print(os.path.exists(os.getcwd()))
print(os.path.exists('/home/Axizeaus/Nothing'))

print(os.path.isdir(os.getcwd()))
print(os.path.isfile(os.getcwd() + '/osTest.py'))

print(os.path.splitext(os.getcwd() + '/osTest.py'))
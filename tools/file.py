import os
import shutil

path = __file__

if os.path.exists(path):
    print('I exist!')

    if os.path.isfile(path):
        print('I am a big PY!')
else:
    print('File missing')

#Read file
with open('test.txt') as file:
    print(file.read())

print(file.closed)

#Write to file
with open('test.txt', 'a') as file:
    file.write("This is new line!\n")

#There two other methods to copy files. Differs what it copies. Permissions metadata etc.
shutil.copyfile('test.txt', 'test2.txt')

#To move file
#os.replace(src, dst)

#Remove file
shutil.copyfile('test.txt', 'test3.txt')
os.remove('test3.txt')

#Remove folder
#os.rmdir(path)
#recursive
#shutil.rmtree(path)
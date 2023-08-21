import os

#create directory
os.mkdir('D:/demo')

#getting current working directory
print("stringformat",os.getcwd())
print("Byteformat",os.getcwdb())

#rename from current directory
os.rename("input.txt",'file1_new.txt')

#rename & moving to other directory
os.renames('file1.txt','D:/file1_new.txt')

#to change current directory
print("current directory",os.getcwd())
os.chdir('D:\demo')
print("changing directory",os.getcwd())

#to display list of files
print("files in current directory",os.listdir(os.getcwd()))
print("Directory contents are",os.listdir('D:/demo'))

#check directory
print(os.path.isdir('D:/demo'))

#size of directory
print(os.path.getsize('D:/demo'))

#remove directory
os.rmdir('D:/demo')
dir_list=os.listdir('D:/demo')
if len(dir_list)==0:
    print("directory is empty")

import os
current_dir=os.getcwd()# retrun the current working directory
print(current_dir)
#os.mkdir('A') # make directory in current working directory
#os.mkdir('A/kkkk') # make directory in directory
#os.makedirs('A/kkkk/kk') # make subdirectories
#os.chdir('A') # change directory
#print(os.getcwd())
#os.rename('A','B') # rename the directory
#os.mkdir("k")
#os.rmdir("k") # remove the diractory
#os.removedirs('B/kkkk/kk')# remove the subdrectory
content=os.walk('D:\python program\advanced python programs\kk', topdown=True,onerror=None)
print(content)

import os
f=[]
namelist=[]
for path, subdirs, files in os.walk("D://EMODnet/"):
    print(subdirs, files)
    for name in files:
        f.append(os.path.join(path, name))
        namelist.append(name)



print(namelist)

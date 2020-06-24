import os,sys
os.chdir(sys.path[0])

d1=[1,2,3,4]
d2=(1,2,3,4)
re = map((lambda x: x**2),d1)
print(list(re))
re = map((lambda x: x**2),d2)
print(tuple(re))

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sys import argv
from glob import glob
import os
def filter_zero(file):
    f=open(file)
    name=file+"_1"
    r=open(name,"wt")

    header = 1
    for line in f.readlines():
        if header:
            header -= 1
            r.write(line)
        else:

            lineL = line.strip().split("\t")
            a = (float(lineL[1]), float(lineL[2]), float(lineL[3]))
            b = (float(lineL[4]), float(lineL[5]), float(lineL[6]))
            sub = 0

            if a.count(sub) < 2 and b.count(sub) < 2:
                r.write(line)
            elif a.count(sub) < 2 and b.count(sub) >= 2:
                r.write(line)
            elif a.count(sub) >= 2 and b.count(sub) < 2:
                r.write(line)

    f.close()
    r.close()
files=glob("*")
for i in files:
    filter_zero(i)
    os.remove(i)


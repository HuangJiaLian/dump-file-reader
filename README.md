# Dumpfile Reader
This project is to demonstrate one way to load lammps dump file in Python.

The lammps dump file used in this tool looks like this:
```
ITEM: TIMESTEP
1050000
ITEM: NUMBER OF ATOMS
22700
ITEM: BOX BOUNDS pp pp pp
4.4675109769620391e-01 2.9553248902304137e+01
4.4675109769620391e-01 2.9553248902304137e+01
4.4675109769620391e-01 2.9553248902304137e+01
ITEM: ATOMS id type x y z 
21683 2 0.903047 2.28129 27.7373 
3536 1 1.89004 1.48948 27.4408 
3538 1 1.85866 29.3911 28.2316 
3539 1 2.37414 1.06213 28.2208 
...
```

## Features
- [x] Can read lammps dump file
- [x] Can choose the specific type of atoms 
- [x] Can get the xyz coordinate easily 

## Useage 
```python
from dump_reader import *

# file_path: replace with your own
file_path = './data/dump.2all.lammpstrj'

# The line number before the first xyz coordinates,
# which equals to the line number  counting to the first line of 
# 'ITEM: ATOMS id type x y z ' in my case.
extra_line_num = 9

# Get all the dump list  
dump_list= read_dumps(file_path=file_path, extra_line_num=9)

# Show the first dump
print(dump_list[0].time_step)
print(dump_list[0].xyz_df)

# Select all the atoms of type 2
print(dump_list[0].get_xyz_type(2))

# Get specific part of dataframe 
# Example: The xyz coordinates of all the atoms of type 2 at the last dump 
xyz = dump_list[-1].get_xyz_type(2)
xyz = xyz.loc[:,2:]
print(xyz)
```
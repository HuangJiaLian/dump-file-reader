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


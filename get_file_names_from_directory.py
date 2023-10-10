# this code is to get the file name from a folder/directory and print to users

import os

# in windows OS use \\ double slash to scape a \ slash
path = 'C:\\Users\\Cetim\\Downloads\\youtube'

files = os.listdir(path)

for f in files:
	print(f)
import glob
import os
import time

def get_file_list(dirname, fileext):
    file_list = []
# Get list of all files only in the given directory
    list_of_files = filter( os.path.isfile,
                            glob.glob(dirname + fileext) )
# Sort list of files based on last modification time in ascending order
    list_of_files = sorted( list_of_files,
                            key = os.path.getmtime,
                            reverse=True)
# Iterate over sorted list of files and print file path
# along with last modification time of file
    for file_path in list_of_files:
        timestamp_str = time.strftime('%m/%d/%Y %H:%M:%S',
                                      time.gmtime(os.path.getmtime(file_path)))
        file_list.append(file_path + '@' + timestamp_str)
    return file_list


# main

dir_name = 'E:/Downloads/'
file_ext = '*.zip'

init_file_list = get_file_list(dir_name,file_ext)

check_file_list = get_file_list(dir_name,file_ext)
for check_file in check_file_list:
    if not (check_file in init_file_list):
#        copy_file_list.append(check_file)


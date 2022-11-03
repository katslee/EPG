import glob
import os
import time
import functools

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

#folder_prefix = '/Users/Kats/Downloads/EPG'
folder_prefix = 'E:/Downloads/'
file_ext = '*.txt'
init_file_list = []
copy_file_list = []
task_list = [['/EPGSync/task1A_input1/','/EPGSync/task1A_output1/','/EPGSync/task1A_output2/','/EPGSync/task1A_output3/','/EPGSync/task1A_output4'],
             ['/EPGSync/task1B_input1/','/EPGSync/task1B_output1/','/EPGSync/task1B_output2/','/EPGSync/task1B_output3/','/EPGSync/task1B_output4'],
             ['/EPGSync/task1C_input1/','/EPGSync/task1C_output1/','/EPGSync/task1C_output2/','/EPGSync/task1C_output3/','/EPGSync/task1C_output4'],
             ['/EPGSync/task1D_input1/','/EPGSync/task1D_output1/','/EPGSync/task1D_output2/','/EPGSync/task1D_output3/','/EPGSync/task1D_output4'],
             ['/EPGSync/task2A_input1/','/EPGSync/task2A_output1/'],
             ['/EPGSync/task2B_input1/','/EPGSync/task2B_output1/'],
             ['/EPGSync/task3_input1/','/EPGSync/task3_output1/']]

#init_file_list = get_file_list(dir_name,file_ext)

#check_file_list = get_file_list(dir_name,file_ext)
#for check_file in check_file_list:
#    if not (check_file in init_file_list):
#        copy_file_list.append(check_file)

# Get init file list for task input folder
for task in task_list:
    folder_in = task[0]
    init_file_list.append(get_file_list(folder_prefix + folder_in, file_ext))

for ii in range(100):
    for task in task_list:
        check_file_list = get_file_list(folder_prefix + task[0], file_ext)
        i = task_list.index(task)
        new_files = [x for x in check_file_list + init_file_list[i] if x not in check_file_list or x not in init_file_list[i]]
        if new_files != []:
            for new_file in new_files:
                copy_file_list.append([task, new_file[:new_file.find('@')]])
        if len(copy_file_list) > 0:
            print(copy_file_list)
        time.sleep(5)

print("Done")
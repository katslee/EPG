import glob
import os
import time
import shutil
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

def copy_file():
    global copy_file_list
    global task_list
    global current_file_list
    global folder_prefix

    for cp_file in copy_file_list:
        cp_len = len(cp_file) - 1
        cp_filename = cp_file[cp_len]
        source = folder_prefix + cp_file[0][0] + cp_filename
        print(source)
        copy_fail = False
        for i in range(len(cp_file[0]) - 1) :
            target = folder_prefix + cp_file[0][i + 1]
            print(target)
            try:
                shutil.copy2(source, target)
            except:
                print("Fail to copy file " + source + " to " + target)
                copy_fail = True
        if not copy_fail:
            copy_file_list.remove(cp_file)
        index = task_list.index(cp_file[0])
        timestamp_str = time.strftime('%m/%d/%Y %H:%M:%S',
                                      time.gmtime(os.path.getmtime(folder_prefix + cp_file[0][1] + cp_file[1])))
        append = folder_prefix + cp_file[0][1] + cp_file[1] + '@' + timestamp_str
        current_file_list[index].append(folder_prefix + cp_file[0][0] + cp_file[1] + '@' + timestamp_str) # append should include timestamp, find it

# main

folder_prefix = '/Users/Kats/Downloads/EPG'
#folder_prefix = 'E:/Downloads/'
file_ext = '*.txt'
current_file_list = []
copy_file_list = []
del_file_list = []
task_list = [['/EPGSync/task1A_input1/','/EPGSync/task1A_output1/','/EPGSync/task1A_output2/','/EPGSync/task1A_output3/','/EPGSync/task1A_output4/'],
             ['/EPGSync/task1B_input1/','/EPGSync/task1B_output1/','/EPGSync/task1B_output2/','/EPGSync/task1B_output3/','/EPGSync/task1B_output4/'],
             ['/EPGSync/task1C_input1/','/EPGSync/task1C_output1/','/EPGSync/task1C_output2/','/EPGSync/task1C_output3/','/EPGSync/task1C_output4/'],
             ['/EPGSync/task1D_input1/','/EPGSync/task1D_output1/','/EPGSync/task1D_output2/','/EPGSync/task1D_output3/','/EPGSync/task1D_output4/'],
             ['/EPGSync/task2A_input1/','/EPGSync/task2A_output1/'],
             ['/EPGSync/task2B_input1/','/EPGSync/task2B_output1/'],
             ['/EPGSync/task3_input1/','/EPGSync/task3_output1/']]

# Get init file list for task input folder
for task in task_list:
    folder_in = task[0]
    current_file_list.append(get_file_list(folder_prefix + folder_in, file_ext))

for ii in range(1000):
    for task in task_list:
        checking_folder = folder_prefix + task[0]
        check_file_list = get_file_list(folder_prefix + task[0], file_ext)
        i = task_list.index(task)

#        new_files = list(set(check_file_list).difference(current_file_list[i]))
        new_files = list(set(check_file_list) - set(current_file_list[i]))
        new_files_len = len(new_files)
        if len(new_files) > 0:
            for new_file in new_files:
                new_file = new_file[new_file.index(task[0]) + len(task[0]):new_file.find('@')]
                copy_file_list.append([task, new_file])

# Remove the current_file_list item for deleted files are found
        del_files = list(set(current_file_list[i]).difference(check_file_list))
        if del_files != []:
            for del_file in del_files:
                current_file_list[i].remove(del_file)

# Copy the new files to target task folders
    if len(copy_file_list) > 0:
        print("New files are found.")
        copy_file()

    time.sleep(1)

print("Done")
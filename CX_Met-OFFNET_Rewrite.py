import glob
import time
from os.path import exists
files_to_open = glob.glob("CX_Filtered.csv")

entry_data = {}

def File_Creator(log_data):
    start_time = time.clock()
    for all_files in log_data:
        with open(all_files, 'r') as read_file:
            with open('CX_Filtered_Offnet.csv', 'a+') as write_file:
                for netflow in read_file:
                    entry_data = netflow.split(',')
                    entry_data[6] = entry_data[6].strip('\n')
                    if (entry_data[6]) == 'No UTC Time':
                        pass
                    elif (int(entry_data[6])>=1410305349819) and (int(entry_data[6])<=1410334349819):
                        write_file.write(netflow)
                    else:
                        pass 
    print(time.clock() - start_time, "seconds")

File_Creator(files_to_open)
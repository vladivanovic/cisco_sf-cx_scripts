# /////////////////////////
#
# This script written by Vlad
# This script strips apart the Sourcefire log and uses RegEx to pull specific fields out and write these to a file
# On average, a 40GB file for one day takes awhile
#
# /////////////////////////

import time
import re
import threading

def File_Write(SF_Array1):
    with open('SF_Filtered.csv', 'a+') as SF_Filtered:
        SF_Filtered.writelines(",".join(SF_Array1) + "\n")

def IP_CX_Correlator(log_data):
    start_time = time.clock()
    with open(log_data, encoding='ISO-8859-1', mode='r+') as read_file:
        for sf_log in read_file:
            # An Array to putting all the Regex'd Items into before its printed to a File
            SF_Array = []
            # All the Regex's, pretty straightforward how its composed if you'd like to pull out a different value
            SF_TimeDate = re.search('(?P<SF_TimeDate>\w+\s\d+\s\d+\:\d+\:\d+)', sf_log)
            SF_Con = re.search('Connection Type:(?P<SF_Con>.+?)\,', sf_log)
            SF_Client = re.search('Client:(?P<SF_Client>.+?)\,', sf_log)
            SF_AppProt = re.search('Application Protocol:(?P<SF_AppProt>.+?)\,', sf_log)
            SF_WebApp = re.search('Web App:(?P<SF_WebApp>.+?)\,', sf_log)
            SF_IniBytes = re.search('Initiator Bytes:\s(?P<SF_IniBytes>\d+)\,', sf_log)
            SF_ResBytes = re.search('Responder Bytes:\s(?P<SF_ResBytes>\d+)', sf_log)
            SF_TheEnd = re.search('({TCP}|{UDP})\s(?P<SF_SrcIP>\d+\.\d+\.\d+\.\d+)\:(?P<SF_SrcPort>\d+)\s\-\>\s(?P<SF_DestIP>\d+\.\d+\.\d+\.\d+)\:(?P<SF_DestPort>\d+)', sf_log)
            # This area check if Regex found anything, if it didn't it replaces it with a null value we specify
            if SF_TimeDate:
                SF_Array.append(SF_TimeDate.group('SF_TimeDate'))
            else:
                SF_Array.append("No Time Date")    
            if SF_Con:
                SF_Array.append(SF_Con.group('SF_Con'))
            else:
                SF_Array.append("No Connection Type")
            if SF_Client:
                SF_Array.append(SF_Client.group('SF_Client'))
            else:
                SF_Array.append("No Client Type")
            if SF_AppProt:
                SF_Array.append(SF_AppProt.group('SF_AppProt'))
            else:
                SF_Array.append("No AppProt Type")
            if SF_WebApp:
                SF_Array.append(SF_WebApp.group('SF_WebApp'))
            else:
                SF_Array.append("No WebApp Type")
            if SF_IniBytes:
                SF_Array.append(SF_IniBytes.group('SF_IniBytes'))
            else:
                SF_Array.append("No Res Bytes") 
            if SF_ResBytes:
                SF_Array.append(SF_ResBytes.group('SF_ResBytes'))
            else:
                SF_Array.append("No Res Bytes")     
            if SF_TheEnd:
                SF_Array.append(SF_TheEnd.group('SF_SrcIP'))
                SF_Array.append(SF_TheEnd.group('SF_SrcPort'))
                SF_Array.append(SF_TheEnd.group('SF_DestIP'))
                SF_Array.append(SF_TheEnd.group('SF_DestPort'))
            else:
                SF_Array.append("No Info")          
            threading.Thread(target=File_Write, args=(SF_Array,)).start()
            
    print(time.clock() - start_time, "seconds")

# Make sure that you the correct filename here!!!
threading.Thread(target=IP_CX_Correlator, args=("sourcefire.log-20140814",)).start()

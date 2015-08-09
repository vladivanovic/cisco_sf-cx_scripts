# /////////////////////////
#
# This script written by Vlad
# This script strips apart the CX log and uses RegEx to pull specific fields out and write these to a file
# On average, a 40GB file takes about 6 hours to rewrite as its not the best process to do so but I'm a newb
#
# /////////////////////////

import time
import re
import threading

def File_Write(CX_Array1):
    with open('CX_Filtered_Test.csv', 'a+') as CX_Filtered:
        CX_Filtered.writelines(",".join(CX_Array1) + "\n")

def IP_CX_Correlator(log_data):
    start_time = time.clock()
    with open(log_data, encoding='utf-8', mode='r+') as read_file:
        for prsm_log in read_file:
            
            # An Array to putting all the Regex'd Items into before its printed to a File
            CX_Array = []
            
            # All the Regex's, pretty straightforward how its composed if you'd like to pull out a different value
            CX_Recieved = re.search('Flow_Bytes_Received=(?P<CX_Recieved>\".+?\")', prsm_log)
            CX_Dest = re.search('Flow_DstIp=(?P<CX_Dest>\"\d+\.\d+\.\d+\.\d+\")', prsm_log)
            CX_Src = re.search('Flow_SrcIp=(?P<CX_Src>\"\d+\.\d+\.\d+\.\d+\")', prsm_log)
            CX_App = re.search('Avc_App_Name=(?P<CX_App>\".+?\")', prsm_log)
            CX_AppType = re.search('Avc_App_Type=(?P<CX_AppType>\".+?\")', prsm_log)
            CX_UrlCat = re.search('Url_Category_Name=(?P<CX_UrlCat>\".+?\")', prsm_log)
            CX_GenTime = re.search('Ev_GenTime=(?P<CX_GenTime>\".+?\")', prsm_log)
            
            # This area check if Regex found anything, if it didn't it replaces it with a null value we specify
            if CX_Src:
                CX_Array.append((CX_Src.group('CX_Src')).strip('"'))
            else:
                CX_Array.append("No Source")
            if CX_Dest:
                CX_Array.append((CX_Dest.group('CX_Dest')).strip('"'))
            else:
                CX_Array.append("No Destination")
            if CX_Recieved:
                CX_Array.append((CX_Recieved.group('CX_Recieved')).strip('"'))
            else:
                CX_Array.append("No Bytes")
            if CX_App:
                CX_Array.append((CX_App.group('CX_App')).strip('"'))
            else:
                CX_Array.append("No App")
            if CX_AppType:
                CX_Array.append((CX_AppType.group('CX_AppType')).strip('"'))
            else:
                CX_Array.append("No App Type")
            if CX_UrlCat:
                CX_Array.append((CX_UrlCat.group('CX_UrlCat')).strip('"'))
            else:
                CX_Array.append("No URL Category")
            if CX_GenTime:
                CX_Array.append((CX_GenTime.group('CX_GenTime')).strip('"'))
            # This writes to the file, not in a proper csv format but it does the job
            with open('CX_Filtered.csv', 'a+') as CX_Filtered:
                CX_Filtered.writelines(",".join(CX_Array) + "\n")
            #threading.Thread(target=File_Write, args=(CX_Array,)).start()
    print(time.clock() - start_time, "seconds")

def CX_Byte_Count(log_data):
    start_time = time.clock()
    with open(log_data, encoding='utf-8', mode='r+') as read_file:
        total_bytes_recieved = 0
        total_bytes_sent = 0
        total_bytes = 0
        for prsm_log in read_file:
            # The Regex's            
            CX_Recieved = re.search('Flow_Bytes_Received=(?P<CX_Recieved>\".+?\")', prsm_log)
            CX_Sent = re.search('Flow_Bytes_Sent=(?P<CX_Sent>\".+?\")', prsm_log)
            CX_Total = re.search('Flow_Bytes=(?P<CX_Total>\".+?\")', prsm_log)
            # Adding to the variable
            if CX_Recieved:
                total_bytes_recieved = total_bytes_recieved + int((CX_Recieved.group('CX_Recieved')).strip('"'))
            else:
                pass
            if CX_Sent:
                total_bytes_sent = total_bytes_sent + int((CX_Sent.group('CX_Sent')).strip('"'))
            else:
                pass
            if CX_Total:
                total_bytes = total_bytes + int((CX_Total.group('CX_Total')).strip('"'))
            else:
                pass
    print(time.clock() - start_time, "seconds")
    # Printing the variable
    print((((total_bytes_recieved/1024)/1024)/1024) + " GB Downloaded")
    print((((total_bytes_sent/1024)/1024)/1024) + " GB Uploaded")
    print((((total_bytes/1024)/1024)/1024) + " GB Total")

# Make sure that you the correct filename here!!!
threading.Thread(target=IP_CX_Correlator, args=("prsm-cx-20140910",)).start()

CX_Byte_Count("prsm-cx-20140910")

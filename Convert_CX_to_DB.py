import time
import sqlite3

def Create_DB():
    con = sqlite3.connect('ip_lookup.db')
    # What I'm trying to accomplish
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE CX_Logs(ID INT, SrcIP TEXT, DestIP TEXT, Bytes TEXT, CX_App TEXT, CX_AppType TEXT, CX_WebCat TEXT, UTC TEXT);")

def Add_to_DB(src_ip, dest_ip, cx_bytes, cx_app, cx_apptype, cx_webcat, utc):
    con = sqlite3.connect('ip_lookup.db')
    # What I'm trying to accomplish
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO CX_Logs(SrcIP) VALUES('%s');" % src_ip)
        cur.execute("INSERT INTO CX_Logs(DestIP) VALUES('%s');" % dest_ip)
        cur.execute("INSERT INTO CX_Logs(Bytes) VALUES('%s');" % cx_bytes)
        cur.execute("INSERT INTO CX_Logs(CX_App) VALUES('%s');" % cx_app)
        cur.execute("INSERT INTO CX_Logs(CX_AppType) VALUES('%s');" % cx_apptype)
        cur.execute("INSERT INTO CX_Logs(CX_WebCat) VALUES('%s');" % cx_webcat)
        cur.execute("INSERT INTO CX_Logs(UTC) VALUES('%s');" % utc)        

entry_data = {}

def Database_Creator(log_data):
    start_time = time.clock()
    with open(log_data, 'r') as read_file:
        for netflow in read_file:
            entry_data = netflow.split(',')
            Add_to_DB(entry_data[0], entry_data[1], entry_data[2], entry_data[3], entry_data[4], entry_data[5], entry_data[6], entry_data[7])
    print(time.clock() - start_time, "seconds to push all CX Data to DB")

Create_DB() # Already Created

Database_Creator("CX_Filtered.csv")
# cisco_sf-cx_scripts
These are Python scripts I built for working with Syslog data from Cisco CX and Sourcefire devices.

These devices through no fault of their own output quite a lot of data in Syslog format (between 40-60GB of day for an organisation I worked at) which is great news but hard to parse so much data. This is where Splunk came in quite handy but limitations with the amount of logging I could input into the Splunk system I had access too meant that these big chunky files needing a lot of rewriting to compact into a format I could upload into Splunk but still obtain the data I needed.

SF_Rewrite.py is my attempt at rewriting SourceFire Syslogs, I then used regex to pull the following variables:
Time and Date, Connection Type, Client, Application Protocol, Web Application detected, Initiator Bytes, Responder Bytes, and then lastly, connection type UDP/TCP, source/destination ports and source/destination IP Addresses.


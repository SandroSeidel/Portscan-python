#coding:UTF-8

import socket
import sys 

<<<<<<< HEAD
#list off most used ports
default_ports = [21, 22, 80, 8080, 443, 53, 3306, 3389]

#check the argumments
if len(sys.argv) < 2: 
    print("""Usage: portscan.py [IP] [arguments]
             Arguments:
                -d set a default list of most used ports
                -p to set the ports """)    
    sys.exit(1)
if len(sys.argv) < 3:

    #set all the possible ports if the user did not especify it 
    ports = list(range(1, 65536))

for arg in sys.argv:

    if arg == '-d':
        #use the default list with de arg -d
        ports = default_ports
    
    if arg == '-p':
        a =1


for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        response = s.connect_ex((sys.argv[1], port ))
=======

if len(sys.argv) < 2: 
    print("Usage: portscan.py [IP] [ports - leave empty to listen to all ports]")    
    sys.exit(1)

default_ports = [21, 22, 80, 8080, 443, 53, 3306, 3389]

for port in default_ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)

    try:
        response = client.connect_ex((sys.argv[1], port ))
>>>>>>> 62b7c4100eb2bfbd430d1e71468b0283c35f24b1
        if response == 0:
            print("Port: ", str(port), "open")

    except:
        print("ERROR - Host not found")
        sys.exit(1)

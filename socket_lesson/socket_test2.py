import socket
import sys
import select

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("localhost", 5555))
data = my_socket.recv(1024)
print "recieved:\n%s" %data

running = True
while running:
    inputready, outputready, exceptready = select.select([my_socket, sys.stdin ], [], [])

    for s in inputready:
        if s == sys.stdin:
            # Do keyboard stuff
            keyboard = sys.stdin.readline()
            my_socket.sendall(keyboard)
        elif s == my_socket:
            # do socket stuff
            msg = s.recv(1024)
            print msg        
        else:
            print "Disconnected from server!"
            running = False


my_socket.close()
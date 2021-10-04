#!/usr/bin/env python
import socket

from variableDef import variableAssign, list

from expressions import doMath

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 100  #the max size of the command by the user

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    data1 = data.strip()
    if not data: break
    print ("received data:", data)
    if data1.lower() == 'author':
        conn.send('Oliver Fay\n')
    elif data1.lower() == 'hello':
        conn.send('world\n')
    elif data1.lower() == 'help':
        conn.send('This is my command line tool\nTo find out the author type: Author\nTo get a response type: Hello\nTo assign variables use the format <variableName> = <numericValue>\nTo perform mathmatical exprestions separate your numbers with +, -, *, /, **\n')
    elif data1.lower() == 'oliver':
        conn.send('you did it\n')
    elif not data1.find('=') == -1:
        conn.send(variableAssign(data1))
    elif data1.find('+') or data1.find('/') or data1.find('*') or data1.find('**') or data1.find('-'):
        conn.send(doMath(data1))
    for obj in list:
        print("test")
        if data1 == obj.name:
            conn.send(obj.value + "\n")
    #conn.send(data1 + '\n')  # echo
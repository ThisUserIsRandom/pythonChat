import socket
import threading
import time
users = []
communication = {}
IP = '127.0.0.1'
portListen = 4000
portSpeak = 4001
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
S = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
i = 0
def handleClientListen(conn,addr):
    print(f'{addr} joined')
    while True:
        global i
        msg = conn.recv(1024).decode('utf-8')
        convo = {i:f"{msg}"}
        communication.update(convo)
        i += 1
        if msg == '!Dis':
            print(f'connection Ended from{addr}!')
            break 
def listernerHandler(conn,addr):
    commKeys = []
    for x in list(communication):
        conn.sendall(f'{communication[x]}'.encode('utf-8'))
        commKeys.append(x)
        time.sleep(0.01)
    while True:
        if len(list((communication))) != len(commKeys):
            for x in list(communication):
                if x not in commKeys:
                    commKeys.append(x)
                    conn.sendall(f'{communication[x]}'.encode('utf-8'))
def ListenServer():
    print("[+] this server is going to listen things :")
    s.bind((IP,portListen))
    s.listen()
    print("[+] Now listening for connection")
    while True:
        conn,addr = s.accept()
        users.append(conn) 
        thread = threading.Thread(target=handleClientListen,args=(conn,addr))
        thread.start()
def SpeakServer():
    print("[+] this server is going to display communication:")
    S.bind((IP,portSpeak))
    S.listen()
    while True: 
        conn,addr = S.accept()
        thread = threading.Thread(target=listernerHandler,args=(conn,addr))
        thread.start()
threadOne = threading.Thread(target=ListenServer)
threadTwo = threading.Thread(target=SpeakServer)
threadOne.start()
threadTwo.start()

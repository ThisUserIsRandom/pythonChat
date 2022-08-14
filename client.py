import socket

IP = '0.tcp.in.ngrok.io'
portSpeak = 10104
portListen = 14384
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def main():
    userName = input("kimi no na wa?: ")
    s.connect((IP,portSpeak)) 
    print(f"connected to {IP}:{portSpeak}")
    connected = True
    while connected:
        msg = input(">")
        s.send(f'{userName}=>{msg}'.encode('utf-8'))
        if msg == '!disconnect' or msg =='!DISCONNECT':
            connected = False
def dataViewer():
    s.connect((IP,portListen))
    while True:
        msg = s.recv(1024).decode('utf-8')
        print(msg)
instanceTask = int(input('Enter 1 to Speak  , 2 for listen :'))
if instanceTask == 1:
    main()
else:
    dataViewer()
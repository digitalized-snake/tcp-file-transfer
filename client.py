import os
import socket
import tqdm
IP = socket.gethostbyname(socket.gethostname())
PORT = 65432
BUFFER_SIZE = 1024
ADDR = (IP, PORT)
FORMAT = 'utf-8'
FILELOCATION = input("Enter the location of the file: ")
FILESIZE = os.path.getsize(FILELOCATION)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(bytes(f'{FILELOCATION},{FILESIZE}', FORMAT))

print(client.recv(BUFFER_SIZE).decode(FORMAT))

bar = tqdm.tqdm(range(FILESIZE), f"Sending{FILELOCATION}", unit='B', unit_scale=True)

with open(FILELOCATION, 'rb') as f:
    while True:
        data = f.read(BUFFER_SIZE)
        if not data:
            break
        client.send(data)

        bar.update(len(data))

client.close()

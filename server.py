import socket
import tqdm

IP = socket.gethostbyname(socket.gethostname())
PORT = 65432
BUFFER_SIZE = 1024
ADDR = (IP, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print('Server is listening...')

conn, addr = server.accept()
print('Connected by', addr)

bdata = conn.recv(BUFFER_SIZE).decode(FORMAT)
data = str(bdata)
filelocation = data.split(',')[0]
filesize = data.split(',')[1]

conn.send("File data received".encode(FORMAT))

bar = tqdm.tqdm(range(int(filesize)), f'Receiving {filelocation}', unit='B', unit_scale=True)

with open("received_file", 'wb') as f:
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        f.write(data)
        bar.update(len(data))
conn.close()
server.close()

from flask import Flask
import socket
import sqlite3
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the As server'


def create_dns_record(data):
    print(data)
    conn = sqlite3.connect('dns.db')

    cur = conn.cursor()

    cur.execute("INSERT INTO dns (name, type, value, ttl) VALUES (?, ?, ?, ?)",
                (data['name'], 'A', data['value'], data['ttl'])
                )

    conn.commit()
    conn.close()

    record = query_dsn_record(data['name'], data['type'])
    
    return "DNS record created:\n========\n" + record + "\n========\n\n"

def query_dsn_record(name, type):
    conn = sqlite3.connect('dns.db')
    conn.row_factory = sqlite3.Row
    record = conn.execute('SELECT * FROM dns where name=? and type=? limit 1',(name, type)).fetchall()
    conn.close()

    if len(record) > 0:
        data = record[0]
        result = "TYPE="+data['type'] + "\r\nNAME="+data['name'] + "\r\nVALUE="+data['value']+"\r\nTTL="+str(data['ttl'])
    else:
        result = 'No record found'
    
    return result

def create_db():
    connection = sqlite3.connect('dns.db')

    with open('schema.sql') as f:
        connection.executescript(f.read())

def start_udp_server():
    # localIP     = "127.0.0.1"
    localIP     = "0.0.0.0"
    localPort   = 53533
    bufferSize  = 1024
    msgFromServer       = "Hello UDP Client"
    bytesToSend         = str.encode(msgFromServer)

    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))

    print("UDP server up and listening")

    # Listen for incoming datagrams
    while(True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]

        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        
        print(clientMsg)
        print(clientIP)
        data = json.loads(message)

        if data['action'] == 'dns_register':
            result = create_dns_record(data)
        elif data['action'] == 'dns_query':
            print("Querying dns")
            result = query_dsn_record(data['name'], data['type'])
        else:
            result = "No action to perform."
        print(result)

        # Sending a reply to client
        # UDPServerSocket.sendto(bytesToSend, address)
        UDPServerSocket.sendto(str.encode(result), address)


def main():
    create_db()
    start_udp_server()


if __name__ == '__main__':
    main()

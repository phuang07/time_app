from dataclasses import replace
from termios import VSTOP
from flask import Flask, request
import json
import socket
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the User server'

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    args = request.args
    for key in ['hostname', 'fs_port', 'number', 'as_ip', 'as_port']:
        if not key in args:    
            return "Missing parameter " + key, 400

    fs_ip = query_dns(args['hostname'], args['as_ip'], args['as_port'])

    if(fs_ip == ''):
        return "Can't find ip for " + args['hostname']
    else:
        print("fs ip:" + fs_ip)
        return calc_fibonacci(fs_ip, args['fs_port'], args['number'])


@app.route('/qry_host_ip', methods=['GET'])
def get_host_ip():
    args = request.args
    fs_ip = query_dns(args['hostname'], args['as_ip'], args['as_port'])

    return fs_ip, 200

def calc_fibonacci(fs_ip, fs_port, number):
    url = 'http://' + fs_ip + ':' + fs_port + '/fibonacci?number=' + number
    response = requests.get(url)
    return response.text



def query_dns(hostname, as_ip, as_port):
    udp_message = {
        'name': hostname,
        'type': 'A',
        'action': 'dns_query'
    }

    msgFromClient       = json.dumps(udp_message)
    bytesToSend         = str.encode(msgFromClient)
    serverAddressPort   = (as_ip, int(as_port))
    bufferSize          = 1024

    
    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    data_list = msgFromServer[0].decode().split('\r\n')

    if len(data_list) < 2:
        return ''
    else: 
        # Certainly this line can be improved by not hardcoding the position
        return data_list[2].replace('VALUE=', '')

app.run(host='0.0.0.0',
        port=8080,
        debug=False)

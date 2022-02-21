from flask import Flask, request
import socket
import json
app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the Fibonacci server'


@app.route('/register', methods=['PUT'])
def register():
    """ 
    Register with AS server 
    Example: curl -X PUT http://172.17.0.5:9090/register -d '{ "hostname": "fibonacci.com", "ip": "172.18.0.2", "as_ip": "10.9.10.2", "as_port": "30001"}' -H 'Content-Type: application/json' 
    """
    
    data = request.get_json()

    # Call to as server for registration
    msg = send_AS_registration_info(data)

    return msg.decode(), 200


@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    """ 
    Calculate a fibonacci number
    Example: curl -X GET http://172.17.0.5:9090/fibonacci?number=9 
    """
    number_input = request.args.get("number")    

    # check if the this is a number
    if not number_input.isdigit():
        return "Input not a number", 400
    
    number = int(number_input)
    # calculation
    if number < 0:
        return "Incorrect input", 400
    
    result = calc_fibonacci(number)
    
    return str(result), 200

def calc_fibonacci(number):
    if number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return calc_fibonacci(number - 1) + calc_fibonacci(number - 2)


def send_AS_registration_info(data):
    udp_message = {
        'type': 'A',
        'ttl': 10,
        'name': data['hostname'],
        'value': data['ip'],
        'action': 'dns_register'
    }

    msgFromClient       = json.dumps(udp_message)
    bytesToSend         = str.encode(msgFromClient)
    serverAddressPort   = (data['as_ip'], int(data['as_port']))
    bufferSize          = 1024

    

    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    msg = msgFromServer[0]

    print(msg)
    return msg


app.run(host='0.0.0.0',
        port=9090,
        debug=False)
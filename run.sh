#!/bin/bash

# source start_server.sh > /dev/null


# Register from Fibonacci Server
echo "Regeter Fibonacci Servers"
curl -X PUT http://172.17.0.5:9090/register -d '{ "hostname": "fibonacci.com", "ip": "172.17.0.5", "as_ip": "127.0.0.1", "as_port": "53533"}' -H 'Content-Type: application/json'
curl -X PUT http://172.17.0.5:9090/register -d '{ "hostname": "fibonacci2.com", "ip": "172.17.0.5", "as_ip": "127.0.0.1", "as_port": "53533"}' -H 'Content-Type: application/json'
curl -X PUT http://172.17.0.5:9090/register -d '{ "hostname": "fibonacci3.com", "ip": "172.17.0.5", "as_ip": "127.0.0.1", "as_port": "53533"}' -H 'Content-Type: application/json'

# User Server
echo "Get fibonacci number 9 from fibonacci.com"
# curl -X GET 'http://172.17.0.5:8080/qry_host_ip?hostname=fibonacci.com&fs_port=9090&as_ip=127.0.0.1&as_port=53533'
curl -X GET 'http://172.17.0.5:8080/fibonacci?hostname=fibonacci.com&fs_port=9090&as_ip=127.0.0.1&as_port=53533&number=9'

echo ""

echo "Get fibonacci number 6 from finboacci2.com"
# curl -X GET 'http://172.17.0.5:8080/qry_host_ip?hostname=fibonacci2.com&fs_port=9090&as_ip=127.0.0.1&as_port=53533'
curl -X GET 'http://172.17.0.5:8080/fibonacci?hostname=fibonacci2.com&fs_port=9090&as_ip=127.0.0.1&as_port=53533&number=6'
echo ""

echo "Get fibonacci number 4 from finboacci3.com"
# curl -X GET 'http://172.17.0.5:8080/qry_host_ip?hostname=fibonacci2.com&fs_port=9090&as_ip=127.0.0.1&as_port=53533'
curl -X GET 'http://172.17.0.5:8080/fibonacci?hostname=fibonacci3.com&fs_port=9090&as_ip=127.0.0.1&as_port=53533&number=4'
echo ""
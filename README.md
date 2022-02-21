## How to run the program

* Install python3
* Run `pip install -r requirements.txt`
* Start the server from the terminal

```
docker@4e4e47c08c57:/docs$ ./start_server.sh
Start user server
Start fibonacci server
Start authoritative server
docker@4e4e47c08c57:/docs$ nohup: appending output to 'nohup.out'
nohup: appending output to 'nohup.out'
nohup: appending output to 'nohup.out'
fs ip:172.17.0.5
172.17.0.5 - - [21/Feb/2022 03:57:35] "GET /fibonacci?hostname=fibonacci.com&fs_port=9090&as_ip=127.0.0.1&as_port=53533&number=9 HTTP/1.1" 200 -
fs ip:172.17.0.5
172.17.0.5 - - [21/Feb/2022 03:57:35] "GET /fibonacci?hostname=fibonacci2.com&fs_port=9090&as_ip=127.0.0.1&as_port=53533&number=6 HTTP/1.1" 200 -
fs ip:172.17.0.5
172.17.0.5 - - [21/Feb/2022 03:57:35] "GET /fibonacci?hostname=fibonacci3.com&fs_port=9090&as_ip=127.0.0.1&as_port=53533&number=4 HTTP/1.1" 200 -
fs ip:172.17.0.5
172.17.0.5 - - [21/Feb/2022 04:02:02] "GET /fibonacci?hostname=fibonacci.com&fs_port=9090&as_ip=127.0.0.1&as_port=53533&number=9 HTTP/1.1" 200 -
fs ip:172.17.0.5
172.17.0.5 - - [21/Feb/2022 04:02:02] "GET /fibonacci?hostname=fibonacci2.com&fs_port=9090&as_ip=127.0.0.1&as_port=53533&number=6 HTTP/1.1" 200 -
fs ip:172.17.0.5
172.17.0.5 - - [21/Feb/2022 04:02:02] "GET /fibonacci?hostname=fibonacci3.com&fs_port=9090&as_ip=127.0.0.1&as_port=53533&number=4 HTTP/1.1" 200 -

```

* Test the application by running the following script in a new terminal
```
./run.sh
DNS record created:
========
TYPE=A
NAME=fibonacci.com
VALUE=172.17.0.5
TTL=10
========

DNS record created:
========
TYPE=A
NAME=fibonacci2.com
VALUE=172.17.0.5
TTL=10
========

DNS record created:
========
TYPE=A
NAME=fibonacci3.com
VALUE=172.17.0.5
TTL=10
========

Get fibonacci number 9 from fibonacci.com
34
Get fibonacci number 6 from finboacci2.com
8
Get fibonacci number 4 from finboacci3.com
3
```
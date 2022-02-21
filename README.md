## How to run the program

```
docker-compose up

╭─rayhuang at mbp16 in ⌁/git_repos/data-comm (dns_app ✚6)
╰─λ docker-compose up                                                            fish-1 | 2 (02:05.714) < 10:43:28
Starting data-comm_user_server_1 ... done
Starting data-comm_fs_server_2_1 ... done
Starting fibonacci_server_3      ... done
Starting data-comm_as_server_1   ... done
Starting fibonacci_server_1      ... done
Attaching to data-comm_as_server_1, fibonacci_server_3, data-comm_fs_server_2_1, fibonacci_server_1, data-comm_user_server_1
fibonacci_server_3 |  * Running on all addresses.
fibonacci_server_3 |    WARNING: This is a development server. Do not use it in a production deployment.
fibonacci_server_3 |  * Running on http://173.20.1.13:9090/ (Press CTRL+C to quit)
fibonacci_server_3 |  * Serving Flask app 'fibonacci_server' (lazy loading)
fibonacci_server_3 |  * Environment: production
fibonacci_server_3 |    WARNING: This is a development server. Do not use it in a production deployment.
fibonacci_server_3 |    Use a production WSGI server instead.
fibonacci_server_3 |  * Debug mode: off
fibonacci_server_1 |  * Serving Flask app 'fibonacci_server' (lazy loading)
fibonacci_server_1 |  * Environment: production
fibonacci_server_1 |    WARNING: This is a development server. Do not use it in a production deployment.
fibonacci_server_1 |    Use a production WSGI server instead.
fibonacci_server_1 |  * Debug mode: off
fibonacci_server_1 |  * Running on all addresses.
fibonacci_server_1 |    WARNING: This is a development server. Do not use it in a production deployment.
fibonacci_server_1 |  * Running on http://173.20.1.11:9090/ (Press CTRL+C to quit)
fs_server_2_1  |  * Serving Flask app 'fibonacci_server' (lazy loading)
fs_server_2_1  |  * Environment: production
fs_server_2_1  |    WARNING: This is a development server. Do not use it in a production deployment.
fs_server_2_1  |    Use a production WSGI server instead.
fs_server_2_1  |  * Debug mode: off
fs_server_2_1  |  * Running on all addresses.
fs_server_2_1  |    WARNING: This is a development server. Do not use it in a production deployment.
fs_server_2_1  |  * Running on http://173.20.1.12:9090/ (Press CTRL+C to quit)
user_server_1  |  * Serving Flask app 'user_server' (lazy loading)
user_server_1  |  * Environment: production
user_server_1  |    WARNING: This is a development server. Do not use it in a production deployment.
user_server_1  |    Use a production WSGI server instead.
user_server_1  |  * Debug mode: off
user_server_1  |  * Running on all addresses.
user_server_1  |    WARNING: This is a development server. Do not use it in a production deployment.
user_server_1  |  * Running on http://173.20.1.10:8080/ (Press CTRL+C to quit)


```

Then run:

```
─rayhuang at mbp16 in ⌁/git_repos/data-comm (dns_app ✚5)
╰─λ ./run.sh                                                                                                                                                      
Regeter Fibonacci Servers
DNS record created:
========
TYPE=A
NAME=fibonacci.com
VALUE=173.20.1.11
TTL=10
========

DNS record created:
========
TYPE=A
NAME=fibonacci2.com
VALUE=173.20.1.12
TTL=10
========

DNS record created:
========
TYPE=A
NAME=fibonacci3.com
VALUE=173.20.1.13
TTL=10
========

Get fibonacci number 9 from fibonacci.com
34
Get fibonacci number 6 from finboacci2.com
34
Get fibonacci number 4 from finboacci3.com
8
```
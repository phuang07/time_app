#!/bin/bash

echo 'Start user server'
nohup python user_server.py &
echo 'Start fibonacci server'
nohup python fibonacci_server.py &
echo 'Start authoritative server'
nohup python authoritative_server.py &

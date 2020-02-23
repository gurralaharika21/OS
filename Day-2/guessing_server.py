'''
    Write a python server program that
        0. initialized a socket connection on localhost and port 10000
        1. accepts a connection from a  client
        2. receives a "Hi <name>" message from the client
        3. generates a random to_guessbers and keeps it a secret
        4. sends a message "READY" to the client
        5. waits for the client to send a guess
        6. checks if the to_guessber is
            6.1 equal to the secret then it should send a message "Correct! <name> took X attempts to guess the secret"
            6.2 send a message "HIGH" if the guess is greater than the secret
            6.3 send a message "LOW" if the guess is lower than the secrent
        7. closes the client connection and waits for the next one
'''
 

import socket
import sys
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',10003))
sock.listen()
to_guess = random.randint(1,100)
conn,addr = sock.accept()
print('connected to the client' , addr)
conn.recv(1024).decode()
conn.sendall(b'READY')
while True:
    guessed = int(conn.recv(1024).decode())
    if(guessed > to_guess):
        conn.sendall(b'HIGH')
    elif(guessed < to_guess):
        conn.sendall(b'LOW')
    elif(guessed == to_guess):        
        conn.sendall(b'Correct! ')
        break

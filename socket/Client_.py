#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket


# In[ ]:


client_socket = socket.socket()
port = 12345
client_socket.connect(('127.0.0.1',port))
#recieve connection message from server
msg = input("-> ")
while True:
    if msg == 'exit':
        break;
    else:
        client_socket.send(msg.encode())
    msg = input("-> ")
client_socket.close()


# In[ ]:





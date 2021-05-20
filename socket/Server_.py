#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket,select
port = 12345


# In[2]:


socket_list = []
users = {}
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('',port))
server_socket.listen(3)
socket_list.append(server_socket)


# In[ ]:


while True:
    ready_to_read,ready_to_write,in_error = select.select(socket_list,[],[],0)
    for sock in ready_to_read:
        if sock == server_socket:
            connect, addr = server_socket.accept()
            socket_list.append(connect)
            print("You are connected from:" + str(addr))
        else:
            try:
                data = sock.recv(1024).decode()
                if not data:
                    break
                print("from connected user: "+str(data))
            except:
                continue
server_socket.close()


# In[ ]:





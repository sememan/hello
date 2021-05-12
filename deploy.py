#from root

import os
import pexpect 
from pexpect import pxssh


server = {
    "host": "192.168.178.46",
    "user": "pi",
    "passw": "mYB3rryp1",
}


try:      

    hostname = server['host']
    username = server['user']
    password = server['passw']

    s = pxssh.pxssh()

    s.login (hostname, username, password)
    s.prompt() 
    print('\n # login:\n', str(s))
    print()


    s.sendline ('pwd')
    s.prompt() 
    print (s.before.decode())
    print()


    # s.sendline ('git pull origin master:deploy')    
    # s.prompt() 
    # print ('# git pull:\n', s.before.decode())
    # print()



#     s.sendline ('pip3 install -r /opt/binando-binalytics2/src/RESTapi/requirements.txt')
#     s.prompt() 
#     print ('# install requirements:\n', s.before.decode())
#     print()

# #    s.sendline ('sudo apt install -y python3-rtree')
# #    s.prompt() 
# #    print ('# install requirements:\n', s.before.decode())
# #    print()



# #    s.sendline ('cd /opt/binando-binalytics2/src/RESTapi/tasks && rm -R migrations')    
# #    s.prompt() 
# #    print ('# rm migrations:\n', s.before.decode())
# #    print()



#     s.sendline ('cd /opt/binando-binalytics2/src/RESTapi && ls -la')    
#     s.prompt() 
#     print ('# ls:\n', s.before.decode())
#     print()

#     s.sendline ('cd /opt/binando-binalytics2/src/RESTapi/config && ls -la')    
#     s.prompt() 
#     print ('# ls:\n', s.before.decode())
#     print()

#     s.sendline ('cd /opt/binando-binalytics2/src/RESTapi/app && ls -la')    
#     s.prompt() 
#     print ('# ls:\n', s.before.decode())
#     print()

#     s.sendline ('cd /opt/binando-binalytics2/src/RESTapi/apis && ls -la')    
#     s.prompt() 
#     print ('# ls:\n', s.before.decode())
#     print()

#     s.sendline ('cd /opt/binando-binalytics2/src/RESTapi/tasks && ls -la')    
#     s.prompt() 
#     print ('# ls:\n', s.before.decode())
#     print()



# #    s.sendline ('python3 /opt/binando-binalytics2/src/RESTapi/manage.py db init --directory /opt/binando-binalytics2/src/RESTapi/migrations')
# #    s.prompt()
# #    print ('# postgres init:\n', s.before.decode())
# #    print()

#     s.sendline ('python3 /opt/binando-binalytics2/src/RESTapi/manage.py db migrate')
#     s.prompt()
#     print ('# postgres migrate:\n', s.before.decode())
#     print()

#     s.sendline ('python3 /opt/binando-binalytics2/src/RESTapi/manage.py db upgrade')
#     s.prompt() 
#     print ('# postgres upgrade:\n', s.before.decode())
#     print()



#     s.sendline ('service flask restart')
#     s.prompt() 
    # print ('# app restart:\n', s.before.decode())
    # print()

    s.close()

except Exception as e:

    print ("*** Exception FAILURE.")
    print (str(e)) 

    filename = open('/var/log/deploy.log', "a")
    filename.write("*** Exception FAILURE.")
    filename.write(str(e))
    filename.close()


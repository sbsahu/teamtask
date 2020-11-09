import os 
import subprocess

print('\n\n\t\t\t!!!!!!    Now a package httpd is installing to creat webserver !!!!!!!')
os.system('sleep 5')
prvip = os.popen('hostname -i').read()
pubip = os.popen("curl http://checkip.amazonaws.com").read()


os.system('yum install httpd -y')
os.system('systemctl start httpd')
os.system('systemctl enable httpd')





print('\t\t\t\t!!!!!!!    Write somthing to see in your webpage for testing purpose only')
msg = input()
os.system("echo {} > /var/www/html/index.html".format(msg))

print("\t\t\t Are looking for (Public/Private) IP ?")
print('\t\t\t 1 for Public\n\t\t\t 2 for Private')
print("You may choose : Public (In case of AWS) and Private (other)")
ans = input()
if ans=='1':
    print('\t\t\t!!!!!!   Now the webserver configured sucsessfully you can check that by entering your IP address and here is your ip \033[1;32;40m %s' % pubip)
elif ans=='2':
    print('\t\t\t!!!!!!   Now the webserver configured sucsessfully you can check that by entering your IP address and here is your ip \033[1;32;40m %s' % prvip) 
else:
    print('\t\t\t\t!!!!!WRONG OPTION!!!!/nPlease try 1 or 2') 

import os


print("  \033[1;32;40m                                                                                                                           ")
print("     _         _                        _   _                ____             __ _                       _   _              ")
print("    / \  _   _| |_ ___  _ __ ___   __ _| |_(_) ___  _ __    / ___|___  _ __  / _(_) __ _ _   _ _ __ __ _| |_(_) ___  _ __   ")
print("   / _ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \  | |   / _ \| '_ \| |_| |/ _` | | | | '__/ _` | __| |/ _ \| '_ \  ")
print("  / ___ \ |_| | || (_) | | | | | | (_| | |_| | (_) | | | | | |__| (_) | | | |  _| | (_| | |_| | | | (_| | |_| | (_) | | | | ")
print(" /_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|  \____\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|\__|_|\___/|_| |_| ")
print("                                                                                   |___/                                    ")
print("\tChoose any one option   ||")
print("\t*********************   ||")
print("\t                        \/")
print('\t\t\t\tpress 1 to Show Date \n\t\t\t\tpress 2 to Show Calender')
print('\t\t\t\tpress 3 to Run Any Linux Command')
print('\t\t\t\tpress 4 to Configure WebServer')
print('\t\t\t\tpress 5 to Configure and Start NameNode')
print('\t\t\t\tpress 6 to Configure and Start DataNode')
print('\t\t\t\tpress 7 to do complete setup and install Docker and run container')
print('\t\t\t\t => ', end='')
cmd=input()

if cmd2=='1':
 os.system("sudo date")

 elif cmd2=='2':
 os.system('sudo cal')

 elif cmd2=='3':
 print('Enter Linux Command :- ' , end='')
 linux_cmd=input()
 os.system('sudo {}'.format(linux_cmd))

 elif cmd2=='4':
 os.system('yum install httpd -y')
 os.system('systemctl start httpd')
 os.system('systemctl enable httpd')
 os.system('cp index.html /var/www/html')

#os.system('echo \[Docker\] >> /etc/yum.repos.d/docker.repo')
#os.system('echo baseurl\=https://download.docker.com/linux/centos/7/x86_64/stable/ >> /etc/yum.repos.d/docker.repo')
#os.system('echo gpgcheck\=0 >> /etc/yum.repos.d/docker.repo')
                                                                   
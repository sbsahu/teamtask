import osi

os.system('echo \[Docker\] >> /etc/yum.repos.d/docker.repo')
os.system('echo baseurl\t\=\thttps://download.docker.com/linux/centos/7/x86_64/stable/Packages/ >> /etc/yum.repos.d/docker.repo')
os.system('echo gpgcheck\=0 >> /etc/yum.repos.d/docker.repo')





print("  \t\t\t____     ___     ___ __ __  ____ ____       ___   ___   __  __  ____ __   ___  __ __ ____   ___  ______ __   ___   __  __"
print("  \t\t\t|| \\   // \\   //   || // ||    || \\     //    // \\  ||\ || ||    ||  // \\ || || || \\ // \\ | || | ||  // \\  ||\ ||"
print("  \t\t\t||  )) ((   )) ((    ||<<  ||==  ||_//    ((    ((   )) ||\\|| ||==  || (( ___ || || ||_// ||=||   ||   || ((   )) ||\\||"
print("  \t\t\t||_//   \\_//   \\__ || \\ ||___ || \\     \\__  \\_//  || \|| ||    ||  \\_|| \\_// || \\ || ||   ||   ||  \\_//  || \||"



while(1):
    print()
    print()
    print("\t\t\tLet's Begin ")
    print()
    print()
    print("\t\t\tPress 0: Configure Docker")
    print("\t\t\tPress 1: Start Docker service")
    print("\t\t\tPress 2: Check List of OS images you have")
    print("\t\t\tPress 3: Launch a Container")
    print("\t\t\tPress 4: To see Active Containers")
    print("5]  Stop Container")
    print("6]  Terminate a Container")
    print("8]  Attach a Container")
    print("9]  Configure a WebServer")
    print("10] Add new files to the active webserver")
    print("11] Exit")
    option = input("\n\t\t\tSelect an option: ")


    if(option=="0"):
        print("\t\t\tConfiguring Docker........")
        os.system("sleep 2")
        os.system('echo \[Docker\] >> /etc/yum.repos.d/docker.repo')
        os.system('echo baseurl\t\=\thttps://download.docker.com/linux/centos/7/x86_64/stable/Packages/ >> /etc/yum.repos.d/docker.repo')
        os.system('echo gpgcheck\=0 >> /etc/yum.repos.d/docker.repo')
        os.system("yum install docker-ce --nobest")
        print("\t\t\tSuccessfully Configured Docker Now start docker service to Luanch container")
    elif(option=="1"):
        os.system("systemctl start docker")
        os.system("system status docker")
        print ("\t\t\tDocker started")
    elif(option=="2"):
        os.system("docker images")
    elif(option=="3"):
        osName = input("\t\t\tEnter an OS name: ")
        tag = input("\t\t\tEnter the tag: ")
        name = input("\t\t\tEnter a name of your container: ")
        os.system(f"docker run -dit --name {name} {osName}:{tag}")
        print(f"\t\t\tSuccesssfully Launched {name}")
    elif(option=="4"):
        os.system("docker ps -a")
        print()
    elif(option=="5"):
        cname = input("\t\t\tEnter the container Name/ID to stop: ")
        os.system(f"docker stop {cname}")
        print(f"\t\t\tSuccessfuly Stopped {cname}")
    elif(option=="6"):
        cname = input("\t\t\tEnter the container Name/ID: ")
        os.system(f"docker rm -f {cname}")
        print(f"\t\t\tSuccessfully removed {name} container")
    elif(option=="8"):
        idname = input("\t\t\t\Enter the container Name/ID: ")
        os.system(f"docker attach {idname}")
    elif(option=="9"):
        name = input("Enter a Name for os: ")
        files = input("Enter the path of the files to be served by the webserver: ")
        os.system(f"docker run -dit -p {port}:80 --name {name} httpd:latest")
        print("\nYour container is launched")
        print("Transfering your files..........")
        os.system(f"docker cp {files} {name}:/var/www/html/")
        print(f"You can n
    elif(option=="10"):
        name = input("Enter the Container Name: ")
        files = input("Enter the path of the files to be added: ")
        os.system(f"docker cp {files} {name}:/var/www/html/")
    elif(option=="11"):
        print("Exiting Docker Menu  .......Please Wait..............")
        sleep(2)
        break

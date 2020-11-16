import os
import subprocess

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





def webserver():

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

def HadoopMenu():
    while(1):
        print("\t\t\t\tPress 1 to Configure Local Server\n\t\t\t\tPress 2 to Configuring Remote Server")
        print('\t\t\t\tPress 0 to Exit')
        print('\t\t\t\t => ', end='')
        cmd=input()
        print()
        print()
        print("Welcome to Hadoop Configuration")
        print('\t\t\tpress 1 to Configure and Start NameNode') 
        print('\t\t\tpress 2 to Configure and Start DataNode')
        print("\t\t\tpress 3 to Check the status of connected slave")
        print("\t\t\tpress 4 to check NameNode Status")
        print("\t\t\tpress 5 to Check DataNode status")
        print("\t\t\tpress 6 to Stop NameNode")
        print("\t\t\tpress 7 to Stop Datanode")
        print("\t\t\tpress 8 to exit")
        print('\t\t\t\t =>  ', end='')         
        cmd2=input()
          
        if cmd2=='3':
                print("Getting Data.............")
                os.system("hadoop dfsadmin -report")  

        elif cmd2=='4':
                print("Choose an option: \n1] Local\n2] Remote\n")
                lor = input("Select an option: \n")
                if(lor=="1"):
                    os.system("jps")
                elif(lor=="2"):
                    ip = input("Enter the remote IP: ")
                    password = g.getpass("Please enter the password: \n")
                    os.system(f"sshpass -p {password} ssh root@{ip} jps") 

        elif cmd2=='5':
                print("Choose an option: \n1] Local\n2] Remote\n")
                lor = input("Select an option: \n")
                if(lor=="1"):
                    os.system("jps")
                elif(lor=="2"):
                    ip = input("Enter the remote IP: ")
                    password = g.getpass("Please enter the password: \n")
                    os.system(f"sshpass -p {password} ssh root@{ip} jps")               
        
        elif cmd2=='6':             
                print("Choose an option: \n1] Local\n2] Remote\n")
                lor = input("Select an option: \n")
                if(lor=="1"):
                    os.system("hadoop-daemon.sh stop namenode")
                    print("Stopped local NameNode")
                elif(lor=="2"):
                    ip = input("Enter the remote IP: ")
                    password = g.getpass("Please enter the password: \n")
                    os.system(f"sshpass -p {password} ssh root@{ip} hadoop-daemon.sh stop namenode")
                    print("Stopped remote NameNode")

        elif(option=="7"):
                print("Choose an option: \n1] Local\n2] Remote\n")
                lor = input("Select an option: \n")
                if(lor=="1"):
                    os.system("hadoop-daemon.sh stop datanode")
                    print("Stopped local DataNode")
                elif(lor=="2"):
                    ip = input("Enter the remote IP: ")
                    password = g.getpass("Enter the password: ")
                    os.system(f"sshpass -p {password} ssh root@{ip} hadoop-daemon.sh stop datanode")
                    print("Stopped remote DataNode")
        elif(option=="8"):
                print("Exiting Hadoop Menu  .......Please Wait..............")
                os.system('sleep 2')
                break          

def dockerMenu(): 
    
    print("  \t\t\t____     ___     ___ __ __  ____ ____       ___   ___   __  __  ____ __   ___  __ __ ____   ___  ______ __   ___   __  __")
    print("  \t\t\t|| \\   // \\   //   || // ||    || \\     //    // \\  ||\ || ||    ||  // \\ || || || \\ // \\ | || | ||  // \\  ||\ ||")
    print("  \t\t\t||  )) ((   )) ((    ||<<  ||==  ||_//    ((    ((   )) ||\\|| ||==  || (( ___ || || ||_// ||=||   ||   || ((   )) ||\\||")
    print("  \t\t\t||_//   \\_//   \\__ || \\ ||___ || \\     \\__  \\_//  || \|| ||    ||  \\_|| \\_// || \\ || ||   ||   ||  \\_//  || \||")



    while(1):
        print()
        print()
        print("\t\t\tLet's Begin ")
        print()
        print()
        print("\t\t\tPress 1: Configure Docker")
        print("\t\t\tPress 2: Start Docker service")
        print("\t\t\tPress 3: Check List of OS images you have")
        print("\t\t\tPress 4: Launch a Container")
        print("\t\t\tPress 5: To see Active Containers")
        print("\t\t\tPress 6:  Stop Container")
        print("\t\t\tPress 7: Terminate a Container")
        print("\t\t\tPress 8: Configure a WebServer")
        print("\t\t\tPress 9: Attach a Container")
        print("\t\t\tPress 10: Add new files to the active webserver")
        print("\t\t\tPress 11: Exit")
        option = input("\n\t\t\tSelect an option: ")

        if(option=="1"):
            print("\t\t\tConfiguring Docker........")
            os.system("sleep 2")
            os.system('echo \[Docker\] >> /etc/yum.repos.d/docker.repo')
            os.system('echo baseurl\t\=\thttps://download.docker.com/linux/centos/7/x86_64/stable/ >> /etc/yum.repos.d/docker.repo')
            os.system('echo gpgcheck\=0 >> /etc/yum.repos.d/docker.repo')
            os.system("yum install docker-ce --nobest")
            print("\t\t\tSuccessfully Configured Docker Now start docker service to Luanch container")
        elif(option=="2"):
            os.system("systemctl start docker")
            os.system("system status docker")
            print ("\t\t\tDocker started")
            os.system('sleep 2')
        elif(option=="3"):
            os.system("docker images")
            os.system('sleep 2')
        elif(option=="4"):
            osName = input("\t\t\tEnter an OS name: ")
            tag = input("\t\t\tEnter the tag: ")
            name = input("\t\t\tEnter a name of your container: ")
            os.system(f"docker run -dit --name {name} {osName}:{tag}")
            print(f"\t\t\tSuccesssfully Launched {name}")
            os.system('sleep 2')
        elif(option=="5"):
            os.system("docker ps -a")
            print()
            os.system('sleep 2')
        elif(option=="6"):
            cname = input("\t\t\tEnter the container Name/ID to stop: ")
            os.system(f"docker stop {cname}")
            print(f"\t\t\tSuccessfuly Stopped {cname}")
            os.system('sleep 2')
        elif(option=="7"):
            cname = input("\t\t\tEnter the container Name/ID: ")
            os.system(f"docker rm -f {cname}")
            print(f"\t\t\tSuccessfully removed {name} container")
            os.system('sleep 2')
        elif(option=="9"):
            idname = input("\t\t\t\Enter the container Name/ID: ")
            os.system(f"docker attach {idname}")
        elif(option=="8"):
            ip = input("Enter Your IP")
            port = input("Enter the port number: ")
            name = input("Enter a Name for os: ")
            files = input("Enter the path of the files to be served by the webserver: ")
            os.system(f"docker run -dit -p {port}:80 --name {name} httpd:latest")
            print("\nYour container is launched")
            print("Transfering your files..........")
            os.system(f"docker cp {files} {name}:/var/www/html/")
            print(f"You can now access the webpage at {ip}:{port}/{files}")
            os.system('sleep 2')
        elif(option=="10"):
            name = input("Enter the Container Name: ")
            files = input("Enter the path of the files to be added: ")
            os.system(f"docker cp {files} {name}:/var/www/html/")
            os.system('sleep 2')
        elif(option=="11"):
            print("Exiting Docker Menu  .......Please Wait..............")
            os.system('sleep 2')
            break

def LVMMenu():
    while(1):
        print()
        print()
        print("Welcome to LVM Configuration")
        print("\t\t\t press 1: Check Disk Information")
        print("\t\t\t press 2: Create a Physical Volume")
        print("\t\t\t press 3: Create a Volume Group")
        print("\t\t\t press 4: Create, Format, Mount LVM")
        print("\t\t\t press 5: Extend LVM")
        print("\t\t\t press 6: Exit")
        print()
        option = input("Select an option: ")
        if(option == "1"):
            os.system("fdisk -l")
        elif(option == "2"):
            disk_name = input("Please spcify the disk name: ")
            os.system(f"pvcreate {disk_name}")
        elif(option == "3"):
            vgname = input("Name of the Volume Group: ")
            disks = input("Please specify all the DiskNames ( with spaces ): ")
            os.system(f"vgcreate {vgname} {disks}")
        elif(option == "4"):
            vgname = input("Name of the Volume Group: ")
            lvmname = input("Name of the LVM: ")
            size = input("Enter the size: ")
            mount_point = input("Specify the Mount Point: ")
            os.system(f"lvcreate --size {size} --name {lvmname} {vgname}")
            os.system(f"mkfs.ext4 /dev/{vgname}/{lvmname}")
            os.system(f"mount /dev/{vgname}/{lvmname} {mount_point}")
        elif(option == "5"):
            vgname = input("Specify the name of the Volume Group: ")
            lvmname = input("Specify the name of the LVM: ")
            size = input("Size to be increased: ")
            os.system(f"lvextend --size +{size} /dev/{vgname}/{lvmname}")
            os.system(f"resize2fs /dev/{vgname}/{lvmname}")
        elif(option == "6"):
            print("Exiting LVM Menu  .......Please Wait..............")
            os.system('sleep 2')
            break

def AWSMenu():
    while(1):
        print()
        print()
        print("Welcome to AWS Configuration\n\n")
        print("\t\t\t press 1: Set a User Profile")
        print("\t\t\t press 2:  Create a KeyPair")
        print("\t\t\t press 3:  List of VPC-ids")
        print("\t\t\t press 4:  List of Subnet-ids")
        print("\t\t\t press 5:  Create a Security Group")
        print("\t\t\t press 6:  List of all Security Group IDs")
        print("\t\t\t press 7:  Add Inbound Rules to Security Group")
        print("\t\t\t press 8:  Launch Instance")
        print("\t\t\t press 9:  List of all Instances")
        print("\t\t\t press 10: Connect to an Instance")
        print("\t\t\t press 11: Stop Instances")
        print("\t\t\t press 12: Terminate Instances")
        print("\t\t\t press 13: Create an EBS Volume")
        print("\t\t\t press 14: List of all EBS Volumes")
        print("\t\t\t press 15: Attach Volume")
        print("\t\t\t press 16: Create an S3 Bucket")
        print("\t\t\t press 17: Upload File to S3 Bucket")
        print("\t\t\t press 18: Create a CloudFront Distribution")
        print("\t\t\t press 19: Exit\n\n")
        option = input("Select an option: ")
        if(option=="1"):
            os.system("aws configure")
        elif(option=="2"):
            keyName = input("Enter the KeyName: ")
            os.system(f"aws ec2 create-key-pair --key-name {keyName} --query \"KeyMaterial\" --output text > {keyName}.pem")
            print("Key has been downloaded to your current directory.")
        elif(option=="3"):
            print("VPC-ID\t\t\tDefault_VPC")
            os.system("aws ec2 describe-vpcs --query \"Vpcs[*].[VpcId,IsDefault]\" --output=text")
        elif(option=="4"):
            print("Availability Zone\t\tSubnetID\t\tVpcID")
            os.system("aws ec2 describe-subnets --query \"Subnets[*].[AvailabilityZone,SubnetId,VpcId]\" --output=text")
        elif(option=="5"):
            gname = input("Enter group_name: ")
            des = input("Enter description: ")
            os.system(f"aws ec2 create-security-group --description \"{des}\" --group-name {gname}")
        elif(option=="6"):
            os.system("aws ec2 describe-security-groups --query \"SecurityGroups[*].[GroupName,GroupId]\" --output=json")
        elif(option=="7"):
            groupID = input("Please enter the Security Group ID: ")
            protocol = input("Which protocol? ")
            port = input("Enter the port number: ")
            cidr = input("Enter the IP range to be allowed ( in CIDR notation ): ")
            os.system(f"aws ec2 authorize-security-group-ingress --group-id {groupID} --protocol {protocol} --port {port} --cidr {cidr}")
            print(f"Added {protocol} to the Inbound Rules")
        elif(option=="8"):
            imageId = input("Enter the AMI ID: ")
            instanceType = input("Enter the Instance Type: ")
            subnetId = input("Enter the Subnet-ID: ")
            sg = input("Enter the Security Group ID: ")
            keyname = input("Enter the KeyName: ")
            count = input("How many instances you want? ")
            os.system(f"aws ec2 run-instances --image-id {imageId} --count {count} --instance-type {instanceType} --key-name {keyname} --security-group-ids {sg} --subnet-id {subnetId}")
        elif(option=="9"):
            print("Instance-ID\t\tPublicIP")
            os.system("aws ec2 describe-instances --query \"Reservations[*].Instances[*].[InstanceId,PublicIpAddress]\" --output=text")
        elif(option=="10"):
            ip = input("Enter the PublicIP: ")
            keyName = input("Enter the KeyName: ")
            os.system(f"ssh -i {keyName}.pem ec2-user@{ip}")
        elif(option=="11"):
            instanceIDs = input("Enter the Instance IDs ( with space in between ): ")
            os.system(f"aws ec2 stop-instances --instance-ids {instanceIDs}")
        elif(option=="12"):
            instanceIDs = input("Enter the Instance IDs ( with space in between ): ")
            os.system(f"aws ec2 terminate-instances --instance-ids {instanceIDs}")
        elif(option=="13"):
            size = input("Enter the size: ")
            az = input("Enter the Availability Zone: ")
            name = input("Enter Tag Name: ")
            tag = "ResourceType=volume,Tags=[{Key=Name,Value="+name+"}]"
            os.system(f"aws ec2 create-volume --availability-zone {az} --size {size} --tag-specifications \"{tag}\"")
        elif(option=="14"):
            print("Displaying VolumeID,Availability Zone,Size,Tag\n")
            os.system("aws ec2 describe-volumes --query \"Volumes[*].[VolumeId,AvailabilityZone,Size,Tags[*].Value]\"")
        elif(option=="15"):
            volId = input("Enter the Volume ID: ")
            instanceID = input("Enter the Instance ID: ")
            device = input("Enter Disk Name: ")
            os.system(f"aws ec2 attach-volume --device {device} --instance-id {instanceID} --volume-id {volId}")
        elif(option=="16"):
            bucketName = input("Enter the Bucket Name: ")
            region = input("Enter the Region: ")
            os.system(f"aws s3api create-bucket --bucket {bucketName} --region {region} --create-bucket-configuration LocationConstraint={region}")
            opt= input("Do you want to make the bucket public? y or n: ")
            if(opt=="y"):
                os.system(f"aws s3api put-bucket-acl --acl public-read --bucket {bucketName}")
        elif(option=="17"):
            bucketname = input("Enter the Bucket Name: ")
            filePath = input("FileName: ")
            os.system(f"aws s3api put-object --bucket {bucketname} --body {filePath} --key {filePath}")
        elif(option=="18"):
            bn = input("Enter Bucket Name: ")
            os.system(f"aws cloudfront create-distribution --origin-domain-name {bn}.s3.amazonaws.com")
        elif(option=="19"):
            print("Exiting AWS Menu  .......Please Wait..............")
            os.system('sleep 2')
            break        

while(1):

    print()
    print()
    print("\t\t\tWelcome to Python Automation Menu")
    print()
    print()
    print("\t\t\t press 0: configure webserver")
    print("\t\t\t press 1: Hadoop Configuration")
    print("\t\t\t press 2: LVM Configuration")
    print("\t\t\t press 3: AWS Configuration")
    print("\t\t\t press 4: Docker Configuration")
    print("\t\t\t press 5: Exit")
    option = input("choose an option: ")
    if(option=="0"):
        webserver()
    elif(option=="1"):
        HadoopMenu()
    elif(option=="2"):
        LVMMenu()
    elif(option=="3"):
        AWSMenu()
    elif(option=="4"):
        dockerMenu()
    elif(option=="5"):
        print("Exiting Program ......Please Wait............")
        os.system('sleep 2')
        exit()

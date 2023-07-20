#Dean Takle - 20124863
import netmiko
import getpass

#User inputs - added to ssh dictionary + telnet dictionary
host = input("Enter IP Address: ")
username = input("Enter Username: ")
password = getpass.getpass()

#added only to telnet dictionary - password used to access EXEC
secret = getpass.getpass()

#ssh dictionary - takes inputs and runs ssh connection
ssh = {
    'device type':'cisco_ios',
    'host': host,
    'username': username,
    'password': password
}

#telnet dictionary - takes inputs and runs telent connection 
telnet = {
    "device_type": "cisco_ios_telnet",
    "host": host,
    "username": username,
    "password": password,
    "secret": secret
}

#function for ssh - executes the inputs added to the ssh dictionary
def sshToDevice():
    device = netmiko.ConnectHandler(**ssh)
    testCommand = device.send_command('sh ip int br')
    print(testCommand)

#function for telnet - executes the inputs added to the telnet dictionary
def telnetToDevice():
    device = netmiko.ConnectHandler(**telnet)
    testCommand = device.send_command('sh clock')
    print(testCommand)

#Menu that will allow for the user to choose what connection they are wanting to connect via
choice = input("Do you want to SSH (1) or Telnet (2) to the device? ")
#runs ssh dictionary if chosen
if choice == "1":
    sshToDevice()
#runs telnet dictionary if chosen
elif choice == "2":
    telnetToDevice()
#displays this message if something else is entered
else:
    print("Please try again!")
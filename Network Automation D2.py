#Dean Takle - 20124863
import netmiko
import getpass

#User Inputs - if using user inputs
#Enter correct ips otherwise it won't work - R1 = 192.168.1.1, S1 = 192.168.2.1
R1host = input("Enter IP Address For R1: ")
S1host = input("Enter IP Address For S1: ")

#cisco
R1username = input("Enter Username For R1: ")
S1username = input("Enter Username For S1: ")

#cisco - getpass makes it so the password is covered
R1password = getpass.getpass()
S1password = getpass.getpass()

#class - used to access EXEC mode
R1secret = getpass.getpass()
S1secret = getpass.getpass()

#SwitchInfo dictionary - stores inputs for the switch
switchInfo = {
    'device_type': 'cisco_ios',
    'host': S1host,
    'username': S1username,
    'password': S1password,
    'secret': S1secret
}
#RouterInfo dictionary - stores inputs for the Router
routerInfo = {
    'device_type': 'cisco_ios',
    'host': R1host,
    'username': R1username,
    'password': R1password,
    'secret': R1secret
}

#Runs the commands to configure loopback 0 with the following ip address
routerCommands = ['int loopback 0', 'ip address 10.10.63.1 255.255.255.255']

#Runs the commands to configure vlan(s) numbers and corresponding names
switchCommands = ['vlan 23','name Bikes','vlan 33','name Trikes','vlan 43','Name Management','vlan 53','name Parking','vlan 63','name Native']

#runs trunk and switchport commands
trunkCommands = ['int g0/1', 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport native valn63', 'switchport trunk allowed vlan 23','switchport trunk allowed vlan 33','switchport trunk allowed vlan 43','switchport trunk allowed vlan 53']
  
#runs etherchannel f0/1 command
ether1commands = ['int f0/1', 'switchport access vlan 63', 'switchport mode trunk', 'no shut']

#runs etherchannel f0/2 command
ether2commands = ['int f0/2', 'switchport access vlan 63', 'switchport mode trunk', 'no shut']

def configureDevice(info):
    device = netmiko.ConnectHandler(**info)
    device.enable()
    
    hostname = device.send_command('sh run | i host').split()[1]
    print (hostname)
    
    if 'S' in hostname:
        device.send_config_set(switchCommands)
    elif 'R' in hostname:
        device.send_config_set(routerCommands)
    else:
        print('Device Type Not Found!')
       
configureDevice(switchInfo)
configureDevice(routerInfo)
#===================================
from paramiko import SSHClient, AutoAddPolicy
#===================================
#            Functions
#-----------------------------------
def ipread():
        bip = []
        with open('ElastiFlow_ Public Threats (flows) - table.csv') as f:    
                for line in f:
                        bip.append(line.split(',')[1])
                        bipstrip = map(lambda each:each.strip('"'), bip)
        print("Added " + str(len(bip)) + "Ip(s) to be blocked for 10 Days")
        return bipstrip

def cleartxt():
         os.remove('ElastiFlow_ Public Threats (flows) - table.csv')
                                            
def writeconf(blockip):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect("192.168.1.1", username="Janco", password="passwordhere")
    for i in blockip:
           client.exec_command("/ip firewall address-list add address=" + i +" list=Port_Scanner timeout=10d")
    print("All IPs Blocked")      
    client.close()
    cleartxt()
#-----------------------------------
#           Main Code             
#-----------------------------------
importip = ipread()
writeconf(importip)
 



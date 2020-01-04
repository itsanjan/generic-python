import paramiko

myhostname = '192.168.17.128'
myusername = 'anjan'
mypassword = 'anjan4450'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=myhostname, username=myusername, password=mypassword)
channel = ssh_client.invoke_shell()

# stdin,stdout,stderr=ssh_client.exec_command("ls")
# # stdin.write('anjan4450\n')
# print(stdout.readlines())
#
# stdin,stdout,stderr=ssh_client.exec_command("cd Documents; pwd")
# # stdin.write('anjan4450\n')
# print(stdout.readlines())
#
# stdin,stdout,stderr=ssh_client.exec_command("ls")
# # stdin.write('anjan4450\n')
# print(stdout.readlines())

stdin,stdout,stderr=channel.exec_command("cd Documents; pwd")
print(stdout.readlines())
stdin,stdout,stderr=channel.exec_command("ls")
print(stdout.readlines())
ssh_client.close()

import subprocess

output = subprocess.check_output('hostname', shell=True)
hostname = output.decode('utf-8').rstrip()

group_list = ["Administrators","\"Power Users\"", "Users"]
command= "net localgroup "

file = open("foutput.txt","w")

for group in group_list:
    output = subprocess.check_output(command+group, shell=True)
    output2 = output.decode('utf-8')
    for l in output2.splitlines()[6:-2]:
        # account = l.split(' ')[0]
        account = l.strip()
        line = "{}:{}:{}\n".format(hostname, group, account)
        print(line)
        file.write(line)

file.close()
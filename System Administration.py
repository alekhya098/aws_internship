import os
os.system("ls")
sys-admin.py README.md
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
import subprocess
subprocess.run(["ls"])
sys-admin.py  sys-admin_2.py  README.md
subprocess.run(["ls","-l"])

total 12
-rw-r--r-- 1 ec2-user ec2-user  55 Apr 16 20:20 sys-admin.py
-rw-r--r-- 1 ec2-user ec2-user 343 Apr 16 19:07 sys-admin_2.py
-rw-r--r-- 1 ec2-user ec2-user 569 Apr  6 02:17 README.md
subprocess.run(["ls","-l","README.md"])
-rw-r--r-- 1 ec2-user ec2-user 569 Apr  6 02:17 README.md
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
Gathering system information with command: uname -a                          
Linux ip-172-31-29-181 4.4.0-139-generic #165-Ubuntu SMP Wed Oct 24 10:58:50
UTC 2018 x86_64 x86_64 x86_64 GNU/Linux 
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

Gathering active process information with command: ps -x                       
  PID TTY      STAT   TIME COMMAND                                           
18976 pts/459  S+     0:00 python3.6 lab_15_2.py                               
18977 pts/459  R+     0:00 ps -x                                             
21139 pts/459  S      0:00 /bin/bash -c export OLD_HOME=/home/ccc_4dfa91ec5a_
21164 pts/459  S      0:00 bash --rcfile /home/ccc_4dfa91ec5a_45122/.termrc -
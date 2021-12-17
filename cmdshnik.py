from os import system as sys_command
from os import name as os_name


if os_name == 'nt':
    print('Windows')
elif os_name == 'posix':
    print('Linux')
elif os_name == 'mac':
    print('Mac')
elif os_name == 'os2':
    print('OS/2')
elif os_name == 'ce':
    print('Windows CE')
elif os_name == 'java':
    print('java OS')
print()


while True:
    print(sys_command(input()))
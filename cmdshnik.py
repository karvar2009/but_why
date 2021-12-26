from os import system as sys_command
from os import name as os_name
from os import chmod as os_dostup
from os.path import dirname as os_dirname
from os.path import realpath as os_realpath
from getpass import getuser


def add_to_startup(file_path="", user_name=getuser()):
    if file_path == "":
        file_path = os_dirname(os_realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % user_name
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


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
    cmd_or_programm = input()
    if cmd_or_programm.lower() == 'открыть доступ':
        dost = input('ввсдите путь к файлу: \n')
        os_dostup(dost, mode=7, dir_fd=None, follow_symlinks=True)
    elif cmd_or_programm.lower() == 'добавить в автозагрузку':
        path_au = input('Введите путь к файлу(этот файл по умолчанию): ')
        user_au = input('Введите пользователя(ваш по умолчанию): ')
        add_to_startup(path_au, user_au)
    else:
        print(sys_command(cmd_or_programm))

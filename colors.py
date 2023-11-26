import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(Back.RED + Fore.YELLOW + 'Welcome to LinuxHint')



print(Back.GREEN + 'I like programming')

print(Style.RESET_ALL)

print(Style.DIM + 'Learn Python')
print(Style.BRIGHT + 'Google')
print(Style.NORMAL + 'Fru fru')

if __name__ == '__main__':
    pass
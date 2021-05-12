import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

print(Fore.RED + "Hello World")
print(Back.GREEN + "Testing Highlight Color")
print (f"{Fore.RED}H{Fore.GREEN}E{Fore.MAGENTA}L{Fore.BLUE}L{Fore.YELLOW}O{Fore.YELLOW}")
print (f"{Fore.RED}W{Fore.GREEN}O{Fore.MAGENTA}R{Fore.BLUE}L{Fore.YELLOW}D{Fore.MAGENTA}")
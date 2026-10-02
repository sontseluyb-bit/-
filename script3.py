import colorama
from colorama import just_fix_windows_console , Fore , Back , Style
print(Back.BLACK + "робить фон певного кольору")
A = dir(colorama)
B = " ".join(A)
print(Fore.BLUE + B + "виводить абсолютно всі команди")
just_fix_windows_console()
print(Fore.GREEN + "Ця команда просто виправляє консоль як і каже назва " + Style.BRIGHT + "just_fix_windows_console" +
                   Style.RESET_ALL + Fore.GREEN + Back.BLACK +" дозволяє користуватися кольорами на консолі без жодних подальших налаштувань")
print( "Ця команда робить текст " + Style.BRIGHT + "Жирним")

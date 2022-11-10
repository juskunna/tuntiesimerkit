from colorama import Fore, Back, Style

print(Fore.CYAN+ 'Eri väristä tekstiä!')
print("Lisää tekstiä, vieläkin sama väri!")
print(Back.LIGHTCYAN_EX + "Vaihdetaan taustaväri!")
print("Vieläkin sininen teksti ja taustaväri.")

print(Style.RESET_ALL + "Nyt on normaalia.")
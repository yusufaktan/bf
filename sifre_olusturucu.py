from colorama import Fore, Back
# Terminali renklendirmemizi sağlayan kütüphane

import itertools
# Girilen bilgilerin karıştırılması, rastgele şifreler oluşturulması
# için kullandığımız kütüphane

from os import system
# Terminal ekranını temizlemek için kullandığımız kütüphane

import time
# Aralara bekleme süreleri koymak için kullandığımız kütüphane

dizi = []
system("clear")

print("\n ）︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶（")
print(f" ）          {Back.RED}ISTINYE UNIVERSITESI{Back.RESET}          （")
print(" ）----------------------------------------（")
print(" ）            Sifre Olusturucu            （")
print(" ）           ------------------           （")
print(f" ）               {Fore.BLUE}Yusuf AKTAN{Fore.RESET}              （")
print(f" ）               {Fore.BLUE}Emre ERTURK{Fore.RESET}              （")
print(f" ）              {Fore.BLUE}Enes ALBAYRAK{Fore.RESET}             （")
print(f" ）               {Fore.BLUE}Omercem MOD{Fore.RESET}              （")
print(" ）︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵（")

n1 = input(f'{Fore.GREEN}\n  Adı                = {Fore.RESET}')
dizi.append(n1)
print("----------------------------------------")
n2 = input(f'{Fore.GREEN}  Soyadı             = {Fore.RESET}')
dizi.append(n2)
print("----------------------------------------")
n3 = input(f'{Fore.GREEN}  Memleketi          = {Fore.RESET}')
dizi.append(n3)
print("----------------------------------------")
n4 = input(f'{Fore.GREEN}  Doğum Tarihi (Gün) = {Fore.RESET}')
dizi.append(n4)
print("----------------------------------------")
n5 = input(f'{Fore.GREEN}  Doğum Tarihi (Ay)  = {Fore.RESET}')
dizi.append(n5)
print("----------------------------------------")
n6 = input(f'{Fore.GREEN}  Doğum Tarihi (Yıl) = {Fore.RESET}')
dizi.append(n6)
print("----------------------------------------")
n7 = input(f'{Fore.GREEN}  Anne Adı           = {Fore.RESET}')
dizi.append(n7)
print("----------------------------------------")
n8 = input(f'{Fore.GREEN}  Baba Adı           = {Fore.RESET}')
dizi.append(n8)
print("----------------------------------------")
n9 = input(f'{Fore.GREEN}  Sayı 1             = {Fore.RESET}')
dizi.append(n9)
print("----------------------------------------")
n10 = input(f'{Fore.GREEN}  Sayı 2             = {Fore.RESET}')
dizi.append(n10)
print("----------------------------------------")
n11 = input(f'{Fore.GREEN}  Sayı 3             = {Fore.RESET}')
dizi.append(n11)
print("----------------------------------------")
n12 = input(f'{Fore.GREEN}  Sayı 4             = {Fore.RESET}')
dizi.append(n12)
print("----------------------------------------")
n13 = input(f'{Fore.GREEN}  Karakter 1         = {Fore.RESET}')
dizi.append(n13)
print("----------------------------------------")
n14 = input(f'{Fore.GREEN}  Karakter 2         = {Fore.RESET}')
dizi.append(n14)
print("----------------------------------------")
n15 = input(f'{Fore.GREEN}  Karakter 3         = {Fore.RESET}')
dizi.append(n15)
print("----------------------------------------")
n16 = input(f'{Fore.GREEN}  Karakter 4         = {Fore.RESET}')
dizi.append(n16)
print("----------------------------------------")

print(f"{Fore.RED}SIFRELER OLUSTURULUYOR{Fore.RESET}")
time.sleep(1.0)
print(f" {Back.RED}%25  (#########---------------------------){Back.RESET} ")
time.sleep(1.0)
print(f" {Back.RED}%50  (##################------------------){Back.RESET} ")
time.sleep(1.0)
print(f" {Back.RED}%75  (###########################---------){Back.RESET} ")
time.sleep(1.0)
print(f" {Back.RED}%100 (####################################){Back.RESET}")
print("----------------------------------------")

file = open('list.txt', 'a')
for x in itertools.product(dizi, repeat=2):
	sifre = ''.join(x)
	yazdir = file.write(sifre+'\n')

print(f"{Fore.RED}list.txt Oluşturuldu.")
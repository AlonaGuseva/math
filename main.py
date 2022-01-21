from math import *
def funkcija(skaitlis,burts):
  rez = 0
  if burts == "d":
    rez = degrees(skaitlis)
  else:
    rez = radians(skaitlis)
  return rez
skaitlis = int(input("Ievadiet skaitlis: "))
burts = input("Ievadiet burtu (r/d): ")
print("Rezultats = ",funkcija(skaitlis,burts))
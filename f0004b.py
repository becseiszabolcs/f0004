ev  = int(input('hányadik év van: '))
nev = input('Hogy hívnak téged? ')
kor = int(input('És hány éves vagy? '))
születesi_ev = ev - kor
eretsegi_ev = születesi_ev + 18
if eretsegi_ev < születesi_ev + kor:
  print(f"eben az évben éretségizet: {eretsegi_ev}")

else:
  print(f"eben az évben fog éretségizni: {eretsegi_ev}")
print(f"neved: {nev}, születési éved: {születesi_ev}")





#Programa para calcular se o ano será bissexto ou nao:
year = int(input())

#Condições if, elig e else

if year % 4 == 0 :
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

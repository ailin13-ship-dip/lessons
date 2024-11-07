"Signs zodiac"

attemps = 12
while attemps > 0:
    print( f'попыток осталось: {attemps}')

month = input("Введите месяц рождения  ").lower()
day = int(input("Введите день рождения: "))


if(month == '12' and 22 <=  day <= 31 ) or (month == '01' and 1 <= day <= 20):
    print("козерог")
elif(month == '01' and 21 <= day <= 31) or (month == '02' and 1 <= day <= 20):
    print("водолей")
elif(month == '02' and 21 <= day <= 28) or (month == '03' and 1 <= day <= 20):
    print("рыбы")
elif(month == '03' and 21 <= day <= 31) or (month == '04' and 1 <= day <= 20):
    print('овен')
elif(month == '04' and 21 <= day <= 30) or (month == '05' and 1 <= day <= 20):
    print("телец")
elif(month == '05' and 21 <= day <= 31) or (month == '06' and  1 <= day <= 21 ):
    print("близнецы")
elif(month == '06' and 22 <= 30 ) or (month == '07' and 1 <= day <= 22):
    print("рак")
elif(month == '07' and 23 <= day <= 31) or (month == '08' and 1 <= day <= 23):
    print("лев")
elif(month == '08' and 24 <= day <= 31) or (month == '09' and 1 <= day <= 23):
    print("дева")
elif(month == '09' and 24 <= day <= 30) or (month == '10' and 1 <= day <= 23):
    print("весы")
elif(month == '10'  and 24 <= day <= 31) or (month == '11' and 1 <= day <= 22):
    print("скорпион")
elif(month == '11' and 23 <= day <= 30) or (month == '12' and 1 <= day <= 21):
    print("стрелец")
else:
    print("Считается неправильно введенной датой")
attemps -= 1
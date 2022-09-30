let=int(input('Введите количество лет: '))
if let>=4:
    a=int(let/4)
    k_exp=int(((let-a)*365*8*60/5)+(a*366*8*60/5))
else:
    k_exp=int((let*365*8*60/5))
print('За',let,'лет Вы просмотрите',k_exp,'экспонатов')
exp=int(input('Сколько экспонатов просмотренно? - '))
timemin=exp*5
timedn=round(timemin/(8*60))
if (timedn/365)>=4:
    a=int(timedn/(365*4))
    timelet=round(((timedn-(366*a))/365)+a)
else:timelet=round(timedn/365)
print('На просмотр',exp,'экспонатов вы потратите:')
print(timemin,'минут')
print(timedn,'дней')
print(timelet,'лет')
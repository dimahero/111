tickets = 0
number_of_tickets = int(input("Введите количество билетов, которые хотите приобрести: "))
skidka = 0

for age in range(number_of_tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        tickets += 0
    elif 18 <= age < 25:
        tickets += 990
    else:
        tickets += 1390

if tickets == 0:
    print("Несовершеннолетним посетителям вход бесплатный")
else:
    print("Ваша сумма к оплате: ",tickets," рублей")
    if number_of_tickets>3:
        skidka = (tickets/100)*10
        print("Ваша скидка: ", skidka, " рублей")
        tickets -=skidka
print("Ваша сумма к оплате с учетом скидки: ", tickets, " рублей")
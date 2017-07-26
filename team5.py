import numpy as np
import time

nteam5r = ['Спартак-5', 'Реал-5', 'Арсенал-5', 'Динамо-5','Локо-5', 'Машина-5', 'Мозг-5', 'Пайтон-5', 'Питон-5', 'Ноут-5',
           'Комп-5', 'Микро-5', 'Фокст-5', 'Ювентус-5', 'Киров-5', 'Юность-5']
nteam5 = np.random.choice (nteam5r)

name=['Виктор Петухов','Артемий Лусков','Леонид Федун','Артур Васюков', 'Виктор Ан', 'Витор Ан', 'Папа Замечек', 'Артур Наберегу', 'Мечка Наберегу', 'Плюшовая Радость', 'Мечка Неизгубена', 'Бял Мечка', 'Ръж Мечка', 'Арсений Яровой',
            'Мякиш Плюшовый', 'Михаил Яровой', 'Федор Яровой', 'Белый Воротчик', 'Рыжий Защитник', 'Мечка Форнит', 'Мечка Софийский', 'Мечка Болгарский', 'Мечка Мальтийский', 'Мечка Австрийский', 'Арсений Кукушкин',
            'Мякиш Яровой', 'Мишка Главный', 'Федор Любимчик', 'Валерий Карпин', 'Виктор Помащун', 'Алексей Онопко', 'Виктор Онопко',
      'Андрей Карпин', 'Александр Кукушкин', 'Олег Корнеев', 'Олег Кучин', 'Дмитрий Комбаров', 'Кирилл Комбаров', 'Кер Лаэда', 'Мастер Огня', 'Артур Пушкин',
      'Леонид Слуцкий','Артур Васюковский','Артур Васюк','Артур Ваков','Артур Вюков','Артур Вков','Андрей Попов','Андрей Попопов','Андрей Потопов',
      'Андрей Посопов','Андрей Сопов','Андрей Вопов','Андрей Ропов','Андрей Домопов','Андрей Иванов','Михаил Иванов','Андр Иванов','Андриус Иванов',
      'Михаил Иванов','Андрей Ивановский', 'Сергей Молодцов', 'Сергей Прокопьев', 'Валентин Жуков', 'Валентин Иванов', 'Валентин Попов',
      'Валентин Попович']

age = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]

#бот 451
sostav5 = []
nage5 = []
ngoal5 = []
ndef5 = []
npm5 = []
nforw5 = []
nspeed5 = []

i=0
j=0
igrok5 = []
nigrok5 = []


goalkeeper = [10,11,12,13,14,15,16,17,18,19,20]
defender = [0,1,2,3,4,5,6,7,8,9,10]
pm = [0,1,2,3,4,5]
udar = [1,2,3,4,5,6,7,8,9,10]
speed = [1,2,3,4,5,6,7,8,9,10]
igrok1 = np.random.choice (goalkeeper)
nigrok1 = np.random.choice (name)
igrok2 = np.random.choice(defender)
igrok3 = np.random.choice (pm)
igrok4 = np.random.choice (udar)
igrok5 = np.random.choice (speed)
igrok6 = np.random.choice (age)
sostav5 += [nigrok1]
ngoal5 += [igrok1]
ndef5 += [igrok2]
npm5 += [igrok3]
nforw5 += [igrok4]
nage5 += [igrok5]
nspeed5 += [igrok6]



defender = [10,11,12,13,14,15,16,17,18,19,20]
pm = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
udar = [1,2,3,4,5,6,7]
speed = [5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19,20]
i=0
while i <4:
    igrok1 = np.random.choice(defender)
    igrok2 = np.random.choice(pm)
    igrok3 = np.random.choice(udar)
    nigrok5 = np.random.choice(name)
    igrok5 = np.random.choice(speed)
    igrok6 = np.random.choice(age)
    sostav5 += [nigrok5]
    ngoal5 += [0]
    ndef5 += [igrok1]
    npm5 += [igrok2]
    nforw5 += [igrok3]
    nage5 += [igrok5]
    nspeed5 += [igrok6]
    i+=1

pm = [10,11,12,13,14,15,16,17,18,19,20]
defender = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
udar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
i=0
while i <5:
    igrok1 = np.random.choice(defender)
    igrok2 = np.random.choice(pm)
    igrok3 = np.random.choice(udar)
    nigrok5 = np.random.choice(name)
    igrok5 = np.random.choice(speed)
    igrok6 = np.random.choice(age)
    sostav5 += [nigrok5]
    ngoal5 += [0]
    ndef5 += [igrok1]
    npm5 += [igrok2]
    nforw5 += [igrok3]
    nage5 += [igrok5]
    nspeed5 += [igrok6]
    i+=1

pm = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
defender = [1,2,3,4,5,6,7]
udar = [10,11,12,13,14,15,16,17,18,19,20]
i=0
while i <1:
    igrok1 = np.random.choice(defender)
    igrok2 = np.random.choice(pm)
    igrok3 = np.random.choice(udar)
    nigrok5 = np.random.choice(name)
    igrok5 = np.random.choice(speed)
    igrok6 = np.random.choice(age)
    sostav5 += [nigrok5]
    ngoal5 += [0]
    ndef5 += [igrok1]
    npm5 += [igrok2]
    nforw5 += [igrok3]
    nage5 += [igrok5]
    nspeed5 += [igrok6]
    i+=1


gngoal5 = ngoal5[0]
gndef5 = (ndef5 [1] + ndef5 [2] + ndef5[3]+ndef5[4])/4 +(ndef5[5] +ndef5[9]+ ndef5[6] + ndef5[7] +ndef5[8])/8
gnpm5 = (npm5 [9]+npm5 [6]+npm5 [7]+npm5 [8]+npm5 [5])/4 + (npm5 [1]+npm5 [2]+npm5 [3]+npm5 [4])/8 + (npm5 [10])/12
gnforw5 = (nforw5[10])/2 +(nforw5[9] + nforw5[6]+nforw5[7] + nforw5[8]+nforw5 [5])/8


#print ('Команда -', nteam4)
#nomer4 = []
#i=0
#j=0
#kolvo = len(sostav4)
#for i in range(kolvo):
 #   nomer4 +=[i+1]
  #  print(nomer4[i], sostav4[i])
   # print('Вратарство -', ngoal4[i])
   # print('Защита -',ndef4[i])
   # print('Полузащита -',npm4[i])
   # print('Нападение -',nforw4[i], '\n')
   # time.sleep(2)
   # i+=1
   # j+=1


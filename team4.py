import numpy as np
import time

nteam4r = ['Спартак-4', 'Реал-4', 'Арсенал-4', 'Динамо-4', 'Машина-4', 'Мозг-4', 'Пайтон-4', 'Питон-4', 'Ноут-4',
           'Комп-4', 'Микро-4', 'Фокст-4', 'Ювентус-4', 'Киров-4', 'Юность-4']
nteam4 = np.random.choice (nteam4r)

name=['Виктор Петухов','Артемий Лусков','Леонид Федун','Артур Васюков', 'Виктор Ан', 'Витор Ан', 'Папа Замечек', 'Артур Наберегу', 'Мечка Наберегу', 'Плюшовая Радость', 'Мечка Неизгубена', 'Бял Мечка', 'Ръж Мечка', 'Арсений Яровой',
            'Мякиш Плюшовый', 'Михаил Яровой', 'Федор Яровой', 'Белый Воротчик', 'Рыжий Защитник', 'Мечка Форнит', 'Мечка Софийский', 'Мечка Болгарский', 'Мечка Мальтийский', 'Мечка Австрийский', 'Арсений Кукушкин',
            'Мякиш Яровой', 'Мишка Главный', 'Федор Любимчик', 'Валерий Карпин', 'Виктор Помащун', 'Алексей Онопко', 'Виктор Онопко',
      'Андрей Карпин', 'Александр Кукушкин', 'Олег Корнеев', 'Олег Кучин', 'Дмитрий Комбаров', 'Кирилл Комбаров', 'Кер Лаэда', 'Мастер Огня', 'Артур Пушкин',
      'Леонид Слуцкий','Артур Васюковский','Артур Васюк','Артур Ваков','Артур Вюков','Артур Вков','Андрей Попов','Андрей Попопов','Андрей Потопов',
      'Андрей Посопов','Андрей Сопов','Андрей Вопов','Андрей Ропов','Андрей Домопов','Андрей Иванов','Михаил Иванов','Андр Иванов','Андриус Иванов',
      'Михаил Иванов','Андрей Ивановский', 'Сергей Молодцов', 'Сергей Прокопьев', 'Валентин Жуков', 'Валентин Иванов', 'Валентин Попов',
      'Валентин Попович']

age = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]


#бот 541
sostav4 = []
nage4 =[]
ngoal4 = []
ndef4 = []
npm4 = []
nforw4 = []
nspeed4 = []

i=0
j=0
igrok4 = []
nigrok4 = []


goalkeeper = [10,11,12,13,14,15,16,17,18,19,20]
defender = [0,1,2,3,4,5,6,7,8,9,10]
pm = [0,1,2,3,4,5]
udar = [1,2,3,4,5,6,7,8,9,10]
speed = [1,2,3,4,5,6,7,8,9,10]
nigrok4 = np.random.choice (name)
igrok1 = np.random.choice (goalkeeper)
igrok2 = np.random.choice(defender)
igrok3 = np.random.choice (pm)
igrok4 = np.random.choice (udar)
igrok5 = np.random.choice (speed)
igrok6 = np.random.choice (age)
sostav4 += [nigrok4]
ngoal4 += [igrok1]
ndef4 += [igrok2]
npm4 += [igrok3]
nforw4 += [igrok4]
nspeed4 += [igrok5]
nage4 +=[igrok6]



defender = [10,11,12,13,14,15,16,17,18,19,20]
pm = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
udar = [1,2,3,4,5,6,7]
speed = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
i=0
while i <5:
    igrok1 = np.random.choice(defender)
    igrok2 = np.random.choice(pm)
    igrok3 = np.random.choice(udar)
    nigrok4 = np.random.choice(name)
    igrok5 = np.random.choice(speed)
    igrok6 = np.random.choice(age)
    sostav4 += [nigrok4]
    ngoal4 += [0]
    ndef4 += [igrok1]
    npm4 += [igrok2]
    nforw4 += [igrok3]
    nspeed4 += [igrok5]
    nage4 += [igrok6]
    i+=1

pm = [10,11,12,13,14,15,16,17,18,19,20]
defender = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
udar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

i=0
while i <4:
    igrok1 = np.random.choice(defender)
    igrok2 = np.random.choice(pm)
    igrok3 = np.random.choice(udar)
    nigrok4 = np.random.choice(name)
    igrok5 = np.random.choice(speed)
    igrok6 = np.random.choice(age)
    sostav4 += [nigrok4]
    ngoal4 += [0]
    ndef4 += [igrok1]
    npm4 += [igrok2]
    nforw4 += [igrok3]
    nspeed4 += [igrok5]
    nage4 += [igrok6]
    i+=1

pm = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
defender = [1,2,3,4,5,6,7]
udar = [10,11,12,13,14,15,16,17,18,19,20]
i=0
while i <1:
    igrok1 = np.random.choice(defender)
    igrok2 = np.random.choice(pm)
    igrok3 = np.random.choice(udar)
    nigrok4 = np.random.choice(name)
    igrok5 = np.random.choice(speed)
    igrok6 = np.random.choice(age)
    sostav4 += [nigrok4]
    ngoal4 += [0]
    ndef4 += [igrok1]
    npm4 += [igrok2]
    nforw4 += [igrok3]
    nspeed4 += [igrok5]
    nage4 += [igrok6]
    i+=1


gngoal4 = ngoal4[0]
gndef4 = (ndef4 [1] + ndef4 [2] + ndef4[3]+ndef4[4]+ndef4[5])/4 +( ndef4[9]+ ndef4[6] + ndef4[7] +ndef4[8])/8
gnpm4 = (npm4 [9]+npm4 [6]+npm4 [7]+npm4 [8])/4 + (npm4 [1]+npm4 [2]+npm4 [3]+npm4 [4]+npm4 [5])/8 + (npm4 [10])/12
gnforw4 = (nforw4[10])/2 +(nforw4[9] + nforw4[6]+nforw4[7] + nforw4[8])/8


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


import numpy as np
import time

#generation of name of Team
nteam2r = ['Спартак-2','Манчестер-2', 'Реал-2', 'Арсенал-2', 'Динамо-2', 'Машина-2', 'Мозг-2', 'Пайтон-2', 'Питон-2', 'Ноут-2', 'Комп-2', 'Микро-2', 'Фокст-2']
nteam2 = np.random.choice (nteam2r)

#generation name's players
name=['Виктор Петухов','Артемий Лусков','Леонид Федун','Артур Васюков', 'Виктор Ан', 'Витор Ан', 'Папа Замечек', 'Артур Наберегу', 'Мечка Наберегу', 'Плюшовая Радость', 'Мечка Неизгубена', 'Бял Мечка', 'Ръж Мечка', 'Арсений Яровой',
            'Мякиш Плюшовый', 'Михаил Яровой', 'Федор Яровой', 'Белый Воротчик', 'Рыжий Защитник', 'Мечка Форнит', 'Мечка Софийский', 'Мечка Болгарский', 'Мечка Мальтийский', 'Мечка Австрийский', 'Арсений Кукушкин',
            'Мякиш Яровой', 'Мишка Главный', 'Федор Любимчик', 'Валерий Карпин', 'Виктор Помащун', 'Алексей Онопко', 'Виктор Онопко',
      'Андрей Карпин', 'Александр Кукушкин', 'Олег Корнеев', 'Олег Кучин', 'Дмитрий Комбаров', 'Кирилл Комбаров', 'Кер Лаэда', 'Мастер Огня', 'Артур Пушкин',
      'Леонид Слуцкий','Артур Васюковский','Артур Васюк','Артур Ваков','Артур Вюков','Артур Вков','Андрей Попов','Андрей Попопов','Андрей Потопов',
      'Андрей Посопов','Андрей Сопов','Андрей Вопов','Андрей Ропов','Андрей Домопов','Андрей Иванов','Михаил Иванов','Андр Иванов','Андриус Иванов',
      'Михаил Иванов','Андрей Ивановский', 'Сергей Молодцов']

#age generation
age = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]

#bot 442
sostav2 = []
nage2 = []
ngoal2 = []
ndef2 = []
npm2 = []
nforw2 = []
nspeed2 = []

i=0
j=0
igrok2 = []
nigrok2 = []


#generation skills of goalkeeper
goalkeeper = [10,11,12,13,14,15,16,17,18,19,20]
defender = [0,1,2,3,4,5,6,7,8,9,10]
pm = [0,1,2,3,4,5]
udar = [1,2,3,4,5,6,7,8,9,10]
speed = [1,2,3,4,5,6,7,8,9,10]
igrok1 = np.random.choice(defender)
igrok2 = np.random.choice (goalkeeper)
igrok3 = np.random.choice (pm)
igrok4 = np.random.choice (udar)
igrok5 = np.random.choice (speed)
igrok6 = np.random.choice (age)
nigrok2 = np.random.choice (name)
sostav2 += [nigrok2]
ngoal2 += [igrok2]
ndef2 += [igrok1]
npm2 += [igrok3]
nforw2 += [igrok4]
nspeed2 +=[igrok5]
nage2 +=[igrok6]


defender = [10,11,12,13,14,15,16,17,18,19,20]
pm = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
udar = [1,2,3,4,5,6,7]
speed = [5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19,20]
i=0
while i <4:
    igrok1 = np.random.choice(defender)
    igrok2 = np.random.choice(pm)
    igrok3 = np.random.choice(udar)
    igrok5 = np.random.choice(speed)
    igrok6 = np.random.choice(age)
    nigrok2 = np.random.choice(name)
    sostav2 += [nigrok2]
    ngoal2 += [0]
    ndef2 += [igrok1]
    npm2 += [igrok2]
    nforw2 += [igrok3]
    nspeed2 +=[igrok5]
    nage2 +=[igrok6]
    i+=1

pm = [10,11,12,13,14,15,16,17,18,19,20]
defender = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
udar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
speed = [1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19,20]
i=0
while i <4:
    igrok1 = np.random.choice(defender)
    igrok2 = np.random.choice(pm)
    igrok3 = np.random.choice(udar)
    nigrok2 = np.random.choice(name)
    igrok5 = np.random.choice(speed)
    igrok6 = np.random.choice(age)
    sostav2 += [nigrok2]
    ngoal2 += [0]
    ndef2 += [igrok1]
    npm2 += [igrok2]
    nforw2 += [igrok3]
    nspeed2 +=[igrok5]
    nage2 +=[igrok6]
    i+=1

pm = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
defender = [1,2,3,4,5,6,7]
udar = [10,11,12,13,14,15,16,17,18,19,20]
speed = [6,7,8,9,10, 11,12,13,14,15,16,17,18,19,20]
i=0
while i <2:
    igrok1 = np.random.choice(defender)
    igrok2 = np.random.choice(pm)
    igrok3 = np.random.choice(udar)
    igrok5 = np.random.choice(speed)
    igrok6 = np.random.choice(age)
    nigrok2 = np.random.choice(name)
    sostav2 += [nigrok2]
    ngoal2 += [0]
    ndef2 += [igrok1]
    npm2 += [igrok2]
    nforw2 += [igrok3]
    nspeed2 +=[igrok5]
    nage2 +=[igrok6]
    i+=1

#lines ratings of team
gngoal2 = ngoal2[0]
gndef2 = (ndef2 [1] + ndef2 [2] + ndef2[3]+ndef2[4])/4 +(ndef2[5] + ndef2[6] + ndef2[7] +ndef2[8])/8
gnpm2 = (npm2 [5]+npm2 [6]+npm2 [7]+npm2 [8])/4 + (npm2 [1]+npm2 [2]+npm2 [3]+npm2 [4])/8 + (npm2 [9]+npm2 [10])/12
gnforw2 = (nforw2[9] + nforw2[10])/2 +(nforw2[5] + nforw2[6]+nforw2[7] + nforw2[8])/8



#print ('Команда -', nteam2)
nomer2 = []
i=0
j=0
kolvo = len(sostav2)
#if need, publication of players with skills
for i in range(kolvo):
    nomer2 +=[i+1]
    print(nomer2[i], sostav2[i])
    print ('Возраст -', nage2[i])
    print('Вратарство -', ngoal2[i])
    print('Защита -',ndef2[i])
    print('Полузащита -',npm2[i])
    print('Нападение -',nforw2[i])
    print ('Скорость -',nspeed2[i] , '\n')
    time.sleep(1)
    i+=1
    j+=1



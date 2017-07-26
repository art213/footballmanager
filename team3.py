import numpy as np
import time

nteam3r = ['Спартак-3', 'Реал-3', 'Арсенал-3', 'Динамо-3', 'Машина-3', 'Мозг-3', 'Пайтон-3', 'Питон-3', 'Ноут-3',
           'Комп-3', 'Микро-3', 'Фокст-3', 'Ювентус-3', 'Киров-3', 'Юность-3']
nteam3 = np.random.choice (nteam3r)

name=['Виктор Петухов','Артемий Лусков','Леонид Федун','Артур Васюков', 'Виктор Ан', 'Витор Ан', 'Папа Замечек', 'Артур Наберегу', 'Мечка Наберегу', 'Плюшовая Радость', 'Мечка Неизгубена', 'Бял Мечка', 'Ръж Мечка', 'Арсений Яровой',
            'Мякиш Плюшовый', 'Михаил Яровой', 'Федор Яровой', 'Белый Воротчик', 'Рыжий Защитник', 'Мечка Форнит', 'Мечка Софийский', 'Мечка Болгарский', 'Мечка Мальтийский', 'Мечка Австрийский', 'Арсений Кукушкин',
            'Мякиш Яровой', 'Мишка Главный', 'Федор Любимчик', 'Валерий Карпин', 'Виктор Помащун', 'Алексей Онопко', 'Виктор Онопко',
      'Андрей Карпин', 'Александр Кукушкин', 'Олег Корнеев', 'Олег Кучин', 'Дмитрий Комбаров', 'Кирилл Комбаров', 'Кер Лаэда', 'Мастер Огня', 'Артур Пушкин',
      'Леонид Слуцкий','Артур Васюковский','Артур Васюк','Артур Ваков','Артур Вюков','Артур Вков','Андрей Попов','Андрей Попопов','Андрей Потопов',
      'Андрей Посопов','Андрей Сопов','Андрей Вопов','Андрей Ропов','Андрей Домопов','Андрей Иванов','Михаил Иванов','Андр Иванов','Андриус Иванов',
      'Михаил Иванов','Андрей Ивановский', 'Сергей Молодцов', 'Сергей Прокопьев', 'Валентин Жуков', 'Валентин Иванов', 'Валентин Попов',
      'Валентин Попович']

age = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]

#бот 352
sostav3 = []
nage3 = []
ngoal3 = []
ndef3 = []
npm3 = []
nforw3 = []
nspeed3 = []

i=0
j=0
igrok3 = []
nigrok3 = []


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
nigrok3 = np.random.choice (name)
sostav3 += [nigrok3]
ngoal3 += [igrok2]
ndef3 += [igrok1]
npm3 += [igrok3]
nforw3 += [igrok4]
nspeed3 +=[igrok5]
nage3 +=[igrok6]




defender = [10,11,12,13,14,15,16,17,18,19,20]
pm = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
udar = [1,2,3,4,5,6,7]
speed = [5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19,20]
i=0
while i <3:
    igrok1 = np.random.choice(defender)
    igrok2 = np.random.choice(pm)
    igrok3 = np.random.choice(udar)
    igrok5 = np.random.choice(speed)
    igrok6 = np.random.choice(age)
    nigrok3 = np.random.choice(name)
    sostav3 += [nigrok3]
    ngoal3 += [0]
    ndef3 += [igrok1]
    npm3 += [igrok2]
    nforw3 += [igrok3]
    nspeed3 += [igrok5]
    nage3 += [igrok6]
    i+=1

pm = [10,11,12,13,14,15,16,17,18,19,20]
defender = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
udar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
speed = [1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19,20]
i=0
while i <5:
    igrok1 = np.random.choice(defender)
    igrok2 = np.random.choice(pm)
    igrok3 = np.random.choice(udar)
    nigrok3 = np.random.choice(name)
    igrok5 = np.random.choice(speed)
    igrok6 = np.random.choice(age)
    sostav3 += [nigrok3]
    ngoal3 += [0]
    ndef3 += [igrok1]
    npm3 += [igrok2]
    nforw3 += [igrok3]
    nspeed3 += [igrok5]
    nage3 += [igrok6]
    i+=1

pm = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
defender = [1,2,3,4,5,6,7]
udar = [10,11,12,13,14,15,16,17,18,19,20]
speed = [5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19,20]
i=0
while i <2:
    igrok1 = np.random.choice(defender)
    igrok2 = np.random.choice(pm)
    igrok3 = np.random.choice(udar)
    nigrok3 = np.random.choice(name)
    igrok5 = np.random.choice(speed)
    igrok6 = np.random.choice(age)
    sostav3 += [nigrok3]
    ngoal3 += [0]
    ndef3 += [igrok1]
    npm3 += [igrok2]
    nforw3 += [igrok3]
    nspeed3 += [igrok5]
    nage3 += [igrok6]
    i+=1

gngoal3 = ngoal3[0]
gndef3 = (ndef3[1] + ndef3[2] + ndef3[3]) / 4 + ( ndef3[4]+ ndef3[5] + ndef3[6] + ndef3[7] + ndef3[8]) / 8
gnpm3 = (npm3[5] + npm3[6] + npm3[7] + npm3[8] + npm3[4]) / 4 + (npm3[1] + npm3[2] + npm3[3] ) / 8 + (npm3[9] + npm3[
        10]) / 12
gnforw3 = (nforw3[9] + nforw3[10]) / 2 + (nforw3[5] + nforw3[6] + nforw3[7] + nforw3[8]) / 8




#print ('Команда -', nteam3)
#nomer3 = []
#i=0
#j=0
#kolvo = len(sostav3)
#for i in range(kolvo):
 #   nomer3 +=[i+1]
  #  print(nomer3[i], sostav3[i])
   # print('Вратарство -', ngoal3[i])
   # print('Защита -',ndef3[i])
    #print('Полузащита -',npm3[i])
    #print('Нападение -',nforw3[i], '\n')
    #time.sleep(2)
    #i+=1
    #j+=1


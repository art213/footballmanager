import numpy as np
import time

from team2 import *
from team3 import *
from team4 import *
from team5 import *

from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')


gnteam = [nteam5, nteam2, nteam3,nteam4]
gsostav = [sostav5, sostav2, sostav3, sostav4]
gngoal = [gngoal5, gngoal2, gngoal3, gngoal4]
gndef = [gndef5, gndef2, gndef3, gndef4]
gnpm = [gnpm5, gnpm2, gnpm3, gnpm4]
gnforw = [gnforw5, gnforw2, gnforw3, gnforw4]
gnspeed = [nspeed5, nspeed2, nspeed3, nspeed4]
gscore = [0,0,0,0]
gzgoals = [0,0,0,0]
gpgoals = [0,0,0,0]

tours = len (gnteam) - 1

j=0
m=1
k=2
l=3
print ()

for i in range (tours):
    print (Fore.BLUE + 'Тур', i+1)
    print(Style.RESET_ALL)
    kk = k % 4
    ll = 0+1+2+3-m-kk
    print ('Матчи:', gnteam[j],'-', gnteam[m],'и', gnteam[kk],'-',gnteam[ll])


    vladenie = [1, 2]
    minuta = [1, 0]
    flang = ['левому флангу', 'центру', 'правому флангу']
    ataka1 = [1, 0]
    ataka2 = [1, 0]
    udar1 = [0, 1, 2]
    udar2 = [0, 1, 2]
    goal1 = 0
    goal2 = 0

    i = 1

    #text of game
    text1t1 = ['Оборона оставлена не у дел. Сможет ли ' + gsostav[m][0] + ' спасти команду?',
               'С трудом на оборона пройдена',
               'Оборона грамотно защищается. Ни одной лазейки. Ан нет, игрокам команды ' + gnteam[
                   j] + ' удается пройти.',
               'Защита пройдена.', 'Пройти оборону не составляет труда.', 'Лихо пройдены редуты обороны.',
               'Защита противника какая-то сонная. Пройти ее раз плюнуть.',
               'Какая игра диспетчера! Какой пас! Защита противника ничего не может сделать']

    text1t2 = [
        'Оборона грамотно защищается. Ни одной лазейки. Ан нет, игрокам команды ' + gnteam[m] + ' удается пройти.',
        'Оборона оставлена не у дел. Сможет ли ' + gsostav[j][0] + ' спасти команду?',
        'С трудом на оборона пройдена', 'Защита пройдена.',
        'Пройти оборону не составляет труда.', 'Лихо пройдены редуты обороны.',
        'Защита противника какая-то сонная. Пройти ее раз плюнуть.',
        'Какая игра диспетчера! Какой пас! Защита противника ничего не может сделать']

    text2 = ['Удар!.. Мимо', 'Такая атака и такой посредственный удар', 'Удар... Чуть выше ворот',
             'Срезка. Мяч катится мимо ворот',
             'Мощный удар с 17 метров. Мяч чиркает по штанге и уходит за лицевую.',
             'Разве это удар? Мяч летит к угловому флажку',
             'Мощный удар с 17 метров. Перекладина. Мяч отлетает к защитникам.',
             'Какой удар. Чуть-чуть выше ворот']

    text3t1 = ['Удар!... Гол!', 'Точный удар в "девятку". ' + gsostav[m][0] + ' бессилен.',
               'Вот это гол! Мяч по идеальной траектории влетает в ворота.',
               'Какая ошибка вратаря. Мяч влетает в ворота. Ох, не простят ему этот гол.',
               'Мяч летит в нижний угол. Вратарь дотягивается до мяча, но этого оказывается мало. Мяч от штанги влетает в ворота',
               'Удар. Вратарь даже не реагирует. Мяч в сетке',
               'Выход один на один. Вратарь бессилен. Мяч в воротах.',
               'Мяч летит в девятку. ' + gsostav[m][0] + ' прыгает... и...чуть-чуть не дотягивается до мяча. Гол!']

    text3t2 = ['Удар!... Гол!', 'Точный удар в "девятку". ' + gsostav[j][0] + ' бессилен.',
               'Ох! У ' + gsostav[j][0] + ' "дырявые" руки. Как так?',
               'Какая ошибка ' + gsostav[j][0] + '. Мяч влетает в ворота. Ох, не простят ему этот гол.',
               'Мяч летит в нижний угол. ' + gsostav[j][
                   0] + ' дотягивается до мяча, но этого оказывается мало. Мяч от штанги влетает в ворота',
               'Удар. Вратарь даже не реагирует. Мяч в сетке',
               'Выход один на один. Вратарь бессилен. Мяч в воротах.',
               'Мяч летит в девятку. ' + gsostav[j][0] + ' прыгает... и...чуть-чуть не дотягивается до мяча. Гол!']

    text4 = ['Что за удар? Вратарь справляется с ним без проблем.', 'Удар... Кто его учил бить? Дети и то бьют сильнее',
             'Какой мощный удар! Штанга! Мяч отлетает в поле, защитники первыми успевают к мячу.',
             'Мяч летит в девятку. Вратарь прыгает... и спасает команду.',
             'Отличный удар. Вратарь в блестящем прыжке отбивает мяч. На подборе первые защитники. ',
             'С таким ударом справился бы и ребенок. Такую атаку запороли.',
             'Мяч летит в правый угол. Вратарь прыгает... и ловит мяч.',
             'Выход один на один. Вратарь прыгает в ноги и забирает мяч.',
             'Выход один на один... Голкипер спасает команду',
             'Удар. Мяч попадает в штангу, а от нее в руки вратаря. Какая удача.']

    text5 = ['Разве это атака? Оборона справляется с ней без проблем', 'Противник убивает атаку в зародыше',
             'Неточный пас. Мяч у соперника.',
             'Атака заканчивается не начавшись', 'Защита на высоте. Мяч отобран.',
             'Нда. Разве это атака? Мяч у соперника.',
             'Неточный пас. Атаку можно было и не начинать, если раздавать такие пасы.']

    print('Сегодня встречаются команды', gnteam[j],'-', gnteam[m])

#count of segments in match (may be - 15, 30, 45)
    while i <= 30:
        vvladenie = np.random.choice(vladenie, p=[(gnpm[j] / (gnpm[j] + gnpm[m])), (gnpm[m] / (gnpm[j] + gnpm[m]))])
        vminuta = np.random.choice(minuta)
        vflang = np.random.choice(flang, p=[0.3, 0.4, 0.3])
#Determine who has the ball
        if vvladenie == 1:
            vataka1 = np.random.choice(ataka1, p=[(gnforw[j] / (gnforw[j] + gndef[m])),
                                                  1 - (gnforw[j] / (gnforw[j] + gndef[m]))])
#generation of minutes and direction of attack, you can add scoring event (if forward of attack team have speed more than speed of defenders of defending team)
            if vataka1 == 1:
                print(i * 3 - vminuta, 'минута.', gnteam[j], 'начинает атаку по', vflang)
                text1a = np.random.choice(text1t1)
                print(text1a)
                #generation of result, you can add penalty (with chance 0.05-0.1 + realization (2*nforw[j]/(2*nforw[j]+gngoal[m])) - 67 %, if forward skill = goalkeeping skill)
                vudar1 = np.random.choice(udar1,
                                          p=[1 - gnforw[j] * 0.032,
                                             gnforw[j] * 0.032 * gnforw[j] / (gnforw[j] + gngoal[m]),
                                             gnforw[j] * 0.032 * (1 - gnforw[j] / (gnforw[j] + gngoal[m]))])
                time.sleep(5)
                if vudar1 == 0:
                    text2a = np.random.choice(text2)
                    print(text2a)
                    print('***')
                if vudar1 == 1:
                    text3a = np.random.choice(text3t1)
                    print(text3a)
                    goal1 += 1
                    print(Fore.BLUE + 'Счет в матче:', goal1, '-', goal2)
                    #generation of players who scored of goal
                    vgoal1 = np.random.choice(gsostav[j], p=[0, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2])
                    print('Гол забил', vgoal1)
                    print(Style.RESET_ALL)
                    print('***')
                if vudar1 == 2:
                    text4a = np.random.choice(text4)
                    print(text4a)
                    print('***')
            else:
                i += 0
                # text5a = np.random.choice(text5)
                # print(text5a)
        if vvladenie == 2:

            vataka2 = np.random.choice(ataka2, p=[(gnforw[m] / (gnforw[m] + gndef[j])),
                                                  1 - (gnforw[m] / (gnforw[m] + gndef[j]))])
            if vataka2 == 1:
                print(i * 3 - vminuta, 'минута.', gnteam[m], 'начинает атаку по', vflang)
                text1a = np.random.choice(text1t2)
                print(text1a)
                vudar2 = np.random.choice(udar2,
                                          p=[1 - gnforw[m] * 0.032,
                                             gnforw[m] * 0.032 * gnforw[m] / (gnforw[m] + gngoal[j]),
                                             gnforw[m] * 0.032 * (1 - gnforw[m] / (gnforw[m] + gngoal[j]))])
                time.sleep(5)
                if vudar2 == 0:
                    text2a = np.random.choice(text2)
                    print(text2a)
                    print('***')
                if vudar2 == 1:
                    text3a = np.random.choice(text3t2)
                    print(text3a)
                    goal2 += 1
                    print(Fore.MAGENTA + 'Счет в матче:', goal1, '-', goal2)
                    vgoal2 = np.random.choice(gsostav[m], p=[0, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2])
                    print('Гол забил', vgoal2)
                    print(Style.RESET_ALL)
                    print('***')
                if vudar2 == 2:
                    text4a = np.random.choice(text4)
                    print(text4a)
                    print('***')
            if vataka2 == 0:
                i += 0
                # text5a = np.random.choice(text5)
                # print(text5a)

        i += 1

#score
    if goal1 > goal2:
        gscore[j] += 3
    elif goal2 > goal1:
        gscore[m] += 3
    else:
        gscore[m] += 1
        gscore[j] += 1
#goals
    gzgoals[j] += goal1
    gzgoals[m] += goal2
    gpgoals[j] += goal2
    gpgoals[m] += goal1

    print(Fore.BLUE + 'Итоговый счет матча:', gnteam[j], '-', gnteam[m], '-', goal1, '-', goal2, '\n')
    print(Style.RESET_ALL)
    time.sleep(2)

    goal1 = 0
    goal2 = 0

    i = 1

    # атака первой команды
    text1t1 = ['Оборона оставлена не у дел. Сможет ли ' + gsostav[ll][0] + ' спасти команду?',
               'С трудом на оборона пройдена',
               'Оборона грамотно защищается. Ни одной лазейки. Ан нет, игрокам команды ' + gnteam[
                   kk] + ' удается пройти.',
               'Защита пройдена.', 'Пройти оборону не составляет труда.', 'Лихо пройдены редуты обороны.',
               'Защита противника какая-то сонная. Пройти ее раз плюнуть.',
               'Какая игра диспетчера! Какой пас! Защита противника ничего не может сделать']

    text1t2 = [
        'Оборона грамотно защищается. Ни одной лазейки. Ан нет, игрокам команды ' + gnteam[ll] + ' удается пройти.',
        'Оборона оставлена не у дел. Сможет ли ' + gsostav[kk][0] + ' спасти команду?',
        'С трудом на оборона пройдена', 'Защита пройдена.',
        'Пройти оборону не составляет труда.', 'Лихо пройдены редуты обороны.',
        'Защита противника какая-то сонная. Пройти ее раз плюнуть.',
        'Какая игра диспетчера! Какой пас! Защита противника ничего не может сделать']

    text2 = ['Удар!.. Мимо', 'Такая атака и такой посредственный удар', 'Удар... Чуть выше ворот',
             'Срезка. Мяч катится мимо ворот',
             'Мощный удар с 17 метров. Мяч чиркает по штанге и уходит за лицевую.',
             'Разве это удар? Мяч летит к угловому флажку',
             'Мощный удар с 17 метров. Перекладина. Мяч отлетает к защитникам.',
             'Какой удар. Чуть-чуть выше ворот']

    text3t1 = ['Удар!... Гол!', 'Точный удар в "девятку". ' + gsostav[ll][0] + ' бессилен.',
               'Вот это гол! Мяч по идеальной траектории влетает в ворота.',
               'Какая ошибка вратаря. Мяч влетает в ворота. Ох, не простят ему этот гол.',
               'Мяч летит в нижний угол. Вратарь дотягивается до мяча, но этого оказывается мало. Мяч от штанги влетает в ворота',
               'Удар. Вратарь даже не реагирует. Мяч в сетке',
               'Выход один на один. Вратарь бессилен. Мяч в воротах.',
               'Мяч летит в девятку. ' + gsostav[ll][0] + ' прыгает... и...чуть-чуть не дотягивается до мяча. Гол!']

    text3t2 = ['Удар!... Гол!', 'Точный удар в "девятку". ' + gsostav[kk][0] + ' бессилен.',
               'Ох! У ' + gsostav[kk][0] + ' "дырявые" руки. Как так?',
               'Какая ошибка ' + gsostav[kk][0] + '. Мяч влетает в ворота. Ох, не простят ему этот гол.',
               'Мяч летит в нижний угол. ' + gsostav[kk][
                   0] + ' дотягивается до мяча, но этого оказывается мало. Мяч от штанги влетает в ворота',
               'Удар. Вратарь даже не реагирует. Мяч в сетке',
               'Выход один на один. Вратарь бессилен. Мяч в воротах.',
               'Мяч летит в девятку. ' + gsostav[kk][0] + ' прыгает... и...чуть-чуть не дотягивается до мяча. Гол!']

    text4 = ['Что за удар? Вратарь справляется с ним без проблем.', 'Удар... Кто его учил бить? Дети и то бьют сильнее',
             'Какой мощный удар! Штанга! Мяч отлетает в поле, защитники первыми успевают к мячу.',
             'Мяч летит в девятку. Вратарь прыгает... и спасает команду.',
             'Отличный удар. Вратарь в блестящем прыжке отбивает мяч. На подборе первые защитники. ',
             'С таким ударом справился бы и ребенок. Такую атаку запороли.',
             'Мяч летит в правый угол. Вратарь прыгает... и ловит мяч.',
             'Выход один на один. Вратарь прыгает в ноги и забирает мяч.',
             'Выход один на один... Голкипер спасает команду',
             'Удар. Мяч попадает в штангу, а от нее в руки вратаря. Какая удача.']

    text5 = ['Разве это атака? Оборона справляется с ней без проблем', 'Противник убивает атаку в зародыше',
             'Неточный пас. Мяч у соперника.',
             'Атака заканчивается не начавшись', 'Защита на высоте. Мяч отобран.',
             'Нда. Разве это атака? Мяч у соперника.',
             'Неточный пас. Атаку можно было и не начинать, если раздавать такие пасы.']

    print('Сегодня встречаются команды', gnteam[kk], '-', gnteam[ll])

    while i <= 30:
        vvladenie = np.random.choice(vladenie,
                                     p=[(gnpm[kk] / (gnpm[kk] + gnpm[ll])), (gnpm[ll] / (gnpm[kk] + gnpm[ll]))])
        vminuta = np.random.choice(minuta)
        vflang = np.random.choice(flang, p=[0.3, 0.4, 0.3])

        if vvladenie == 1:
            vataka1 = np.random.choice(ataka1, p=[(gnforw[kk] / (gnforw[kk] + gndef[ll])),
                                                  1 - (gnforw[kk] / (gnforw[kk] + gndef[ll]))])
            if vataka1 == 1:
                print(i * 3 - vminuta, 'минута.', gnteam[kk], 'начинает атаку по', vflang)
                text1a = np.random.choice(text1t1)
                print(text1a)
                vudar1 = np.random.choice(udar1,
                                          p=[1 - gnforw[kk] * 0.032,
                                             gnforw[kk] * 0.032 * gnforw[kk] / (gnforw[kk] + gngoal[ll]),
                                             gnforw[kk] * 0.032 * (1 - gnforw[kk] / (gnforw[kk] + gngoal[ll]))])
                time.sleep(1)
                if vudar1 == 0:
                    text2a = np.random.choice(text2)
                    print(text2a)
                    print('***')
                if vudar1 == 1:
                    text3a = np.random.choice(text3t1)
                    print(text3a)
                    goal1 += 1
                    print(Fore.BLUE + 'Счет в матче:', goal1, '-', goal2)
                    vgoal1 = np.random.choice(gsostav[kk], p=[0, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2])
                    print('Гол забил', vgoal1)
                    print(Style.RESET_ALL)
                    print('***')
                if vudar1 == 2:
                    text4a = np.random.choice(text4)
                    print(text4a)
                    print('***')
            else:
                i += 0
                # text5a = np.random.choice(text5)
                # print(text5a)
        if vvladenie == 2:

            vataka2 = np.random.choice(ataka2, p=[(gnforw[ll] / (gnforw[ll] + gndef[kk])),
                                                  1 - (gnforw[ll] / (gnforw[ll] + gndef[kk]))])
            if vataka2 == 1:
                print(i * 3 - vminuta, 'минута.', gnteam[ll], 'начинает атаку по', vflang)
                text1a = np.random.choice(text1t2)
                print(text1a)
                vudar2 = np.random.choice(udar2,
                                          p=[1 - gnforw[ll] * 0.032,
                                             gnforw[ll] * 0.032 * gnforw[ll] / (gnforw[ll] + gngoal[kk]),
                                             gnforw[ll] * 0.032 * (1 - gnforw[ll] / (gnforw[ll] + gngoal[kk]))])
                time.sleep(1)
                if vudar2 == 0:
                    text2a = np.random.choice(text2)
                    print(text2a)
                    print('***')
                if vudar2 == 1:
                    text3a = np.random.choice(text3t2)
                    print(text3a)
                    goal2 += 1
                    print(Fore.MAGENTA + 'Счет в матче:', goal1, '-', goal2)
                    vgoal2 = np.random.choice(gsostav[ll], p=[0, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2])
                    print('Гол забил', vgoal2)
                    print(Style.RESET_ALL)
                    print('***')
                if vudar2 == 2:
                    text4a = np.random.choice(text4)
                    print(text4a)
                    print('***')
            if vataka2 == 0:
                i += 0
                # text5a = np.random.choice(text5)
                # print(text5a)

        i += 1

    if goal1 > goal2:
        gscore[kk] += 3
    elif goal2 > goal1:
        gscore[ll] += 3
    else:
        gscore[ll] += 1
        gscore[kk] += 1

    gzgoals[kk] += goal1
    gzgoals[ll] += goal2
    gpgoals[kk] += goal2
    gpgoals[ll] += goal1

    print(Fore.BLUE + 'Матч окончен. Итоговый счет', goal1, '-', goal2, '\n')
    print(Style.RESET_ALL)

    m += 1
    k += 1
    l += 1
    kk = k % 4
    if kk == j:
        k += 1

print(Fore.BLUE + 'Итоговая таблица:')
print(Style.RESET_ALL)
print('Команда', '\t', '\t', 'Очки', '\t', 'Разница')
i = 0
for i in range(len(gnteam)):
    if len(gnteam[i]) < 7:
        print(gnteam[i], '\t', '\t', '\t', gscore[i], '\t','\t', gzgoals[i], '-', gpgoals[i])
    elif len(gnteam[i]) > 10:
        print(gnteam[i], '\t', gscore[i], '\t','\t', gzgoals[i], '-', gpgoals[i])
    else:
        print(gnteam[i], '\t', '\t', gscore[i], '\t','\t', gzgoals[i], '-', gpgoals[i])

    i += 1







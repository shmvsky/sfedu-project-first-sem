from playsound import playsound
from datetime import datetime
from threading import Thread
import time
from os import path as Path
from os import getcwd

def printt():
    print('Будильник отложен на минуту')

def choose(par = ''):
    if par == '':
        print('Поставить собственную мелодию или проигрывать мелодию по умолчанию? (enter - по умолчанию)\(укажите путь до милодии)')
        path = input()
        if path != '':
            if len(path) > 3 and path[len(path) - 4:len(path)] == '.mp3':
                if Path.isfile(path):
                    return path
                else:
                    return choose(' ')
            else:
                print('Некорректный файл')
                return choose()
        else:
            return path
    else:
        print('Неверно указан путь к файлу')
        return choose()
    
def play(alarmWd,alarmHour,alarmMin,alarmSec,path):
    now = datetime.now()
    currentHour = now.hour
    currentMin = now.minute
    currentSec = now.second
    currentWday = now.weekday()
    if currentWday != alarmWd:
        if (alarmMin + 1) // 60 == 0:
            printt()
            return alarmClock(currentWday,currentHour,currentMin + 1,currentSec,path)
        elif (alarmMin + 1) // 60 == 1 and alarmHour != 23:
            return alarmClock(currentWday,currentHour + 1,(currentMin + 1) % 60,currentSec,path)
        elif (alarmMin + 1) // 60 == 1:
            printt()
            return alarmClock(currentWday + 1 if currentWday != 6 else 0,0,(currentMin + 1) % 60,currentSec,path)
    elif currentHour > alarmHour:
        if (alarmMin + 1) // 60 == 0:
            printt()
            return alarmClock(currentWday,currentHour,currentMin + 1,currentSec,path)
        elif (alarmMin + 1) // 60 == 1 and alarmHour != 23:
            printt()
            return alarmClock(currentWday,currentHour + 1,(currentMin + 1) % 60,currentSec,path)
        elif (alarmMin + 1) // 60 == 1:
            printt()
            return alarmClock(currentWday + 1 if currentWday != 6 else 0,0,(currentMin + 1) % 60,currentSec,path)
    elif currentMin > alarmMin and currentHour >= alarmHour:
        if (alarmMin + 1) // 60 == 0:
            printt()
            return alarmClock(currentWday,currentHour,currentMin + 1,currentSec,path)
        elif (alarmMin + 1) // 60 == 1 and alarmHour != 23:
            printt()
            return alarmClock(currentWday,currentHour + 1,(currentMin + 1) % 60,currentSec,path)
        elif (alarmMin + 1) // 60 == 1:
            printt()
            return alarmClock(currentWday + 1 if currentWday != 6 else 0,0,(currentMin + 1) % 60,currentSec,path)
    elif currentMin >= alarmMin and currentHour >= alarmHour and currentSec >= alarmSec:
        if (alarmMin + 1) // 60 == 0:
            printt()
            return alarmClock(currentWday,currentHour,currentMin + 1,currentSec,path)
        elif (alarmMin + 1) // 60 == 1 and alarmHour != 23:
            printt()
            return alarmClock(currentWday,currentHour + 1,(currentMin + 1) % 60,currentSec,path)
        elif (alarmMin + 1) // 60 == 1:
            printt()
            return alarmClock(currentWday + 1 if currentWday != 6 else 0,0,(currentMin + 1) % 60,currentSec,path)
    else: 
        if path == '':
            playsound(getcwd() + '\\petit_poney.mp3')
            play(alarmWd,alarmHour,alarmMin,alarmSec,'')
        else:
            playsound(path)
            play(alarmWd,alarmHour,alarmMin,alarmSec,path)
        
def alarmClock(alarmWd,alarmHour,alarmMin,alarmSec,path):
    while True:
        now = datetime.now()
        currentHour = now.hour
        currentMin = now.minute
        currentSec = now.second
        currentWd = now.weekday()
        if alarmWd == currentWd:
            if alarmHour == currentHour:
                if alarmMin == currentMin:
                    if alarmSec == currentSec:
                        print('Время пришло')
                        if (alarmMin + 1) // 60 == 0:
                            return play(alarmWd,alarmHour,alarmMin + 1,alarmSec,path)
                        elif (alarmMin + 1) // 60 == 1 and alarmHour != 23:
                            return play(alarmWd,alarmHour + 1,(alarmMin + 1) % 60,alarmSec,path)
                        elif (alarmMin + 1) // 60 == 1:
                            return play(alarmWd + 1 if alarmWd != 6 else 0,0,(alarmMin + 1) % 60,alarmSec,path)
                        break

            
def validateTime(alarmTime):
    weekd = ['mo','tu','we','th','fr','sa','su']
    if len(alarmTime) != 11:
        return 'Неверный формат'
    else:
        if alarmTime[2] != ':' or alarmTime[5] != ':' or alarmTime[8] != ':':
            return 'Неверно расставлены разделители \':\''
        elif not(alarmTime[0:2].lower() in weekd):
            return 'Неверный формат дня недели'
        if int(alarmTime[3:5]) > 23:
            return 'Неверный формат часов'
        elif int(alarmTime[6:8]) > 59:
            return 'Неверный формат минут'
        elif int(alarmTime[9:11]) > 59:
            return 'Неверный формат секунд'
        else:
            return 'True!'

print('Дни недели:\nПонедельник - mo\nВторник - tu\nСреда - we\nЧетверг - th\nПятница - fr\nСуббота - sa\nВоскресенье - su\n')

path = choose()

while True:
    alarmTime = input('Введите время в формате \'DW:HH:MM:SS\': ')
    if validateTime(alarmTime) != 'True!':
        print(validateTime(alarmTime))
    else:
        print('Будильник установлен на %s' % alarmTime)
        break
alarmWd = alarmTime[0:2]
alarmHour = int(alarmTime[3:5])
alarmMin = int(alarmTime[6:8])
alarmSec = int(alarmTime[9:11])
weekd = {'mo': 0,'tu' : 1,'we' : 2,'th' : 3,'fr' : 4,'sa' : 5,'su' : 6}
alarmClock(weekd[alarmWd.lower()],alarmHour,alarmMin,alarmSec,path)
import time
from playsound import playsound


def countdown(user_time):
   while user_time >= 0:
       mins, secs = divmod(user_time, 60)
       timer = '{:02d}:{:02d}'.format(mins, secs)
       print(timer, end='\r')
       time.sleep(1)
       user_time -= 1
   print('Lift off!')
   playsound("D:\Codes\projects\alarm clock\alarm.mp3")
   time.sleep(5)

CLEAR = "\33[2j" #clear the whole terminal
CLEAR_AND_RETURN = "\033[h" #cleat the line to reprint (also done by \r)

def alarm(sec):
   time_elapsed = 0

   print(CLEAR)
   while time_elapsed < sec:
      time_elapsed += 1

      time_left = sec - time_elapsed
      minutes_left = time_elapsed//60
      seconds_left = time_left % 60

      #print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
      # can also be done by just doing ' end = "\r" '

      #:02d format it to have 0 before the numbers
      print(f"{minutes_left:02d}:{seconds_left:02d}",end="\r")
      time.sleep(1)
      
   print('Alarm Ring!')
   playsound("D:/Codes/projects/alarm clock/alarm.mp3")
   
      

min = int(input("Minutes : "))
sec = int(input("Seconds : "))
total_sec = min *60 + sec
alarm(total_sec)
import datetime
import random

def get_student_id():

    ctime = datetime.datetime.now()
    mtime = str(ctime.today())
    newtime = ''.join(ch for ch in mtime if ch.isalnum())
    year = newtime[0:4]
    month_day = newtime[5:14]
   
    my_id = f'Tech/{year}/{str(month_day)}/Arena'
 
    return my_id


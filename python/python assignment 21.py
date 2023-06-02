1 List the files in your current directory
Ans – import os
	New_list = os.listdir()
list(New_list)

2  Create a list of all of the files in your parent directory (minimum five files should be available).
Ans – directory_list = os.listdir('D:/python assignment')

3.  Use multiprocessing to create three separate processes. Make each one wait a random number of
seconds between one and five, print the current time, and then exit.
Ans - def wait_time():
    TIME  = time.localtime()
    CURR_TIME= time.strftime('%H:%M:%S',TIME)
    print(CURR_TIME)
    time.sleep(random.randint(1,5))
    TIME  = time.localtime()
    CURR_TIME= time.strftime('%H:%M:%S',TIME)
    print(CURR_TIME)
    time.sleep(random.randint(1,5))
    TIME  = time.localtime()
    CURR_TIME= time.strftime('%H:%M:%S',TIME)
    print(CURR_TIME)
    
print(wait_time())

4. Create a date object of your day of birth.
Ans 4 - import datetime as dt
Birth_date = dt.datetime(2000, 3,23).date()



5. What day of the week was your day of birth?
Ans -  import datetime as dt
	Week_day = dt.datetime(2000, 3,23).date().strftime('%w')
int(Week_day)

6. When will you be (or when were you) 10,000 days old?
Ans 6 – 
import datetime as dt
a = dt.datetime(1990, 3,23).date()
born_year = a.year
current_year = dt.datetime.now().year
diff_curr_born = current_year - born_year
cal_year = 10000/365


diff_cal_born = cal_year - diff_curr_born
if diff_cal_born > 0:
    print(f'in {round(diff_cal_born,2)} years i"ll be 10000 days old')
else:
    print(f'im already 10000 days old on {round(-1 * diff_cal_born,2)} years ago')




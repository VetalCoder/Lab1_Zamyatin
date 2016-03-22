import datetime

def get_Date():
    # input date
    while True:
        try:
            year = int(input('Enter date (year): '))
            month = int(input('Enter date (month):'))
            day = int(input('Enter date (day):'))
			#check date
            tmp = datetime.date(year, month, day)           
        except ValueError:
            print('Values is not correct. Try again.')
            continue
        return tmp

def get_temp():
    #input temperature
    while True:
        try:
            tmp = int(input('Enter Temperature (eg. +8): '))
        #check temperature
		except ValueError:                                  
            print('Values is not correct. Try again.')
            continue
        return tmp

def get_humidity():
    #input humidity
    while True:
        try:
            tmp = int(input('Enter humidity (%): '))
        #check humidity
		except ValueError:                                  
            print('Values is not correct. Try again.')
            continue
        if 0<=tmp<=100: 
			return tmp
        else: 
			print('Values is not correct. Try again.')

def get_preasure():
    #input preasure
    while True:
        try:
            tmp = int(input('Enter preasure (mm): '))
        #check preasure
		except ValueError:                              
            print('Values is not correct. Try again.')
            continue
		if tmp >=0 :
			return tmp
		else:
			print('Values is not correct. Try again.')
		

def get_wspeed():
    #input wind speed
    while True:
        try:
            tmp = float(input('Enter wind speed (m/sec): '))
        #check wind speed
		except ValueError:                              
            print('Values is not correct. Try again.')
            continue
		if tmp >= 0:
			return tmp	
		else: 
			print('Values is not correct. Try again.')
        

def get_year():
    while True:
        try:
            tmp = int(input('Enter year: '))
        except ValueError:
            print('Values is not correct. Try again.')
            continue
        if 0<=tmp<=2016: 
			return tmp
        else: 
			print('Values is not correct. Try again.')

def get_month():
    while True:
        try:
            tmp = int(input('Enter month: '))
        except ValueError:
            print('Values is not correct. Try again.')
            continue
        if 1<=tmp<=12: 
			return tmp
        else: 
			print('Values is not correct. Try again.')

def get_choice():
    while True:
        try:
            tmp = int(input())
        except ValueError:
            print('Choice is not correct. Try again.')
            continue
        return tmp
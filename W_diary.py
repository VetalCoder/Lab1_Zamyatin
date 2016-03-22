import datetime
import Open_file
import Input

weather = {}

def push_data():

    d1 = datetime.date(2015, 10, 10)
    d2 = datetime.date(2015, 10, 12)
    tmp = {d1:['+10', 750, 48, 3.0, 'W', 'None'],
           d2:['+8', 747, 53, 3.3, 'SW', 'None']}
    weather.update(tmp)


def add_data():
#add data to our weather diary#
    date = Input.get_Date()
    temp = Input.get_temp()
    preasure = Input.get_preasure()
    humidity = Input.get_humidity()
    wspeed = Input.get_wspeed()
    wdirect = input('Enter wind direction (eg. SW or S): ')
    prec = input('Enter precipitations (eg. Rain or Snow): ')
    tmp = {date:[temp, preasure, humidity, wspeed, wdirect, prec]}
	#rewrite data that already exsist
    weather.update(tmp) 
	#save changes in file
    Open_file.save_data(weather)                               
    tmp = input('Adding/Editing Successful. Press Enter to continue...')


def rm_data():
# remove data from our diary
    date = Input.get_Date()
    if date in weather:
        del weather[date]
		#save changes in file
        Open_file.save_data(weather)            
        tmp = input('Removing Successful. Press Enter to continue...')
    else:
        tmp = input('Day in diary not found. Press Enter to continue...')

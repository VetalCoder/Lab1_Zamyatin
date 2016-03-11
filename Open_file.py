import pickle

def open_data(obj):
#load data from file
    with open('weather.pickle','rb') as weatherFile:
        tmp = {}
        try: tmp = pickle.load(weatherFile)
        except FileNotFoundError:pass
        obj.update(tmp)

def save_data(obj):
    with open('weather.pickle', 'wb') as weatherFile:       #open file with data
        pickle.dump(obj, weatherFile)                       #save data
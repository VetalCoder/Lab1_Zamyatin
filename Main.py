import Menu
import Open_file
import W_diary

def main ():
    Open_file.open_data(W_diary.weather)        #load data from file
    Menu.print_menu()                           #run menu

main()


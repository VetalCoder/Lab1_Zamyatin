import Menu
import Open_file
import W_diary

def main ():
 #load data from file
	Open_file.open_data(W_diary.weather)        
 #run menu
	Menu.print_menu()                          

main()


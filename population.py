# Lesa skráarnafn frá notanda
# Lesið tiltekið ár frá notenda
# Opna skrá
# Meðhöndla skrá
# prenta út Minimum: (population, state)
# prenta út Maximum: (population, state)
	
def read_filename():
	name = input("Enter filename: ")
	return name

def read_year():
	while True:
		year = int(input("Enter year: "))
		if year == 1950 or year == 1960 or year == 1970 or year == 1980 or year == 1990:
			return year 
		else:
			print("Invalid year.")

def open_file(filename):
	try:
		file_object = open(filename, "r")
		return file_object
	except:
		print("Filename {} not found!".format(filename))
	
def process_file(file, y):
	
	
def print_results():
	pass
	
def main():
	filename = read_filename()
	
	file_object = open_file(filename)

	if file_object:
		year = read_year()
		
		process_file(file_object, year)
		
		print_results()	

main()

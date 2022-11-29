# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = convert_distance(55)
print(my_trip_miles)



def format_name(first_name, last_name):
	# code goes here
	if first_name== '' and last_name=='':
		string=""
		
	elif last_name == "":
		string = "Name: "+first_name
	elif first_name=="":
		string = "Name: "+last_name
	else:
		string = "Name: "+last_name+", "+first_name
	
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
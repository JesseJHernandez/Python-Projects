def f_c (temp):

	celsius = (temp - 32) * 5/9
	
	return celsius
    
def c_f (temp):

        fahren = (temp * 9/5) + 32

        return fahren
    
def main():
    
    user_input = raw_input("What temperature would you like converted? ")

    input_split = user_input.split() 

    num = int(input_split[0])
    temp_type = input_split[1]

    if temp_type.lower() in ["celsius" , "c"]:
        print "The temperature in fahrenheit is %.2f" % c_f(num)
    
    elif temp_type.lower() in ["fahrenheit" , "f"]:
        print "The temperature in celsius is %.2f" % f_c(num)
        
    else:
        print "Your input is invalid, let Rocio tutor you! "
    
main()
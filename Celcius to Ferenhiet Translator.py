print("Celcius To Ferenhiet or Vice-versa Conversion System")
print("Developed By Sudip Mitra")
print("E-mail : sudipmitraonline@gmail.com")
print("")

def c_to_f_translator(value) :
    #Celcius to Ferenhiet Conversion Function
    farenhiet_conversion = ( (value * 9) / 5 ) + 32
    return farenhiet_conversion

def f_to_c_translator(value) :
    #Ferenhiet to Celcius Conversion Function
    celcius_conversion = ( ( value - 32 ) * 5 ) / 9
    return celcius_conversion

#Choice for User Preference
print("Enter a choice : \n ' 1 ' for Celcius to Ferenhiet Conversion. \n ' 2 ' for Ferenhiet to Celcius Conversion.")
user_input = int(input())

if(user_input == 1):
    print("Enter the Celcius Temperature to convert :")
    user_input1 = int(input())
    print("Converted Ferenhiet Temperature is : " ,c_to_f_translator(user_input1))

elif(user_input == 2):
    print("Enter the Ferenhiet Temperature to convert :")
    user_input1 = int(input())
    print("Converted Celcius Temperature is : ",f_to_c_translator(user_input1))

else :
    print("Wrong Choice. Process Abandoned. Please Try Again.")

input()


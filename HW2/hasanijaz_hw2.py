#Hasan Ijaz#Jee oye #Code ho gaya 
#Taking inputs and displaying welcome message
print("Welcome to Online Car Rental Service")
name=input("Please enter your name: ")
v_seg=input(name +","+ " please enter the segment of the vehicle: ")
n_day=int(input(name+","+" please enter the number of rental days: "))
gear=input(name+","+" please enter the gear type: ")
fuel=input(name+","+" please enter the fuel type: ")
#Initializing values
econ=250
com=400
pres=600
prem=750
lux=1150
auto=150
man=50
pet=100
die=200
#checking conditions and calculating value if all are met else outputing errors
if v_seg == "Economic" or v_seg == "Comfort" or v_seg == "Prestige" or v_seg == "Premium" or v_seg =="Luxury":
     if n_day > 0 :
         if gear=="Automatic" or gear== "Manual":
             if fuel=="Petrol" or fuel=="Diesel":
                 if   v_seg=="Economic" and gear=="Automatic" and fuel=="Petrol":
                        ch=(n_day)*(econ+auto+pet)
                 elif v_seg=="Economic" and gear=="Automatic" and fuel=="Diesel":
                        ch=(n_day)*(econ+auto+die)
                 elif v_seg=="Economic" and gear=="Manual" and fuel=="Diesel":
                        ch=(n_day)*(econ+man+die)
                 elif v_seg=="Economic" and gear=="Manual" and fuel=="Petrol":
                            ch=(n_day)*(econ+auto+pet)
                 elif v_seg=="Comfort" and gear=="Automatic" and fuel=="Petrol":
                            ch=(n_day)*(com+auto+pet)
                 elif v_seg=="Comfort" and gear=="Automatic" and fuel=="Diesel":
                            ch=(n_day)*(com+auto+die)
                 elif v_seg=="Comfort" and gear=="Manual" and fuel=="Diesel":
                            ch=(n_day)*(com+man+die)
                 elif v_seg=="Comfort" and gear=="Manual" and fuel=="Petrol":
                            ch=(n_day)*(com+man+pet)
                 elif v_seg=="Prestige" and gear=="Automatic" and fuel=="Petrol":
                            ch=(n_day)*(pres+auto+pet)
                 elif v_seg=="Prestige" and gear=="Automatic" and fuel=="Diesel":
                            ch=(n_day)*(pres+auto+die)
                 elif v_seg=="Prestige" and gear=="Manual" and fuel=="Diesel":
                            ch=(n_day)*(pres+auto+die)
                 elif v_seg=="Prestige" and gear=="Manual" and fuel=="Petrol":
                            ch=(n_day)*(pres+auto+pet)
                 elif v_seg=="Premium" and gear=="Automatic" and fuel=="Petrol":
                            ch=(n_day)*(prem+auto+pet)
                 elif v_seg=="Premium" and gear=="Automatic" and fuel=="Diesel":
                            ch=(n_day)*(prem+auto+die)
                 elif v_seg=="Premium" and gear=="Manual" and fuel=="Diesel":
                            ch=(n_day)*(prem+man+die)
                 elif v_seg=="Premium" and gear=="Manual" and fuel=="Petrol":
                            ch=(n_day)*(prem+man+pet)
                 elif v_seg=="Luxurt" and gear=="Automatic" and fuel=="Petrol":
                            ch=(n_day)*(lux+auto+pet)
                 elif v_seg=="Luxurt" and gear=="Automatic" and fuel=="Diesel":
                            ch=(n_day)*(lux+auto+die)
                 elif v_seg=="Luxurt" and gear=="Manual" and fuel=="Diesel":
                            ch=(n_day)*(lux+man+die)
                 elif v_seg=="Luxurt" and gear=="Manual" and fuel=="Petrol":
                            ch=(n_day)*(lux+man+pet)
                 print(name+",",ch,"TL is charged for your vehicle rental.")
             else:
                 print("Incorrect fuel type!")
         else:
            print("Incorrect gear type!")
     else:
        print("Icorrect number of rental days!")
else:
    print("Incorrect vehicle segment!")

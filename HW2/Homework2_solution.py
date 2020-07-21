# display introductory information
print("This program bla bla bla...")
print("")   # empty line

# initializations
economic, comfort, prestige, premium, luxury = 250, 400, 600, 750, 1150
automatic, manuel = 150, 50
petrol, diesel = 100, 200

# prompt for the inputs
name = input("Please enter your name: ")
segment = input(name + ", please enter the segment of the vehicle: ")
days = int(input(name + ", please enter the number of rental days: "))
gear = input(name + ", please enter the gear type: ")
fuel = input(name + ", please enter the fuel type: ")

print("")   # empty line

# input check
if segment != "Economic" and segment != "Premium" and segment != "Comfort" \
   and segment != "Prestige" and segment != "Luxury":
    print("Incorrect vehicle segment!")
elif days <= 0:
    print("Incorrect number of rental days!")
elif gear != "Automatic" and gear != "Manuel":
    print("Incorrect gear type!")
elif fuel != "Petrol" and fuel != "Diesel":
    print("Incorrect fuel type!")
else:
    # calculate the charge
    if segment == "Economic":
        segment_charge = economic
    elif segment == "Premium":
        segment_charge = premium
    elif segment == "Comfort":
        segment_charge = comfort
    elif segment == "Prestige":
        segment_charge = prestige
    else:
        segment_charge = luxury
        
    if gear == "Automatic":
        gear_charge = automatic
    else:
        gear_charge = manuel
        
    if fuel == "Petrol":
        fuel_charge = petrol
    else:
        fuel_charge = diesel
        
    bill = days * (segment_charge + gear_charge + fuel_charge)

    # display the output
    print(name, ", ", bill, " TL is charged for your vehicle rental.", sep="")

    

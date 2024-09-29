import math

# Get our variables
width = float(input("What is the width of the tire in millimenters?\n> "))
aspectRatio = float(input("What is the aspect ratio of the tire?\n> "))
diameter = float(input("What is the diameter of the tire in inches?\n> "))

# Now we do the math
volume = float(((math.pi * (width**2) * aspectRatio * (width * aspectRatio + 2540 * diameter)) / 10000000000))

print(f"The volume of this tire is roughly: {volume:.2f} liters")

# Import datetime to time stamp volume in volume.txt
import datetime

buyTires = input("Would you like to buy tires that have the same dimensions you have specified? Yes or no?\n> ")
if buyTires.lower() == "yes":
    confirmation = input("You seem to have said 'yes'. Is this correct?\n> ")
    
    if confirmation.lower() == "yes":
        number = input("Please type out your number, and we will get in contact with you to continue your purchase.\n> ")
        # Store the tire width, aspect ratio, diameter, and volume, along with the client's number
        currentDate = datetime.datetime.now()
        # Open volume.txt, and append it
        with open("volume.txt", "at") as volumeFile:
        # Print the date and the associated tire volume
            print(f"{currentDate:%Y-%m-%d}: width - {width:.2f}, aspect ratio - {aspectRatio:.2f}, diameter - {diameter:.2f}, volume - {volume:.2f}, client's number - {number}", file=volumeFile)
            print("Your number and specifications have been saved. We will reach out to you at the earliest convenience.")
else:
    currentDate = datetime.datetime.now()
    # Even without a sale, record the data to use for research purposes
    with open("volume.txt", "at") as volumeFile:
        print(f"{currentDate:%Y-%m-%d}: width - {width:.2f}, aspect ratio - {aspectRatio:.2f}, diameter - {diameter:.2f}, volume - {volume:.2f}", file=volumeFile)
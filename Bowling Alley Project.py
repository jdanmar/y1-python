from rich import print # pip install colorama before running
from time import sleep
from random import randint
totalBooks = []
def bowlingbooking():
    try:
        global bookingAmount
        bookingAmount = int(input("How many people are booking? "))
        for i in range(bookingAmount):
            bookerName = input("Name: ")
            bookerAge = int(input("Age: "))

            totalBooks.append({
                "Name:": bookerName,
                "Age:": bookerAge
            })
        print("Logging..")
        sleep(4)
        print("Booking(s) logged successfully!")
        sleep(2)
        print(f"Please go to lane: {randint(1,5)} when ready!\nThank you for booking at [bold violet]StrikeZone Bowling & Café![/bold violet]")
        sleep(2)
        return totalBooks
    except ValueError:
        print("Incorrect value. Please retry")
        bowlingbooking()

def bowlingcafe():
    print("[green]Welcome to the StrikeZone Café![/bold green]")
    cafedecision = int(input("What would you like to do?\n[1] Exit\n> "))
#    if cafedecision == 1:
#       menuitems = ["Drinks:"["Water - £2.50","CocaCola - £3.75","Fanta - £3","Sprite - £3","Pepsi - £3","Dr Pepper - £3"],
#                     "Food:"["Burger & Fries - £12.50","Chicken Nuggets - £7.50","Wrap - £9"]]
    if cafedecision == 1:
        print("Thank you for visiting the [green]StrikeZone Café![/bold green]")
        sleep(2.5)
        bowlingalley()

def customersummary():
    totalprice = 12.50*bookingAmount + 0.00
    print("Calculating final information...")
    sleep(5)
    print(f"[bold red]Customer Summary:[/bold red]\n"
          f"[italics yellow]Total Price(£):{totalprice}[italics yellow]\n\n"
          f"[italics red]Booking information:[/italics red]\n")
    for person in totalBooks:
        print(person)
    sleep(3)
    bowlingalley()

def bowlingalley():
    v = True
    while v:
        try:
            print("[bold violet]Welcome to\nStrikeZone Bowling & Café![/bold violet]")
            decision = int(input("Please select what you'd like to do:\n[1] Book\n[2] View the Café\n[3] Display Customer Summary\n[4] Exit\n> "))
            if decision == 1:
                print("Loading..")
                sleep(2)
                bowlingbooking()
            elif decision == 2:
                print("Loading..")
                sleep(2)
                bowlingcafe()
            elif decision == 3:
                print("Loading..")
                sleep(2)
                customersummary()
            elif decision == 4:
                print("[red]Thanks for visiting![/red]")
                v = False
                break
        except ValueError:
            print("Incorrect value, please retry.")
            bowlingalley()

bowlingalley()

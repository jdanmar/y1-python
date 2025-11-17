arcade = {
    "Pinball Wizard": {"Category":"Pinball","Status":"Working"},
    "Retro Racer": {"Category": "Racing", "Status": "Needs Service"}
}
def arcademachines():
    decision = int(input("Would you like to:\n[1]View all machines\n[2]Add a new machine\n[3]Update a machine's status\n[4]Delete a machine entry\n[6]Exit\n"))
    if decision == 1:
        print(arcade)
arcademachines()

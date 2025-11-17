energy = []
usernames = []
steps = []

change = int(input("What list do you want to update:\n[1] Energy Levels\n[2] Usernames\n[3] Step Count\n[4] Quit\n"))
if change == 1:
    energychange = int(input("Enter value: "))
    energy.append(energychange)
elif change == 2:
    usernamechange = int(input("Enter value: "))
    usernames.append(usernamechange)
elif change == 3:
    stepschange = int(input("Enter value: "))
    steps.append(stepschange)
elif change == 4:
    print("Stepcount:")
    print(steps)
    print(steps[0],steps[-1])
    print("Usernames:")
    print(usernames)
    print(usernames[0],usernames[-1])
    print("Energy:")
    print(energy)
    print(energy[0],energy[-1])
else:
    print("Incorrect value")
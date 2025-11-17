def notifsoftware():
    notifications = [34,28,55,40,60,22,18]
    day = int(input("Enter the day [0 - 6 (0 being Monday, 6 being Sunday)]: "))
    match day:
        case 0:
            print(f"Total notifications today: {notifications[0]}")
        case 1:
            print(f"Total notifications today: {notifications[1]}")
        case 2:
            print(f"Total notifications today: {notifications[2]}")
        case 3:
            print(f"Total notifications today: {notifications[3]}")
        case 4:
            print(f"Total notifications today: {notifications[4]}")
        case 5:
            print(f"Total notifications today: {notifications[5]}")
        case 6:
            print(f"Total notifications today: {notifications[6]}")
    totalnotifications = sum(notifications)
    print(totalnotifications)
notifsoftware()
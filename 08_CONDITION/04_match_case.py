while True:

    num = int(input("Enter you num : "))

    match num:
        case 1:
            print("You won a bike")
        case 7:
            print("You won a S25 ultra")
        case 9:
            print("you won a cycle")
        case _:
            print("Better luck next time")
    print("\n")
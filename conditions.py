command = ""
started = False
while True:
    command = input(">").lower()
    if command =="start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started....")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("car stopped.")
    elif command =="help":
        print('''
star - to star the car
stop - to stop the car
quit - to quite
help - to help
         ''')
    elif command =="quit":
        break
    else:
        print("Sorry , I dont understand")

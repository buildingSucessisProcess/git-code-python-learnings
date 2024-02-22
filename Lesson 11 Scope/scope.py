name = "Dave"
count = 1

def another():
    color = "blue"
    global count # making count from global level available
    count += 1
    print(count)

    def greeting(name):
        nonlocal color #get color from parent
        color = "red"
        print(color)
        print(name)

    greeting("Dave")

another()
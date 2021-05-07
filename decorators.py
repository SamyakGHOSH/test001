def announce(f):
    def wrapper():
        print(f"Function is commencing")
        f()
        print(f"Function is completed")
    return wrapper

@announce
def greeting():
    print(f"wazzup bitches")

greeting()
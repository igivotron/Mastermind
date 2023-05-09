from rules import MasterMind

if __name__ == '__main__':
    game = MasterMind(n=4, rep=False)
    game.generate()
    game.rules_message()
    while True:
        a = input("Your guess : ")
        if game.shot(a.split()):
            break
    print("You won")

import random

def guessing_game():
    print("Ku soo dhowow ciyaarta qiyaasta tirada!")
    secret_number = random.randint(1, 10)
    guess = None
    attempts = 0

    while guess != secret_number:
        try:
            guess = int(input("Qiyaas tiro u dhaxaysa 1 iyo 10: "))
            attempts += 1
            
            if guess < secret_number:
                print("Waa ka yar yahay! Kor u qaad tirada.")
            elif guess > secret_number:
                print("Waa ka weyn yahay! Hoos u dhig tirada.")
            else:
                print(f"Hambalyo! Waa adiga guuleystay. Waxaad ku heshay {attempts} jeer.")
        except ValueError:
            print("Fadlan geli tiro sax ah!")

guessing_game()

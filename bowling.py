def welcome():
    print('\nHi welcome to Base Camp Bowling Alley!\n')
    name = input('\nWhat is your name?\n')
    print('\nHi', name)
    response = input('\nAre you ready to bowl?\n')
    while True:
        if response == 'yes':
            break
        elif response == 'no':
            print('\nOk have a great day!\n')
        exit()


def bowling():
    bowl_pins = []
    for i in range(1, 10):
        print('-------------------------------------------')
        print('\nFrame', i)
        while True:
            ball_1 = int(input('\nWhat did you roll on ball 1?\n'))
            if ball_1 >= 0 and ball_1 <= 10:
                break
        while True:
            ball_2 = int(input('What did you roll on ball 2?\n'))
            if ball_1 + ball_2 >= 0 and ball_1 + ball_2 <= 10:
                break
        bowl_pins.append([ball_1, ball_2])
        print(bowl_pins)


def main():
    welcome()
    bowling()


if __name__ == '__main__':
    main()

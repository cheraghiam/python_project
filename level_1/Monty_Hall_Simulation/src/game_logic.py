import random 


doors = ['car'] + ['goat'] * 2
random.shuffle(doors) # shuffle doors varible, replace = True


def user_choice():
    try:
        user_input = int(input("select door: ['1', '2', '3']: "))

        if user_input in [1, 2, 3]:
            return user_input - 1

        print("please Enter a number in range 1 to 3")
        return user_choice()
    
    except ValueError:
        print("please Enter a number in range 1 to 3")
        return user_choice()
    

def find_another_goat():
    for i, w in enumerate(doors):
        if i == user_input:
            pass
        elif w == 'goat':
            another_goat = i
            break

    return another_goat


if __name__ == "__main__":
    user_input = user_choice()
    another_goat = find_another_goat()
    print(user_input, another_goat)
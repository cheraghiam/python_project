import random


def simulation(switch: bool) -> str:
    """Simulate the Monty Hall game.

    Args:
        Whether the contestant switches their choice.

    Returns:
        return goat or car string
    """

    doors = ['car'] + ['goat'] * 2
    random.shuffle(doors)
    number_of_choice = random.choice(range(3))

    for i, w in enumerate(doors):
        if i == number_of_choice:
            continue   

        elif w == 'goat':
            another_goat = i
            break
    
    if switch:
        switch_choice = [i for i in range(3) if i != number_of_choice and i != another_goat]
        return doors[switch_choice[0]]
    
    else:
        return doors[number_of_choice]
    

def counter_simulation(counter: int, strategy=False) -> tuple:
    """Simulate the Monty Hall game multiple times and return the results.

    Args:
        The number of simulations to run.

    Returns:
        The results of the simulations.
    """

    car = 0
    goat = 0

    for _ in range(counter):
        result = simulation(strategy)
        
        if result == 'car':
            car += 1

        else:
            goat += 1
    
    sum_car_goat = car + goat
    return (car / sum_car_goat), (goat / sum_car_goat)


if __name__ == "__main__":
    print(counter_simulation(10000))
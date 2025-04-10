import random

dors = {0,1,2}
time_of_wins = 0
time_of_loses = 0


def get_the_door_with_the_prize():
    return random.choice(list(dors))

def choose_a_door():
    door = 0 # just to add some time 
    return random.choice(list(dors))

def open_a_door(door_with_prize, chosen_door):
    if door_with_prize == chosen_door:
        # if the chosen door has the prize, open a random door that doesn't have the prize
        doors_to_open = list(dors - {door_with_prize})
    else:
        # if the chosen door does not have the prize, open the only other door that doesn't have the prize
        doors_to_open = list(dors - {door_with_prize} - {chosen_door})
   
    return random.choice(doors_to_open)

def switch_door(chosen_door, opened_door):
    # switch to the remaining door that is not the chosen door or the opened door
    return (dors - {chosen_door, opened_door}).pop()



def monty_hall_simulation(num_trials):
    global time_of_wins, time_of_loses
    for _ in range(num_trials):
        door_with_prize = get_the_door_with_the_prize()
        chosen_door = choose_a_door()
        opened_door = open_a_door(door_with_prize, chosen_door)
        switched_door = switch_door(chosen_door, opened_door)
        
        # printing progress
        if _ % (num_trials // 10) == 0:
            print(f"Progress: {(_ / num_trials) * 100:.2f}%")

        if switched_door == door_with_prize:
            time_of_wins += 1
        else:
            time_of_loses += 1

    return time_of_wins, time_of_loses

# run the simulation
monty_hall_simulation(1000000000)
print(f"Number of wins: {time_of_wins}")
print(f"Number of loses: {time_of_loses}")
print(f"Winning probability: {time_of_wins/(time_of_wins + time_of_loses)}")
print(f"Losing probability: {time_of_loses/(time_of_wins + time_of_loses)}")
print(f"Total trials: {time_of_wins + time_of_loses}")
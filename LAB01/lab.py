print("Hello World")

def wins_rock_scissors_paper(player, opponent):
    # make lowercase so Match is not ca se sensitive and so to make it all same
    player = player.lower()
    
    opponent = opponent.lower()

    # if same it's a tie game 
    if player == opponent:
        return False

    # check win conditions for player to win the game
    if (player == "rock" and opponent == "scissors") or \
       (player == "paper" and opponent == "rock") or \
       (player == "scissors" and opponent == "paper"):
        return True

    # player lost the game display
    return False


def factorial(n): #case 
    
    if n == 0:
        return 1

    total = 1
    for i in range(1, n + 1):
        total = total * i


    return total

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    first = 0

    second = 1

    for i in range(2, n + 1):
        next = first + second
        first = second
        second = next


    return second

def sum_to_goal(numbers, goal): # sum
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]

    return 0  


class UpCounter:
    def __init__(self, step=1):
        self.val = 0          # start at from value 0
        self.step = step      # step size decalred



    def count(self):
        return self.val       # return current value 

    def update(self):
        self.val = self.val + self.step  # go up and update the value after count



class DownCounter(UpCounter):
    def update(self):
        self.val = self.val - self.step  # reduce value 
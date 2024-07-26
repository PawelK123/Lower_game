# importing necessary things
import random
import Data
import Logo
# download logo and data
logo = Logo.logo
vs = Logo.vs
data = Data.data
print(logo)
# making a list of numbers 0-50 and using for choose data
list = [i for i in range(51)]
game = True
score = 0
A = random.choice(list)
list.remove(A)
A = data[A]
# main loop of game
while game == True:
    B = random.choice(list)
    list.remove(B)
    B = data[B]
    if B == A:
        B = random.choice(list)
        list.remove(B)
        B = data[B]
    # printing choosen data
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    # asking for decision
    decision = input("Who has more followers? Type 'A' or 'B': ").upper()
    # function which gives a right answer
    def compare(A,B):
        print(f"followers A {A}")
        print(f"followers B {B}")
        if A > B:
            return 'A'
        else:
            return 'B'
    result = compare(A['follower_count'],B['follower_count'])
    # checking if right answer is equal to decision
    # counting a score or finish the game if answer is wrong
    if result == decision:
        score += 1
        A = B
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game = False
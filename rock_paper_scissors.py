import random


def play():
    u_point = 0
    c_point = 0
    print("Collect 5 points to win.")
    while u_point != 5 and c_point != 5:
        user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
        computer = random.choice(["r", "p", "s"])
        if user == computer:
            print(f"Computer chose {computer}. Draw. The score is {u_point}/{c_point}")
        elif (user == "p" and computer == "r") or (user == "s" and computer == "p") or \
        (user == "r" and computer == "s"):
            u_point += 1
            print(f"Computer chose {computer}. User won. The score is {u_point}/{c_point}")
        elif (user == "p" and computer == "s") or (user == "s" and computer == "r") or \
        (user == "r" and computer == "p"):
            c_point += 1
            print(f"Computer chose {computer}. Computer won. The score is {u_point}/{c_point}")
    if u_point == 5:
        print(f"You won. The score is {u_point}/{c_point}")
    else:
        print(f"Computer won. The score is {u_point}/{c_point}")

play()

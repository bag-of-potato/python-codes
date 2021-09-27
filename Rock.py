import random

moves = ["rock", "paper", "scissors"]

play_again = 1
player_score = 0
comp_score = 0
ties = 0

while True:

    user_move = input("Move: ")
    while user_move.lower() not in moves:
        user_move = input("Oops! Enter a valid move:")


    comp_move = random.choice(moves)
    print(f"Computer: {comp_move}")
    if user_move == comp_move:
        print("Tie!")
        ties +=1
    elif user_move == "rock":
        if comp_move == "scissors":
            print("Rock beats scissors! User Wins!")
            player_score +=1
        else:
            print("paper covers rock! computer wins!")
            comp_score +=1
    elif user_move == "paper":
        if comp_move == "scissors":
            print("scissors cut paper! computer Wins!")
            comp_score +=1
        else:
            print("paper covers rock! User wins!")
            player_score +=1
    elif user_move == "scissors":
        if comp_move == "rock":
            print("rock breaks scissors! computer Wins!")
            comp_score +=1
        else:
            print("scissors cut paper! User wins!")
            player_score +=1
    print(f"user: {player_score} || Computer: {comp_score} || Ties: {ties}")

    play_again = int(input("Play Again? (0: no 1: yes): \n\n"))
    if play_again == 0:
        print("see ya!")
        break
    else:
        continue 

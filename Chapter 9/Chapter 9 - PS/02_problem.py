import random

def game():
    print("You are playing the game")
    score = random.randint(1, 62)
    # Fetch the high score from the file
    with open("high_score.txt", "r") as file:
        high_score = file.read()
        if (high_score != ""):
            high_score = int(high_score)
        else:
            high_score = 0
    print(f"Your score is: {score}")
    if(score > high_score):
        with open("high_score.txt", "w") as file:
            file.write(str(score))
        print("Congratulations! You have the new high score!")
        return score
    game()
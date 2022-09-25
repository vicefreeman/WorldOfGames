SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 0


# Clearing scores
def clear_score():
    # Resets the Score
    score_file = open(SCORES_FILE_NAME, "w")
    score_file.write("0")
    score_file.close()


# Checking if player wants to continue playing. If not, resetting score.
def check_play_again():
    yes = "y"
    no = "n"
    while True:
        try:
            answer = (input("Do you want to play some more? Y/N\n")).lower()
            if answer == yes:
                return True
            elif answer == no:
                print("Hope to see ya next time! BYE :)")
                clear_score()
                break
            else:
                print("I'm sorry...Didn't understand your answer...")
                continue
        except ValueError:
            print("I'm sorry...Didn't understand your answer...")

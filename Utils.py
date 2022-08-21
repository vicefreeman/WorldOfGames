SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 0


def screen_cleaner():
    # Resets the Score
    score_file = open(SCORES_FILE_NAME, "w")
    score_file.write("0")
    score_file.close()

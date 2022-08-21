import Utils


# Calculating Score and saving to txt file
def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    # Checking if file exists and adding score, if not, creating the file
    try:
        score_file_r = open(Utils.SCORES_FILE_NAME, "r")
        CURRENT_SCORE = int(score_file_r.read())
        score_file_r.close()
        UPDATED_SCORE = int(CURRENT_SCORE) + POINTS_OF_WINNING
        score_file_w = open(Utils.SCORES_FILE_NAME, "w")
        score_file_w.write(str(UPDATED_SCORE))
        score_file_w.close()
    except FileNotFoundError:
        score_file = open(Utils.SCORES_FILE_NAME, "x")
        score_file.write(str(POINTS_OF_WINNING))
        score_file.close()

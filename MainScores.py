import Utils
import GameSettings
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
# Creating dev Web server using pre-made templates
def score_server():
    try:
        score_file = open(Utils.SCORES_FILE_NAME, "r")
        current_score = score_file.read()
        score_template = render_template("score.html", PLAYER=GameSettings.user_name, SCORE=current_score)
        return score_template
    except FileNotFoundError:
        error_template = render_template("error.html", ERROR="OOPS...Unable to fetch the file...")
        return error_template


app.run()

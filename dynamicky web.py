from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data: list of sports teams
teams = [
    {'name': 'Team A', 'votes': 0},
    {'name': 'Team B', 'votes': 0},
    {'name': 'Team C', 'votes': 0},
]

@app.route("/")
def home():
    return render_template("index.html", teams=teams)

@app.route("/vote", methods=["POST"])
def vote():
    team_name = request.form.get('team')
    for team in teams:
        if team['name'] == team_name:
            team['votes'] += 1
            break
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

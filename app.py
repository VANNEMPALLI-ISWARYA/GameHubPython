from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gkquiz', methods=['GET', 'POST'])
def gkquiz():
    questions = {
        "Capital of India?": "Delhi",
        "Red Planet?": "Mars",
        "Father of Computer?": "Charles Babbage",
        "H2O is?": "Water"
    }
    if request.method == 'POST':
        score = 0
        for q in questions:
            answer = request.form.get(q)
            if answer and answer.lower() == questions[q].lower():
                score += 1
        return render_template('gkquiz_result.html', score=score, total=len(questions))
    return render_template('gkquiz.html', questions=questions)

@app.route('/hangman', methods=['GET', 'POST'])
def hangman():
    word = "flask"
    guessed = []
    display = ''
    if request.method == 'POST':
        letter = request.form['letter']
        guessed = request.form.getlist('guessed')
        guessed.append(letter)
        display = ''.join([c if c in guessed else '_' for c in word])
        if '_' not in display:
            return render_template('hangman.html', display=display, message="You won!", guessed=guessed)
    else:
        display = '_' * len(word)
    return render_template('hangman.html', display=display, guessed=guessed)

@app.route('/rps', methods=['GET', 'POST'])
def rps():
    result = None
    if request.method == 'POST':
        player = request.form['choice']
        computer = random.choice(['rock', 'paper', 'scissors'])
        if player == computer:
            result = "It's a tie!"
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            result = "You win!"
        else:
            result = "You lose!"
        return render_template('rps.html', result=result, player=player, computer=computer)
    return render_template('rps.html')

@app.route('/anagram', methods=['GET', 'POST'])
def anagram():
    word = "listen"
    shuffled = "enlist"
    message = None
    if request.method == 'POST':
        answer = request.form['answer']
        if sorted(answer) == sorted(word):
            message = "Correct!"
        else:
            message = "Try again."
    return render_template('anagram.html', shuffled=shuffled, message=message)

@app.route('/tictactoe')
def tictactoe():
    return render_template('tictactoe.html')

@app.route('/snake')
def snake():
    return render_template('snake.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, flash, session
from surveys import satisfaction_survey

app = Flask(__name__)
app.secret_key = 'survey_pass'

@app.route('/')
def home_page():
    return render_template('home.html', survey = satisfaction_survey)

@app.route('/question/<qNum>')
def qeustion_page(qNum):
    responses = session['responses']

    if int(qNum) != len(responses):
        flash('Invalid Question URL', 'error')
        return redirect(f'/question/{len(responses)}')
    
    if len(satisfaction_survey.questions) == len(responses):
        return redirect('/thankyou')

    question = satisfaction_survey.questions[int(qNum)]
    return render_template('question.html', question=question, qNum = int(qNum)+1)

@app.route('/answer', methods = ['POST'])
def story_page():
    responses = session['responses']
    responses.append(request.form['answer'])
    session['reponses'] = responses

    if len(satisfaction_survey.questions) == len(responses):
        return redirect('/thankyou')
    else:
        return redirect(f'/question/{len(responses)}')

@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html', survey = satisfaction_survey)

@app.route('/start', methods = ['POST'])
def start():
    session['responses'] = []
    return redirect('question/0')


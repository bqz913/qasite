from flask import Flask, render_template, jsonify
from models import question
from random import random
from datetime import datetime

app = Flask(__name__, static_folder='static')

question_list = []
for i in range(100):
    title = "title" + str(random())
    name = "name" + str(random())
    content = "content" + str(random())
    date = str(datetime.now())
    ans = "ans" + str(random())
    question_list.append(question.Question(name, title, content, date, ans))

@app.route('/')
def index():
    return render_template('index.html', questions=question_list)

@app.route('/get_data')
def get_data():
    questions = {}
    q_dict = {}
    for i, q in enumerate(question_list):
        q_dict[str(i)] = {
            "title": q.title,
            "name": q.name,
            "content": q.content,
            "date": q.date,
            "ans": q.ans
        }
        
        #questions.append(q_json)
    q_json = jsonify(q_dict)
    response_data = {
        'questions' : q_dict
    }
    print("aaa")
    return jsonify(response_data)

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
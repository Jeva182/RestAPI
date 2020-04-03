from flask import Flask, render_template, request
from textblob import TextBlob
from flask import Flask, render_template,request,url_for
from flask_bootstrap import Bootstrap 
import random
app = Flask(__name__)


@app.route('/')


def home():
    result = ""
    return render_template('home.html', result = result)


@app.route('/result', methods=['POST','GET'])

def sentiment():
    if request.method == 'POST':
        rawText = request.form['rawText'].lower()
        blob = TextBlob(rawText)
        inText = blob
        sentiment = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
       
                    

    return render_template('home.html', inText = inText,sentiment=sentiment, subjectivity=subjectivity)

















if __name__ == '__main__':
	app.run(debug=True)
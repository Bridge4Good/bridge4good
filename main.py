from flask import Flask, render_template, request
from donor_matching import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def template():
    return render_template('index.html')

def logistic_regression():
    if request.method == 'POST':
        zipcode = request.form['zipcode']
        donation = request.form['donation']

        message = match_donor(zipcode, donation)

    else:
        message = 'Submit your request!'


    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask, flash, redirect, render_template, request
from donor_matching import *
from shelter_matching import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def flexible():
    return render_template('index.html')

@app.route('/donor', methods=['POST'])
def donor():
    zipcode = int(request.form.get('zipcode'))
    donation = request.form.get('donation')
    age = int(request.form.get('age'))
    volunteer = request.form.get('volunteer')

    message = match_donor(zipcode, donation, age, volunteer)

    return render_template('donor_matched.html', message=message)


@app.route('/shelter', methods=['POST'])
def shelter():
    shelter = request.form.get('shelter')

    message = topthree(shelter)

    return render_template('shelter_matched.html', message=message)

if __name__ == '__main__':
    app.run(port=4000, debug=True)

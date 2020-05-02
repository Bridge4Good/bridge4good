from flask import Flask, flash, redirect, render_template, request
from donor_matching import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def flexible():
    return render_template('index.html')

def submit():
    if request.method == 'POST':
        return redirect('/demo')
    else:
        return render_template('index.html')

@app.route('/demo', methods=['POST'])
def demo():
    zipcode = int(request.form.get('zipcode'))
    donation = int(request.form.get('donation'))

    message = match_donor(zipcode, donation)

    return render_template('matched.html', message=message)


if __name__ == '__main__':
    app.run(port=1510, debug = True)

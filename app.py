from flask import Flask, flash, redirect, render_template, request
# from donor_matching import *
from shelter_matching import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def flexible():
    return render_template('index.html')

def submit():
    if request.method == 'POST':
        return redirect('/demo')
    else:
        return render_template('shelter_matched.html')


@app.route('/demo', methods=['POST'])
def demo():
    shelter = request.form.get('shelter')

    message = topthree(shelter)

    return render_template('shelter_matched.html', message=message)

if __name__ == '__main__':
    app.run(port=1510, debug=True)

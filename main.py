from flask import Flask, flash, redirect, render_template, request
from donor_matching import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def flexible():
    return render_template('frontend.html')

def demo():
    if request.method == 'POST':
        zipcode = int(request.form.get('zipcode'))
        donation = int(request.form.get('donation'))

        message = match_donor(zipcode, donation)

        return render_template('frontend.html', message=message)
    else:
        message = 'Internal Server Error'
        return render_template('frontend.html', message=message)


if __name__ == '__main__':
    app.run(port=1510, debug = True)

from flask import Flask, render_template, url_for, request, flash
from flask_wtf import FlaskForm
import json
from best_product import compare_prices


app = Flask(__name__)
app.config['SECRET_KEY'] = '5601e942bf913652dc096cb728f6c417'



@app.route("/")
def index():
    return render_template('index.html', title="Home")


@app.route('/result', methods=['GET', 'POST'])
def result():

    laughs_url = request.form['shop1_url']
    glomark__url = request.form['shop2_url']


    laughs, glomark, result = compare_prices(laughs_url, glomark__url)
    # return f"{laughs}<br/>{glomark}<br/><br/>{answer}<br/><br/><br/><a href='/'><button>Check Again</button></a>"

    flash(f'{result}', 'success')
    return render_template('result.html', laughs=laughs, glomark=glomark, title="Result")
  

if __name__ == '__main__':
    app.run(debug=True)



from unicodedata import name
from flask import Flask, render_template, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key="Black Sabbath and Iron Maiden Rule!"

@app.route('/')
def index():
    """POST input"""
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    """Write values to session"""
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['dojo_location'] = request.form['dojo']
    session['fav_lang'] = request.form['lang']
    session['comment'] = request.form['comments']
    return redirect('/result')
    

@app.route('/result')
def results():
    """Print Results"""
    return render_template('result.html')

# Error message for 404
@app.errorhandler(404)
def page_not_found(e):
    return f'Sorry! No response. Try again.'

# Ensure file is run directly and not from different
# module, and run localhost on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)

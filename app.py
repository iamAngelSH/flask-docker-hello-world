# IMPORT LIBRARIES
from flask import Flask, jsonify, request
import requests as rq

# INIT APP OBJECT
app = Flask(__name__)


# MENU FOR USERS WHO WOULD LIKE TO USE THE APP
@app.route('/')
def menu():
    l = '''
    <h1> Welcome, 👋</h1>
    <h3> Here are some cool things you can do. All this is done with the url.</h3>
    <ul>
        <li>Route Number 1</li>
            <ul>
                <li><a href="http://localhost:5555/ping" target = "_blank">http://localhost:5555/ping</a></li>
                <li>Will return an aweomse surprise: Try to PING it!</li>
            </ul>
        <li>Route Number 2</li>
            <ul>
                <li><a href="http://localhost:5555/word" target = "_blank">http://localhost:5555/word</a></li>
                <li>Get ready for a random word</li>
            </ul>
        <li>Route Number 3</li>
            <ul>
                <li><a href="http://localhost:5555/string-count" target = "_blank">http://localhost:5555/string-count</a></li>
                <li>Nothing crazy, get the length of a string.</li>
                <li>However won't work without using an online API testing tool or creating a request program.</li>
                
            </ul>
    </ul>


    '''
    return l
# <!-- Form which will send a POST request to the current URL -->
#                 <form method="post" action="/string-count">
#                 <label>Name:
#                     <input name="submitted-name" autocomplete="name">
#                 </label>
#                 <button>Save</button>
#                 </form>

# ROUTE 1: RETURNS PONG WHEN PINGED
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# ROUTE 2: RETURNS A RANDOM WORD FROM API
@app.route('/word', methods=['GET'])
def word():
    word = rq.get('https://random-word-api.herokuapp.com/word?number=1')

    # DIDN'T LIKE THE FORMAT : DID SOME STRING MANNIPULATION
    start = '["'
    end = '"]'
    for i in word:
        w = i.decode('utf-8')
        w = w[len(start):-len(end)]
        w = w[::-1]
        w = w.upper()
        return jsonify(w)

# ROUTE 3: RETURNS LENGTH OF STRING (SINGLE INPUT) -- ONLY WORKS WITH ONLINE API TESTING TOOL / MAKE REQUESTS PROGRAM
@app.route('/string-count', methods = ['POST'])
def string_count():

    user_word = request.get_json()

    len_word = len(user_word)
    return jsonify(len_word)

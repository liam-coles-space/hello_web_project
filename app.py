import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/submit', methods=['POST'])
def post_submit():
    return f"Thanks {request.form['name']}, you sent this message:{request.form['message']}"

@app.route('/wave', methods=['GET'])
def get_wave():
    return f"I am waving at {request.args['name']}"

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    vowels = ['a','e','i','o','u']
    count = 0
    for vowel in vowels:
        count += request.form['text'].count(vowel)

    return f"There are {count} vowels in \"{request.form['text']}\""

@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    new_list = request.form['names'].split(',')
    return ','.join(sorted(new_list))

@app.route('/names', methods=['GET'])
def get_names():
    return_list = request.args['add'].split(',')
    if len(return_list) == 1:
        return f"Julia, Alice, Karim, {request.args['add']}"
    else:
        return_list.extend(['Julia','Alice','Karim'])
        return ', '.join(sorted(return_list))


# == Example Code Below ==
@app.route('/', methods=['POST'])
def post_index():
    # DOES NOT RUN: The HTTP method (GET) doesn't match the route's (POST)
    return "Not me! :("

@app.route('/hello', methods=['GET'])
def get_hello():
    # DOES NOT RUN: The path (`/hello`) doesn't match the route's (`/`)
    return "Not me either!"

@app.route('/', methods=['GET'])
def get_index():
    # RUNS: This route matches! The code inside the block will be executed now.
    return "I am the chosen one!"

@app.route('/', methods=['GET'])
def other_get_index():
    # DOES NOT RUN: This route also matches, but will not be executed.
    # Only the first matching route (above) will run.
    return "It isn't me, the other route stole the show"

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


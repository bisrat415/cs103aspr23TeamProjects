'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' 
    display a link to the general query page
    and to the about page
    '''
    return f'''
        <h1>Creative Assignment 01</h1>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
        <p></p>
        <a href="{url_for('about')}">About</a>
        <p></p>
        <a href={url_for('compile')}>Index</a>
        <p></p>
        <a href={url_for('team')}>Team Page</a>
    '''
# added by Tal
@app.route('/about')
def about():
    ''' contents of about page '''
    return f'''
        <h1>About</h1>
        <p>Ask ChatGPT - Given by Hickey</p>
        <small>Query ChatGPT</small>
        <br>
        <br>
        <p>Generate a story - Implemented by Tal Spector</p>
        <small>Asks user for a topic, and returns a paragraph long story</small>
        <br>
        <br>
        <p>Translate a message - Implemented by Robin Buchthal</p>
        <small>Asks the user for a message and a language, then translates
        the message to the given language.</small>
        <br>
        <br>
        <a href={url_for('index')}><p>Return to Home Page</p></a>
        '''

@app.route('/index')
def compile():
    '''
    index of each team members prompt
    '''
    return f'''
    <h1>Individual Prompt Generation</h1>
    <p></p>
    <a href={url_for('tal')}>Tals Project - Story Generator</a>
    <br>
    <br>
    <a href={url_for('robin')}>Robins Project - Translator</a>
    <br>
    <br>
    <a href="{url_for('bisrat')}">Bisrats Project - Generate a Poem</a>
    '''

@app.route('/team')
def team():
    '''
    Bio of each team member and what their role was
    '''
    return f'''
    <h1>Team Biographies/Roles</h1>
    <h4>Tal</h4>
    <h4>Robin </h4>
    <h4>Bisrat</h4>

    '''

@app.route('/tal', methods=['GET', 'POST'])
def tal():
    ''' 
        Tals prompt
        Generates a short story based on a user inputed topic
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getWrite(prompt)
        return f'''
        <h1>Short Story</h1>
        <h3>Here is your short story!</h3>
        <p>{answer}<p>
        <p><p>
        <a href={url_for('tal')}>Request another story</a>
        <a href={url_for('index')}>Return to Home Page</a>
        '''
    else:
        return f'''
        <h1>Tal's Story Generator</h1>
        Enter a subject for a story below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="Get story">
        </form>
        <a href={url_for('index')}>Return to Home Page</a>
        '''

# added by robin 
@app.route('/robin', methods=['GET', 'POST'])
def robin():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.translator(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}>send another message</a>
        '''
    else:
        return '''
        <h1>Translate a message</h1>
        Submit a message to translate into a certain language with the format:
        <b>language, message</b>
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''   
    
# added by Bisrat                   
@app.route('/bisrat', methods=['GET', 'POST'])
def bisrat():
    ''' 
        Bisrat's prompt
        Compose a poem based on a user inputed topic
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getPoem(prompt)
        return f'''
        <h1>Poem</h1>
        <h2>Here is your poem!</h2>
        <div style="border:thin solid black">{answer}</div>
        <p><p>
        <a href={url_for('bisrat')}> make another poem</a>
        '''
    else:
        return f'''
        <h1>Poem Generator</h1>
        Please enter a topic for your poem below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
         <a href={url_for('index')}>Return to Home Page</a>
        '''

# hickey
@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
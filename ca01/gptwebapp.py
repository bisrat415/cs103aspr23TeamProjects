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
        <br>
        <br>
        <h1 style="text-align: center">Creative Assignment 01</h1>
        <a href="{url_for('gptdemo')}"><center>Ask questions to GPT</center></a>
        <p></p>
        <a href="{url_for('about')}"><center>About</center></a>
        <p></p>
        <a href={url_for('compile')}><center>Index</center></a>
        <p></p>
        <a href={url_for('team')}><center>Team Page<center></a>
    '''

@app.route('/about')
def about():
    ''' contents of about page '''
    return f'''
        <br>
        <h1><center>About</center></h1>
        <p><b><center>Ask ChatGPT - Given by Hickey</center></b></p>
        <small><center>Query ChatGPT</center></small>
        <br>
        <p><b><center>Generate a story - Implemented by Tal Spector</center></b></p>
        <small><center>Asks user for a topic, and returns a paragraph long story</center></small>
        <br>
        <p><b><center>Translate a message - Implemented by Robin Buchthal</center></b></p>
        <small><center>Asks the user for a message and a language, then translates
        the message to the given language.</center></small>
        <br>
        <p><b><center>Generate a poem - Implemented by Bisrat Kassie</center></b></p>
        <small><center>Asks the user for a topic, and then returns a poem based on that the given topic.</center></small>
        <br>
        <p><b><center>Generate a joke - Implemented by Ian Ho</center></b></p>
        <small><center>Asks the user for a type of joke, and then returns a funny joke that is categorized into the provided joke type.</center></small>
        <br>
        <p><b><center>Make a song - Implemented by Dakota Lichauco</center></b></p>
        <small><center>Asks the user for a prompt, and then returns a song based on the given prompt</center></small>
        <br>
        <a href={url_for('index')}><p><center>Return to Home Page</center></p></a>
        '''

@app.route('/index')
def compile():
    '''
    index of each team members prompt
    '''
    return f'''
    <br>
    <br>
    <h1><center>Individual Prompt Generation</center></h1>
    <p></p>
    <a href={url_for('tal')}><center>Tal's Project - Story Generator</center></a>
    <br>
    <br>
    <a href={url_for('robin')}><center>Robin's Project - Translator</center></a>
    <br>
    <br>
    <a href="{url_for('bisrat')}"><center>Bisrat's Project - Generate a Poem</center></a>
    <br>
    <br>
    <a href="{url_for('ian')}"><center>Ian's Project - Generate a Joke</center></a>
    <br>
    <br>
    <a href={url_for('dakota')}><center>Dacoder's Project - Write a Song!</center></a>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <a href={url_for('index')}><center>Return to home page</center></a>
    '''

@app.route('/team')
def team():
    '''
    Bio of each team member and what their role was
    '''
    return f'''
    <br>
    <h1><center>Team Biographies/Roles</center></h1>
    <h4><center>Tal</center></h4>
    <p><center>Sophomore Computer Science/Linguistics double major<br>
    Implemented story generator and Index/About pages
    <h4>Robin </h4>
    <p>Sophomore Computer Science major Mathematics minor<br>
    Implemented translator, About page, added the return to home link on some of the pages, and style
    <h4>Bisrat</h4>
    <p>Sophomore Computer Science major Mathematics minor<br>
    Implemented poem generator, worked a bit on the index page, and maintained the repository
    <h4>Ian</h4>
    <p>Sophomore Computer Science and Business major<br>
    Implemented joke generator 
     <h4>Dakota</h4>
    <p>Sophomore Computer Science and Math major<br>
    Implemented Song generator
    <br>
    <br>
    <br>
    <a href={url_for('index')}>Return to Home Page</a>
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
        <a href={url_for('robin')}>send another message</a>
        <a href={url_for('index')}>Return to Home Page</a>
        '''
    else:
        return f'''
        <br>
        <h1 style="color: #2C5E1A"><center>Robin's Translator<center></h1>
        <center>Submit a message to translate into a certain language with the format:
        <b>language, message</b>
        <br>
        <br>
        <br>
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="Get translation">
        </form>
        <img src="https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/I/512M+bmEuKL.jpg" heigt="50px" width="auto" alt="cat selfie">
        <br>
        <br>
        <br>
        <a href={url_for('index')}>Return to Home Page</a>
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

# Added by Ian
@app.route('/ian', methods=['GET', 'POST'])
def ian():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getJoke(prompt)
        return f'''
        <h1>Jokes</h1>
        <h2>What type of joke do you want?</h2>
        <div style="border:thin solid black">{answer}</div>
        <p><p>
        <a href={url_for('ian')}> make another joke</a>
        '''
    else:
        return f'''
        <h1>Joke Generator </h1>
        What kind of joke do you want?
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        <a href={url_for('index')}>Return to Home Page</a>
        '''

# added by Dakota Lichauco
@app.route('/dakota', methods=['GET', 'POST'])
def dakota():
    ''' 
    Dakota's Prompt
    Writes a song based on user's suggested topic of a song.
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getSong(prompt)
        return f'''
        <h1>Song</h1>
        <h2>This is your song!</h2>
        <div style="border:thin solid black">{answer}</div>
        <p><p>
        <a href={url_for('dakota')}> Make another song</a>
        '''
    else:
        return f'''
        <h1>Write a Song</h1>
        What would you like your song to be about?
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
        <a href={url_for('index')}>Return to Home Page</a>
        '''
    else:
        return f'''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        <a href={url_for('index')}>Return to Home Page</a>
        '''
    

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5002)
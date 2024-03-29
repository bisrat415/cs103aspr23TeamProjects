'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    # tal
    def getWrite(self, prompt):
        ''' 
            Specific prompt that GPT will respond to
            contribution by Tal Spector
        '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt= f'''Write a story in JR Tolkeins voice that is 
            no longer than a paragraph about the given topic, don't 
            include a title: {prompt} \n\n''',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    # robin
    def translator(self, prompt):
        ''' 
            Language Translator
            contribution by Robin Buchthal 
        '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt= f'''Translate the given text into the language inputted by the user, it will
            be of the form "language, text". If there is no language provided,
            translate the text into giberish: {prompt} \n\n''',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    # Bisrat
    def getPoem(self, prompt):
        ''' 
            Poem Generator
            contribution by Bisrat Kassie
        '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt= f'''Write a poem about this topic, have a catchy title at the beginning: {prompt} \n\n''',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    #Ian
    def getJoke(self, prompt):
        ''' 
            Joke Generator
            contribution by Ian Ho 
        '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=f'''Give me a joke that will make me laugh: {prompt} \n\n''',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    #Dakota
    def getSong(self, prompt):
        ''' 
            Write a Song!
            contribution by Dakota Lichauco
        '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt= f'''Write lyrics to a song about this topic, create a song name as well: {prompt} \n\n''',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))
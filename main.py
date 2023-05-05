
import streamlit as st 
from streamlit_chat import message
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from PIL import Image

import requests
import openai
#----------------Lottie Animation ---------------

def load_lottieurl(url:str):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_animation1="https://assets7.lottiefiles.com/packages/lf20_96bovdur.json"
lottie_anime_json=load_lottieurl(lottie_animation1)
st_lottie(lottie_anime_json,width=200,height=200)
    
#----------------AI Assistant -------------------
#connect to open Ai
openai.api_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

st.title("Hi! I am your Intelligent Chatbot")
st.subheader(':blue[AI Assistant:dart: : Streamlit + OpenAI]')


def generate_response(prompt):
    completions =openai.Completion.create(
        engine= "text-davinci-003",
        prompt= prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message= completions.choices[0].text
    return message

#store interactions with the chatbot
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    #input_text = st.text_input("You: ","Hello, how are you?", key="input")
    input_text = st.text_input("You: ",placeholder="Ask me anything ...", key="input")
    return input_text 

user_input = get_text()
if user_input:
    output = generate_response(user_input)
    #store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template="""
    Below is an email that maybe poorly worded.
    
    Your goal is to:
    - Properly format the email,with right email format 
    - Convert the input text to a specified tone
    - Convert the input text to a specified dialect
    
    Here are some examples different Tones:
    - Formal: We went to Barcelona for the weekend.We have a lot of things to tell you.
    - Informal: Went to Barcelona for the weekend.Lots to tell you.
    
    Here are some examples of words in different dialects:
    - American English: French Fires,cotton candy,apartment,garbage,
    - British English: chips,candyfloss,flag,rubbish

    Below is the email,tone ,and the dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}

    YOUR RESPONSE: 
"""
prompt=PromptTemplate(
    input_variables=["tone","dialect","email"],
    template=template,
)
def load_LLM():
    """Logic for liading the chain you want to use should go here."""
    llm=OpenAI(temperature=0.5)
    return llm

llm=load_LLM()

st.set_page_config(page_title="Globalize Email",page_icon=":robot:")
st.header("Globalize Email")


col1,col2=st.columns(2)

with col1:
    st.markdown("Often professionals would like to import their emails, but don't have the skils to do so."   
                "             "   
                "This tool will help you improve your email skills by converting your emails into a more profession"
                "format. This tool is powered by [LangChain](www.langchain.com) and [OpenAI](https://openai.com)."
    )  

with col2:
    st.image(image="sakura.jpg",width=500,caption="https://mzh.moegirl.org.cn/%E9%97%B4%E6%A1%90%E6%A8%B1(Fate/EXTRA)#/media/File:Ccc%E7%BA%BF%E7%BB%93%E5%B1%80cg.jpg")


st.markdown("## Enter Your Email To Convert")
col1,col2=st.columns(2)
with col1:
    option_tone=st.selectbox(
        'Which tone would you like your email to have?',
    ('Formal','Informal')
    )
with col2:
    option_dialect=st.selectbox(
        'Which English Dialect would you like your email to have?',
    ('American English','British English')
    )

def get_text():
    input_text=st.text_area(label="",placeholder="Your Email...",key="email_input")
    return input_text
email_input=get_text()

st.markdown("### Your Converted Email: ")
if email_input:
    prompt_with_email=prompt.format(tone=option_tone,dialect=option_dialect,email=email_input)

    formatted_email=llm(prompt_with_email)
    st.write(formatted_email)
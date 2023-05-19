__author__ = 'Juingya'
import os
import openai
from flask import render_template
from flask_restful import Resource, Api, request
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain import LLMChain, PromptTemplate

openai.api_key = ""

prompt_template = """请对如下文本进行文本摘要:

{text}

输出10个字的中文文本摘要:"""

# def login():
#     return render_template('login.html')


# def register():
#     return render_template('register.html')

class login(Resource):
    def get(self):
        return render_template('login.html')


class HelloWorld(Resource):
    def post(self):
        data = request.get_json()
        message = data.get("message")
        print(message)
        llm = ChatOpenAI(temperature=0)
        # chain = load_summarize_chain(llm, chain_type="map_reduce", verbose=True)
        # result = chain.run(input)

        llm_chain = LLMChain(
            llm=llm,
            prompt=PromptTemplate.from_template(prompt_template)
        )
        result = llm_chain(message)
        return result

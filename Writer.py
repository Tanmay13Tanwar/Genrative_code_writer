from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyAZSP3AXxW8vmcalgAYmikudzSqT_IgWQk"
llm = ChatGoogleGenerativeAI(model="gemini-pro")

def generate_code(file_content):
    title_template = PromptTemplate(
            input_variables=['file_content'],
            template="Given the following file content:\n {file_content} \nGenerate the relevant Python code.Just provide me with the code without adding the code into the main function so that it can be executed directly.do not import any external library "
        )

    title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='output')

    response = title_chain.invoke({'file_content': file_content})
    
    code = response["output"].strip()

    return code



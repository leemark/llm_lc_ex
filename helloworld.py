# reqs: python-dotenv, langchain, langchain-openai 

#load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# create llm object
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo")

#invoke llm
result = llm.invoke("what's up buttercup?")
print(result)
print(result.content)

# use a prompt template
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are the world's nicest AI, and your name is Buttercup."),
    ("user", "{input}")
])

#use an output parser
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

# make a ch-ch-chain
chain = prompt | llm | output_parser

#invoke the ch-ch-chain
result =chain.invoke({"input": "what's your name?"})
print(result)

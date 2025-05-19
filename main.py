from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import  add_routes
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4",temperature=0.3)



prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","Translate the following into {language}"),
        ("user", "{text}")
    ]
)


parser = StrOutputParser()

chain = prompt_template | model | parser

app = FastAPI(
    title="Simple Translate Bot"
)

add_routes(app,chain,path="/translator")


if __name__ == "__main__":
    import  uvicorn
    uvicorn.run(app,host="localhost",port=8000)


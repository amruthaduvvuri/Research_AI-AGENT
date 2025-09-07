from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langachain.agents import create_tool_calling_agent , AgentExecutor
from tools import search_tool, wiki_tool, save_tool

load_dotenv()
#specify all of the fields that we want as an output from our LLM call
class ReasearchResponse(BaseModel):
    title: str
    summary: str
    key_points: list[str]
    tools_used: list[str]
    
#setup LLMs - generate output in a specific form 

#llm = ChatOpenAI(model = "gpt-4o-mini")
#we are using chatanthropic for claude 3.5
llm = ChatAnthropic(model = "claude-3-5-sonnet-20241022")
#parser will now us to take the output from the LLM and convert it into a pydantic object
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

#setting up prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        (
            #tells what the agent does 
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"), #user input
        ("placeholder", "{agent_scratchpad}"),
    ]
#format instructions should be same as the above 
).partial(format_instructions=parser.get_format_instructions())

#agent 
tools = [search_tool,]
agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools = tools 
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("What can i help you research? ")
raw_response = agent_executor.invoke({"query": query}) #can pass multiple queries 

#structured response = parser.parse(raw_response.get("output")[0]["text"])
#print(structured_response.topic)
try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)
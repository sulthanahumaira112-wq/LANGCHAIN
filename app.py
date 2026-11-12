from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from tools import(
    get_customer,
    get_order,
    calculate_total,
    get_order_status
)

load_dotenv()

llm=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

tools=[
    get_customer,
    get_order_status,
    get_order,
    calculate_total
]

agent=create_react_agent(
    llm,
    tools
)

print("AI Business Assistant is ready!")

while True:
    question=input("\nYou:")

    if question.lower()=="exit":
        print("Goodbye!")
        break

    if not question.strip():
        continue

    try:
        response=agent.invoke({
            "messages":[
                ("user",question)
            ]
        })
        answer=response["messages"][-1].content
        print("\nAI ASSISTANT:",answer)

    except Exception as e:
        print("\nError:",e)
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

link = os.getenv("OPENROUTER")

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    base_url="https://openrouter.ai/api/v1",
    api_key=link,
    temperature=0.5
)

class WaterAgent:

    def __init__(self):
        self.history = []

    def analyse_and_intake(self, intake_ml):

        prompt = f"""
        You are a Hydration Assistant.

        User consumed {intake_ml} mL water today.

        Tell:
        1. Estimated daily water goal.
        2. Consumed water.
        3. Remaining water required.
        4. One short hydration tip.
        """

        response = llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content
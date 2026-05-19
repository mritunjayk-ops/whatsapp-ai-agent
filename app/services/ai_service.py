import os

from dotenv import load_dotenv
from openai import OpenAI

from app.services.memory_service import (
    add_message,
    get_conversation_history
)

from app.utils.logger import logger


load_dotenv()


client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def load_system_prompt():

    with open(
        "app/prompts/system_prompt.txt",
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


async def get_ai_response(user_message: str):

    try:

        logger.info(f"User Message: {user_message}")

        system_prompt = load_system_prompt()

        add_message("user", user_message)

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        messages.extend(get_conversation_history())

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )

        ai_response = completion.choices[0].message.content

        logger.info(f"AI Response: {ai_response}")

        add_message("assistant", ai_response)

        return ai_response

    except Exception as error:

        logger.error(f"Error occurred: {str(error)}")

        return (
            "Sorry, something went wrong while "
            "processing your request."
        )
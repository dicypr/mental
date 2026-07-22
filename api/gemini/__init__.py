import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def get_response(prompt):
    prompt = (
        "Assume you are a mental health expert and are helping struggling and stressed campus students, so reply to the following question in the language of the following prompt, and act as if it is a conversation and preferably keep answers short and friendly: \n"
        + prompt
    )
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content


import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def ask_groq(prompt: str) -> str:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an IT automation agent. When given a task, reply with ONLY the URL to open. Nothing else. No explanation."
            },
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def query_model(prompt: str, model="gpt-4"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message["content"].strip()

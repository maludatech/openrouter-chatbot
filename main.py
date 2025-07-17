import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

model = "mistralai/mistral-7b-instruct"  # Cheaper model, less chance of 402 error

print("AI Chatbot (type empty input to quit):\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        break

    messages.append({"role": "user", "content": user_input})

    data = {
        "model": model,
        "messages": messages,
        "max_tokens": 100
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    try:
        reply = response.json()['choices'][0]['message']['content']
        print(f"AI: {reply.strip()}")
        messages.append({"role": "assistant", "content": reply})
    except (KeyError, IndexError):
        print("\n❌ Something went wrong:")
        print(f"Status: {response.status_code}")
        print(response.text)
        break

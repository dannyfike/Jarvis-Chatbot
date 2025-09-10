import requests

# 🔑 INSERT YOUR API KEY HERE
API_KEY = "YOUR_API_HERE"

API_URL = "https://api.mistral.ai/v1/chat/completions"

# System prompt: sets the AI's personality or rules
SYSTEM_PROMPT = """
You are Jarvis, Tony Stark's AI assistant. 
You are extremely polite, professional, and intelligent. 
You respond quickly and efficiently, with a touch of dry humor or sarcasm when appropriate. 
You never give vague answers; always provide clear explanations. 
You can offer suggestions, advice, and witty commentary when asked. 
Keep your tone calm, sophisticated, and slightly witty, like a futuristic AI assistant.
"""


def chat_with_mistral(message, conversation=[]):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Only add system prompt once at the start
    if not conversation:
        conversation.append({"role": "system", "content": SYSTEM_PROMPT})

    # Add user message
    conversation.append({"role": "user", "content": message})

    data = {
        "model": "open-mistral-7b",
        "messages": conversation
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        ai_message = response.json()['choices'][0]['message']['content']
        conversation.append({"role": "assistant", "content": ai_message})
        return ai_message
    else:
        return f"Error: {response.status_code} - {response.text}"

# 🗨️ Main Chat Loop
conversation_history = []
print("🤖 Mistral Chatbot - Type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    ai_response = chat_with_mistral(user_input, conversation_history)
    print(f"Chatbot: {ai_response}\n")

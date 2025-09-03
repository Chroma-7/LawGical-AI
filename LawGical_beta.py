import google.generativeai as genai

# Configure with your API key
genai.configure(api_key="AIzaSyDJWbiYWr48KsViFW1TyjU00DAoSE8qVC0")

# Choose a Gemini model (latest is gemini-1.5-flash or gemini-1.5-pro)
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize conversation
conversation = [
    {"role": "system", "content": "You are LawGical, a virtual legal assistant. "
                                  "You provide legal information, explain laws, introduce lawyers that specialize in different cases, and give hypothetical advice. "
                                  "Do not give instructions for illegal activity."}
]

print("LawGical Proto_Python edition - 50 requests per day\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    # Append user message
    conversation.append({"role": "user", "content": user_input})

    # Build prompt
    prompt = "\n".join([f'{msg["role"]}: {msg["content"]}' for msg in conversation])

    # Generate response
    response = model.generate_content(prompt)

    assistant_reply = response.text.strip()

    # Append assistant message
    conversation.append({"role": "assistant", "content": assistant_reply})

    # Show reply
    print(f"LawGical: {assistant_reply}\n")

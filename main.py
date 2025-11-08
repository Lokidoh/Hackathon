import os
from dotenv import load_dotenv
from groq import Groq

# Initialize client

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Define the debate personality
system_prompt = """
You are 'Argus', an expert debater AI.
Your goal is to challenge the user's arguments in an intelligent, logical, and respectful way.
Always take an opposing stance or raise counterpoints.
Use evidence, reasoning, and rhetorical techniques like analogy or reductio ad absurdum.
Never agree easily — force the user to defend their ideas clearly.
Keep responses concise but thought-provoking.
"""

# Initialize the conversation
messages = [{"role": "system", "content": system_prompt}]

print("🧠 Argus Debate Bot — type 'exit' or 'quit' to stop debating.\n")

# Conversation loop
topic = input("I want to learn about: ")
if topic.lower() in ["exit", "quit"]:
    print("🫡 Debate concluded. Well fought!")


side = input("Do you want pro or con first? ").lower()

if side.lower() in ["exit", "quit"]:
    print("🫡 Debate concluded. Well fought!")
    exit()

# Add user message
messages.append({"role": "user", "content": f"debate {side} on: {topic}"})

try:
    # Generate AI response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=messages
    )

    # Extract reply text
    reply = response.choices[0].message.content
    print(f"Argus: {reply}\n")

    # Add assistant message to history
    messages.append({"role": "assistant", "content": reply})

except Exception as e:
    print(f"⚠️ Error: {e}\n")

side = "con" if side == "pro" else "pro"
messages.append({"role": "user", "content": f"debate {side} on: {topic}"})

print(f"Now for the {side} on {topic}: ")

try:
    # Generate AI response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=messages
    )

    # Extract reply text
    reply = response.choices[2].message.content
    print(f"Argus: {reply}\n")

    # Add assistant message to history
    messages.append({"role": "assistant", "content": reply})

except Exception as e:
    print(f"⚠️ Error: {e}\n")





    

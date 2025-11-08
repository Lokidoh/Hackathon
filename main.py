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

# Set up initial messages with system prompt
messages = [{"role": "system", "content": system_prompt}]
affirmative_history = []
negative_history = []

# Welcome message
print("🧠 Argus Debate Bot — type 'exit' or 'quit' to stop debating.\n")


###############################
"""
1) USER CALL
Get User Input
Check if the user wants to exit the debate
Add user message to the messages list
"""
user_input = input("What would you like to learn about today? ")
if user_input.lower() in ["exit", "quit"]:
    print("🫡 Debate concluded. Well fought!")
    exit()

# Add user message
messages.append(
    {
        "role": "admin",
        "content": f"The user's selected topic is: {user_input}. Give a statement from the affirmative side.",
    }
)
###############################

###############################
"""
2) Affirmative AI CALL

If didn't exit, call Llama to get a response
Append Respone to History
"""
try:
    # Generate AI response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=messages
    )

    # Extract reply text
    reply = response.choices[0].message.content
    print(f"Affirmative: {reply}\n")
    affirmative_history.append(reply)

    # Add assistant message to history
    messages.append({"role": "Affirmative", "content": reply})

except Exception as e:
    print(f"⚠️ Error: {e}\n")

###############################

###############################
"""
3) Negative AI CALL

If didn't exit, call Llama to get a response
Append Respone to History
"""

print("Now, present the opposing viewpoint.\n")

messages.append(
    {
        "role": "admin",
        "content": f"The user's selected topic is: {user_input}. Give a statement from the negative side to this topic.",
    }
)

try:
    # Generate AI response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=messages
    )

    # Extract reply text
    reply = response.choices[0].message.content
    print(f"Negative: {reply}\n")
    negative_history.append(reply)

    # Add assistant message to history
    messages.append({"role": "Negative", "content": reply})

except Exception as e:
    print(f"⚠️ Error: {e}\n")

###############################

####### REBUTTAL SECTION ########
# Ask user to Continue for rebuttal or exit

# Continue or Exit
# Ask both AIs to rebut each other's points

# loop for more rebuttal points if user wants, else continue or exit

###### Questionaire Section ########
# Ask user if they have any questions, and which side they are asking to
# Ask AI to answer user's questions
# Loop until user wants to exit, or continue to Conclusion

####### Conclusion Section ########
# Ask both AIs to give closing statements
# Print closing statements
# Automatic Exit

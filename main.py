import os
from dotenv import load_dotenv
from groq import Groq
import pyttsx3

# ==============================
# SETUP
# ==============================
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 0.9)

# ==============================
# HELPERS
# ==============================
def speak(text):
    """Speaks a text response."""
    engine.say(text)
    engine.runAndWait()


def generate_response(role, messages):
    """Send a message to Groq model and return the response text."""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
        reply = response.choices[0].message.content.strip()
        print(f"\n{role}: {reply}\n")
        speak(reply)
        return reply
    except Exception as e:
        print(f"Error generating {role}: {e}")
        return "[Error generating response]"


def user_question_phase(affirmative, negative):
    """Allows user to ask questions to either side."""
    while True:
        question = input("Would you like to ask a question (or type 'continue')? ").strip().lower()
        if question in ["continue", "no", "n"]:
            break

        target = input("Ask which side? (affirmative/negative): ").strip().lower()
        if target not in ["affirmative", "negative"]:
            print("Please choose 'affirmative' or 'negative'.")
            continue

        if target == "affirmative":
            messages = [
                {"role": "system", "content": "You are the Affirmative side in a formal debate."},
                {"role": "user", "content": f"The question is: {question}"}
            ]
            generate_response("Affirmative (Answer)", messages)
        else:
            messages = [
                {"role": "system", "content": "You are the Negative side in a formal debate."},
                {"role": "user", "content": f"The question is: {question}"}
            ]
            generate_response("Negative (Answer)", messages)


def judge_decision(topic, affirmative_case, negative_case, aff_rebuttal, neg_rebuttal):
    """Mediator evaluates who made the stronger case."""
    judge_prompt = [
        {
            "role": "system",
            "content": (
                "You are a neutral debate judge. Evaluate both sides of a Public Forum debate. "
                "Base your judgment on clarity, logic, and evidence. Give a concise decision (~100 words) "
                "and announce the winner: Affirmative or Negative."
            ),
        },
        {
            "role": "user",
            "content": f"Topic: {topic}\n\n"
                       f"Affirmative Case: {affirmative_case}\n\n"
                       f"Negative Case: {negative_case}\n\n"
                       f"Affirmative Rebuttal: {aff_rebuttal}\n\n"
                       f"Negative Rebuttal: {neg_rebuttal}\n\n"
                       "Provide your final judgment."
        }
    ]
    decision = generate_response("Mediator (Judge)", judge_prompt)
    print("Debate concluded.")
    return decision


# ==============================
# MAIN FLOW
# ==============================
print("Hot Take Debate AI — Public Forum Format\n")

topic = input("Enter a debate topic: ").strip()

# ===== Constructives =====
affirmative_messages = [
    {"role": "system", "content": "You are the Affirmative side in a debate. Present your constructive case clearly and persuasively in under 200 words."},
    {"role": "user", "content": f"The debate topic is: {topic}"}
]
affirmative_constructive = generate_response("Affirmative Constructive", affirmative_messages)

negative_messages = [
    {"role": "system", "content": "You are the Negative side in a debate. Present your constructive case clearly and persuasively in under 200 words."},
    {"role": "user", "content": f"The debate topic is: {topic}"}
]
negative_constructive = generate_response("Negative Constructive", negative_messages)

user_question_phase(affirmative_constructive, negative_constructive)

# ===== Rebuttals =====
affirmative_rebuttal_messages = affirmative_messages + [
    {"role": "user", "content": f"Your opponent said: {negative_constructive}\nProvide your rebuttal in under 180 words."}
]
affirmative_rebuttal = generate_response("Affirmative Rebuttal", affirmative_rebuttal_messages)

user_question_phase(affirmative_constructive, negative_constructive)

negative_rebuttal_messages = negative_messages + [
    {"role": "user", "content": f"Your opponent said: {affirmative_rebuttal}\nProvide your rebuttal in under 180 words."}
]
negative_rebuttal = generate_response("Negative Rebuttal", negative_rebuttal_messages)

user_question_phase(affirmative_constructive, negative_constructive)

# ===== Closing Statements =====
affirmative_closing = generate_response(
    "Affirmative Closing",
    affirmative_messages + [{"role": "user", "content": "Give a strong closing statement summarizing your stance in under 150 words."}]
)

negative_closing = generate_response(
    "Negative Closing",
    negative_messages + [{"role": "user", "content": "Give a strong closing statement summarizing your stance in under 150 words."}]
)

# ===== Judge Decision =====
judge_decision(topic, affirmative_constructive, negative_constructive, affirmative_rebuttal, negative_rebuttal)

import os
from groq import Groq


GROQ_API_KEY = os.getenv('GROQ_API_KEY')


if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Set it using: export GROQ_API_KEY='your-api-key'")

client = Groq(api_key=GROQ_API_KEY)


def chat_with_groq(prompt):
    """Interact with Groq AI models to get a response."""
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # You can change the model if needed
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print("Chatbot initialized. Type 'exit', 'quit', or 'bye' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        response = chat_with_groq(user_input)
        print("Chatbot:", response)

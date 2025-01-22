import os
from groq import Groq


# Manually set your API key as an environment variable (or hardcode it here, but not recommended)
GROQ_API_KEY = "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"

# Ensure the API key is available
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Set it using: export GROQ_API_KEY='your-api-key'")

# Initialize the Groq API client
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

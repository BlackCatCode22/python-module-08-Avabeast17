import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY environment variable not set.")


client = OpenAI(api_key=api_key)


def generate_response(messages):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()


def main():
    print("Welcome to Caprice's Python Chatbot!")
    print("Type 'quit' or 'exit' to end the chat.\n")


    messages = [
        {
            "role": "system",
            "content": (
                "You are a kind, patient Python tutor. "
                "Explain things in simple, beginner-friendly language."
            ),
        }
    ]

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() in ("quit", "exit"):
            print("Bot: Goodbye! 👋")
            break


        messages.append({"role": "user", "content": user_input})

        try:
            reply = generate_response(messages)
        except Exception as e:
            print("Bot: Oops, something went wrong:", e)
            continue


        messages.append({"role": "assistant", "content": reply})

        print("Bot:", reply)


if __name__ == "__main__":
    main()

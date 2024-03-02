


import openai

api_key = "Your OpenAI API key here"
openai.api_key = api_key

# def ask_question(question):
#     response = openai.Completion.create(
#         model="gpt-3.5-turbo-instruct",
#         prompt=f"I am a helpful Kidney Disease assistant.\nQ: {question}\nA:",
#         max_tokens=50
#     )
#     return response["choices"][0]["text"].strip()

# # Example usage
# question = "What is the capital of France?"
# answer = ask_question(question)
# print("Answer:", answer)

def ask_question(question):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"I am a helpful Kidney Disease assistant.\nQ: {question}\nA:",
        max_tokens=50
    )
    return response["choices"][0]["text"].strip()

def main():
    print("Welcome to the Kidney Disease Chatbot!")
    while True:
        question = input("You: ")
        if question.lower() == "exit":
            print("Exiting the chatbot. Goodbye!")
            break
        answer = ask_question(question)
        print("Chatbot:", answer)

if __name__ == "__main__":
    main()

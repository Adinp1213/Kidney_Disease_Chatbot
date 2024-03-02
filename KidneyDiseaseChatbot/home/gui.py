
import openai

api_key = "Your OpenAI API Key Here"
openai.api_key = api_key

def ask_question(question):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"I am a helpful Kidney Disease assistant.\nQ: {question}\nA:",
        max_tokens=50
    )
    return response["choices"][0]["text"].strip()

def get_response(question):
    answer = ask_question(question)
    print(answer)
    return answer

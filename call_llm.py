from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables

myapikey = os.getenv('GEMINIKEY')


from google import genai

client = genai.Client(api_key=myapikey)

<<<<<<< HEAD


def call_llm(prompt: str, modelinput: str = "gemini-2.5-flash-lite") -> str:
   
    response = client.models.generate_content(
        model=modelinput, contents=prompt
    )
    return response.text


print(call_llm(input()))
=======
# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Explain how AI works in a few words"
# )
# print(response.text)

def call_llm(prompt: str,modelinput: str = "gemini-2.5-flash") -> str:
    response = client.models.generate_content(
    model= modelinput, contents=prompt
    )
    return response.text
print(call_llm("what's up"))
>>>>>>> origin/main

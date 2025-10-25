from dotenv import load_dotenv
import os 
load_dotenv()  # take environment variables

myapikey =  os.getenv('GEMINIKEY')

from google import genai

client = genai.Client(api_key=myapikey)



def call_llm(prompt: str, modelinput: str = "gemini-2.5-flash-lite") -> str:
   
    response = client.models.generate_content(
        model=modelinput, contents=prompt
    )
    return response.text


print(call_llm(input()))
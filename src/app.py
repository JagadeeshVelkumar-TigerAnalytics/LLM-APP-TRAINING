from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
base_url = "https://api.ai-gateway.tigeranalytics.com"
api_key = os.getenv("LLAMA_API_KEY")

client = OpenAI(api_key=api_key,base_url=base_url)
# question = ''
# while question.lower() != 'exit':
#     question = input("type your question...")
#     bot = client.chat.completions.create(
#             model= "llama-3.2-1b-instruct",
#             messages=[
#                 {
#                     "role" : "user",
#                     "content" : question
#                 }
#             ],
#             stream=True,
#             # temperature = 1,
#             # top_p=1,
#             # frequency_penalty=1,
#             # presence_penalty=1,
#             max_completion_tokens=25
#         )

#     for chunk in bot:
#         delta = chunk.choices[0].delta
#         if delta.content is not None:
#             print(delta.content, end="", flush=True)



question = ''
chat_history = []
while question.lower() != 'exit':
    question = input("\n type your question...")
    chat_history.append(
        {
            "role" : "user",
            "content" : question
        }
    )
    bot = client.responses.create(
            model= "llama-3.2-1b-instruct",
            input = chat_history,
            stream=True,
            temperature = 0,
            # top_p=1,
            max_output_tokens=250,
        )
    
    response = []
    for event in bot:
        if event.type == 'response.output_text.delta':
            print(event.delta, end="", flush=True)
            response.append(event.delta)
            final_response_in_one_line = " ".join(response)
    chat_history.append(
        {
            "role" : "assistant",
            "content" : final_response_in_one_line,
        },
    )

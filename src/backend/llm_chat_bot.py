from openai import OpenAI
from utils.contants import base_url,api_key,text_embedding_api_key
from src.backend.rag import get_relevant_document_using_rag_in_langchain
from src.backend.evaluate_rag import evaluate_rag_without_llm


client = OpenAI(api_key=api_key,base_url=base_url)

chat_history = []
def generate_chatbot_response_without_rag(question):
    # question = ''
    print("Generate response started")
    if question.lower() != 'exit':
        # question = input("type your question...")
        chat_history.append(
            {
                "role" : "user",
                "content" : question
            }
        )
        bot = client.chat.completions.create(
                model= "gpt-4o-mini",
                messages=chat_history,
                stream=True,
                # temperature = 1,
                # top_p=1,
                # frequency_penalty=1,
                # presence_penalty=1,
                max_completion_tokens=255
            )
        response_list = []
        for chunk in bot:
            delta = chunk.choices[0].delta
            if delta.content is not None:
                print(delta.content, end="", flush=True)
                response_list.append(delta.content)
        final_response_in_oneline = " ".join(response_list)
        chat_history.append(
            {
                "role" : "assistant",
                "content" : final_response_in_oneline
            }
        )
    return final_response_in_oneline

################################################

# question = ''
#     chat_history = []
#     output_to_process = []
#     output_dict = {}
#     while question.lower() != 'exit':
#         question = input("\n type your question...")
#         if question.lower() != 'exit':
#             relevant_doc = get_relevant_document_using_rag_in_langchain(
#                 question=question, 
#                 open_ai_key = text_embedding_api_key, 
#                 base_url=base_url
#             )
#         else : relevant_doc = ''
#         chat_history.append({
#                 "role" : "user",
#                 "content" : relevant_doc
#             })
#         chat_history.append(
#             {
#                 "role" : "user",
#                 "content" : question
#             }
#         )
#         bot = client.responses.create(
#                 model= "llama-3.2-1b-instruct",
#                 input = chat_history,
#                 stream=True,
#                 temperature = 0,
#                 # top_p=1,
#                 max_output_tokens=250,
#             )
        
#         response = []
#         for event in bot:
#             if event.type == 'response.output_text.delta':
#                 print(event.delta, end="", flush=True)
#                 response.append(event.delta)
#                 final_response_in_one_line = " ".join(response)
#         chat_history.append(
#             {
#                 "role" : "assistant",
#                 "content" : final_response_in_one_line,
#             },
#         )
#         output_dict = {
#             "user_input": question,
#             "retrieved_contexts": relevant_doc,
#             # "reference": "George Orwell",
#             "response": final_response_in_one_line
#         }
#         output_to_process.append(output_dict)

def generate_chatbot_response(question):
    chat_history = []
    output_to_process = []
    output_dict = {}
    if question.lower() != 'exit':
        # question = input("\n type your question...")
        if question.lower() != 'exit':
            relevant_doc = get_relevant_document_using_rag_in_langchain(
                question=question, 
                open_ai_key = text_embedding_api_key, 
                base_url=base_url
            )
        else : relevant_doc = ''
        chat_history.append({
                "role" : "user",
                "content" : relevant_doc
            })
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
        output_dict = {
            "user_input": question,
            "retrieved_contexts": relevant_doc,
            # "reference": "George Orwell",
            "response": final_response_in_one_line
        }
        output_to_process.append(output_dict)
        print(final_response_in_one_line)
        return final_response_in_one_line


# evaluate_rag_without_llm(output_to_process)

from openai import OpenAI
from contants import base_url,api_key,open_ai_key,text_embedding_api_key
from rag import get_relevant_document_using_rag_in_langchain
from evaluate_rag import evaluate_rag_without_llm


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
output_to_process = []
output_dict = {}
while question.lower() != 'exit':
    question = input("\n type your question...")
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


evaluate_rag_without_llm(chat_history)

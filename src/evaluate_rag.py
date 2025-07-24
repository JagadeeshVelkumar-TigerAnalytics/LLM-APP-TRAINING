from ragas import EvaluationDataset
from ragas import evaluate
from ragas.metrics import Faithfulness, FactualCorrectness, LLMContextRecall
from ragas.llms import LangchainLLMWrapper
from langchain_openai import ChatOpenAI
from contants import base_url

def evaluate_rag_without_llm(dataset):
    print("printing ragas")
    
    evaluation_dataset = EvaluationDataset.from_list(data=dataset)
    print(evaluation_dataset)

    result = evaluate(dataset=evaluation_dataset,
             metrics=[Faithfulness(),FactualCorrectness(),LLMContextRecall()],
             llm=LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini",base_url=base_url))
             )
    print(result)



dataset = [
    {
        "user_input": "Who wrote the novel '1984'?",
        "retrieved_contexts": [
            "George Orwell was an English novelist and essayist, journalist and critic.",
            "'1984' is a dystopian novel set in Airstrip One, a province of the superstate Oceania."
        ],
        "reference": "George Orwell",
        "response": "George Orwell"
    },
    {
        "user_input": "What is the capital of France?",
        "retrieved_contexts": [
            "Paris is the capital and most populous city of France.",
            "France is a country in Western Europe."
        ],
        "reference": "Paris",
        "response": "Paris"
    },
    {
        "user_input": "When did the Apollo 11 mission land on the moon?",
        "retrieved_contexts": [
            "Apollo 11 was the spaceflight that first landed humans on the Moon.",
            "Commander Neil Armstrong and lunar module pilot Buzz Aldrin landed the Apollo Lunar Module Eagle on July 20, 1969."
        ],
        "reference": "July 20, 1969",
        "response": "July 20, 1969"
    }
]


evaluate_rag_without_llm(dataset)
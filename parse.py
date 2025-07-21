from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def get_llm(backend="ollama"):
    if backend == "openai":
        return ChatOpenAI(model="gpt-4o-mini", openai_api_key=OPENAI_API_KEY)
    else:
        return OllamaLLM(model="gemma3")

def parse_with_ai(dom_chunks, parse_description, backend="ollama"):
    llm = get_llm(backend)
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        # If response is an AIMessage, extract .content; else, use as is
        if hasattr(response, 'content'):
            parsed_results.append(response.content)
        else:
            parsed_results.append(str(response))
    
    return "\n".join(parsed_results)
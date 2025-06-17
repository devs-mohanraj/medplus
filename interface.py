from langchain.schema.runnable import RunnablePassthrough, RunnableParallel
from langchain.schema.output_parser import StrOutputParser
from retriever import retriever
from build_chain import prompt
import requests
import os
import json

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable is not set. Please set it with your Together AI API key.")

def format_prompt(inputs):
    context = "\n".join(doc.page_content for doc in inputs["context"])
    formatted_prompt = prompt.format(context=context, query=inputs["query"])
    return formatted_prompt

def call_together_api(formatted_prompt):
    try:
        response = requests.post(
            "https://api.together.xyz/v1/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },            json={
                "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",  # Using Mixtral which is always available
                "prompt": formatted_prompt,
                "max_tokens": 256,
                "temperature": 0.7,
            },
            timeout=30
        )
        if response.status_code != 200:
            raise ValueError(f"API returned status code {response.status_code}: {response.text}")
            
        response_json = response.json()
        if "choices" not in response_json or not response_json["choices"]:
            raise ValueError(f"Unexpected API response format: {response_json}")
            
        return response_json["choices"][0]["text"]
        
    except requests.exceptions.RequestException as e:
        raise ValueError(f"API request failed: {str(e)}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON response: {response.text}")
    except Exception as e:
        raise ValueError(f"Error calling Together API: {str(e)}")

retrieval_chain = RunnableParallel(
    context=retriever,
    query=RunnablePassthrough()
)

# Build the full chain
rag_chain = (
    retrieval_chain 
    | format_prompt
    | call_together_api
    | StrOutputParser()
)

def process_query(query: str) -> str:
    """Process a single query through the RAG chain"""
    return rag_chain.invoke(query)

if __name__ == "__main__":
    print("Medical Knowledge Base Q&A System")
    print("Type 'quit' to exit")
    print("-" * 50)
    
    # Verify API key is set
    if not api_key:
        print("Error: Please set your Together AI API key first:")
        print("$env:API_KEY = 'your-api-key-here'")
        exit(1)
    
    while True:
        query = input("\nEnter your medical question: ")
        if query.lower() == 'quit':
            break
            
        try:
            response = process_query(query)
            print("\nResponse:", response)
        except Exception as e:
            print(f"Error: {str(e)}")

from prompts import system_prompt
from call_function import available_functions
from google.genai import types
import argparse
import os
from google import genai
from dotenv import load_dotenv

def main():
    parser = argparse.ArgumentParser(description="Povezivanje sa Gemini AI")
    parser.add_argument("user_prompt", type=str, help="Pitanje koje zelis da postavis AI modelu")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("Nije pronadjen GEMINI_API_KEY! Proveri da li tvoj .env fajl postoji i da li je ispravno napisan.")
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents = messages,
        config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt,temperature=0),
    )
    if response.usage_metadata is None:
        raise RuntimeError("No data of tokens.")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(response.text)

if __name__ == "__main__":
    main()

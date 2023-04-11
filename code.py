import random 
import json

print("Hello. Here are the options we have for you to select. \n")
print("1. Give me a random quote\n" "2. I want to add a new quote")

questions = int(input("> "))
if questions == 1:
    
    def read_quotes_from_json(quotes):
        with open('D:\Emotion Detection Chatbot\src\classwork\quotes.json', 'r', encoding='utf-8') as f:
            quotes = json.load(f)
        return quotes

    def get_random_quote(quotes):
        return random.choice(quotes)

    def main():
        import random
        file_name = "quotes.json"
        quotes = read_quotes_from_json(file_name)
        if quotes:
            quote = get_random_quote(quotes)
            print("Quote: ", quote["quote"])
            print("Author: ", quote["author"])
        else:
            print("No quotes found in the file.")

    if __name__ == "__main__":
        main()

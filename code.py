import json
import random

file_name = r"C:\Users\Acity\Videos\classwork\quotes.json"  # Update this with the correct file path

def read_quotes_from_json(file_name):
    """Reads quotes from a JSON file and returns a list of dictionaries containing the quote and its author."""
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)   
        quotes = data["quotes"]
    return quotes
def get_random_quote(quotes):
    """Returns a random quote from a list of quotes."""
    return random.choice(quotes)

def add_new_quote(quotes, quote, author):
    """Adds a new quote and its author to the list of quotes already available."""
    new_quote = {"quote": quote, "author": author}
    quotes.append(new_quote)

def save_quotes_to_json(file_name, quotes):
    """Saves the list of quotes to a JSON file."""
    data = {"quotes": quotes}
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def main():
    """Main function that interacts with the user and performs the desired operation."""
    file_name = "quotes.json"  # Update this with the name of your JSON file
    quotes = read_quotes_from_json(file_name)
    while True:
        print("1. Generate a random quote")  #Generates a random quote from the list
        print("2. Input a new quote")        #Enter or input a new quote
        print("3. Exit")                     
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            if quotes:
                quote = get_random_quote(quotes)
                print("Quote: ", quote["quote"])
                print("Author: ", quote["author"]) 
            else:
                print("No quotes found in the file.")
        elif choice == "2":
            quote = input("Enter the quote: ")
            author = input("Enter the author: ")
            add_new_quote(quotes, quote, author)
            save_quotes_to_json(file_name, quotes)
            print("Quote added successfully!")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



from stats import getNumWords;
from stats import getNumChars;

def get_book_text(path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        path (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Book file not found."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = getNumWords(text)
    print(f"{num_words} words found in the document.")
    getNumChars(text)
    print(getNumChars(text))

if __name__ == "__main__":
    main()
# This script reads the content of a book file and prints it to the console.
# It handles file not found errors and other exceptions gracefully.
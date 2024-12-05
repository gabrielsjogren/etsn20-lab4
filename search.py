import sys

def search(word_to_search, file_to_search):
    try:
        with open(file_to_search, "r") as file:
            for line in file:
                if word_to_search in line:
                    print(line)
    except FileNotFoundError:
        print(f"File {file_to_search} not found. please make sure the file exists. ")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Parse args
    word_to_search = sys.argv[1]
    file_to_search = sys.argv[2]
    search(word_to_search, file_to_search)
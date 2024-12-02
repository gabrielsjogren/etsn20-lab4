import sys

def main(word_to_search, file_to_search):
    with open(file_to_search, "r") as file:
        for line in file:
            if word_to_search in line:
                print(line)

if __name__ == "__main__":
    # Parse args
    word_to_search = sys.argv[1]
    file_to_search = sys.argv[2]
    main(word_to_search, file_to_search)
import requests
import sys

print("\n\033[36mWelcome to Scrape-Html-Into-A-Text-file (S.H.I.T.)\033[0m")

banner = f'''
{"="*70}
\033[33m                           ( \_
                         _(\_\\)_\033[0m       \033[36m     Made by\033[0m
\033[33m                        (S.H.I.T.)\033[0m       \033[36m   K2SOsint\033[0m
\033[33m                      ((____\_____))\033[0m
{"="*70}
'''

print(banner)

print("A small script for scraping HTML code from a webpage and saving it\ninto a text file called"
      " \033[33;1mshit.txt\033[0m or \033[33;1mshit.html\033[0m. After scraping,\nit's possible to "
      "search for a word in the file.\n\n\033[33;1m(*)\033[0m Please note that searching is case sensitive."
      "\n\033[33;1m(*)\033[0m Use this script with respect to the Terms of Service of websites.\n")

# Function to save content into a file
def save_content(filename, content):
    with open(filename, "w", encoding="utf-8") as filehandler:
        filehandler.write(content)
        filehandler.close()

# Function to collect data from the given URL and handle errors
def collection(url, filetype):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        print("\nStatus for", url, "is OK. The response is:\033[33;1m", response.status_code, "\033[0m")
        print("Processing your S.H.I.T. request into output...\n")
        filename = "shit.html" if filetype == "html" else "shit.txt"
        save_content(filename, response.text)
        print(f"Please find the text file called '{filename}' in the same directory as where you ran this Python script.\n")
        return filename
    except requests.exceptions.RequestException as e:
        print("\nThe S.H.I.T. has hit the fan.\nError occurred during the request:", str(e), "\n")
        sys.exit(1)
    except Exception as e:
        print("\nAn unexpected error occurred:", str(e), "\n")
        sys.exit(1)

url = str(input("What is the \033[33;1mURL\033[0m of the page to be scraped (\033[33;1minclude https://\033[0m) : "))
filetype = str(input("In what \033[33;1mfiletype\033[0m should it be saved (html or txt) : "))

filename = collection(url, filetype)

question = str(input("Do you want to search within the file? (y/n) : "))

if question == "y":
    def searching():
        # input for searching for a word in the file
        word = str(input("Please enter the word you are searching for within this file: "))
        found = False
        try:
            with open(filename, 'r', encoding="utf-8") as wp:
                # read all lines in a list
                lines = wp.readlines()
                for line in lines:
                    # check if word exists in file
                    if line.find(word) != -1:
                        if not found:
                            print(f'You have searched for: {word}. It exists in the file on the following lines:')
                        print("Line:", lines.index(line), line.strip())
                        found = True
            if not found:
                print(f'The word "{word}" was not found in the file.')
        except FileNotFoundError:
            print(f"The file '{filename}' does not exist.")
        except Exception as e:
            print("\nAn unexpected error occurred while searching:", str(e))

    searching()

else:
    print("Thank you for using S.H.I.T. and have a great day! ~ MIT License ~ (c)2023 K2OSINT")

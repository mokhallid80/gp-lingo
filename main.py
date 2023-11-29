import yaml
from openai import OpenAI

# open the yaml configs file to get our api key
with open("configs.yaml", "r") as configs_file:
    try:
        configs = yaml.safe_load(configs_file)
    except yaml.YAMLError as exc:
        print(exc) # replace it with a logger and stop execution

# assign our constant secret api key
API_KEY = configs["API_KEY"]



# get the category and language inputs from the user
category = str(input("Please write a category that you would like to learn new words about:- "))
lang = str(input("Please choose the language:- "))
print(f"You chose {category} in {lang}")

# open a client connection with chatGPT
client = OpenAI(
    api_key = API_KEY
)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": f"Tell me popular words that I need to know for {category} in {lang}. Give me all words in the same sentence and seprate them with a ','. Don't add any extra stuff to the response. Nothing else"},
  ]
)

choice = response.choices[0]
words = (choice.message.content).split(",")

word_i = 1
print(f"Here is some popular words for {category} in {lang}")
for word in words:
    print(f"{word_i} {word}")
    word_i += 1


chosen_word_index = int(input("Choose a word by its number:- ")) - 1
print(f"You choose {words[chosen_word_index]}")


response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": f"Put the word {words[chosen_word_index]} in a sentence related to {category}"},
  ]
)
choice = response.choices[0]
response = choice.message.content

print(response)
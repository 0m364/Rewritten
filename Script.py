import openai

def get_api_key():
    api_key = input("Enter your OpenAI API key: ")
    return api_key

def rewrite_file(api_key, filepath):
    openai.api_key = api_key
    # Read file content
    with open(filepath, 'r') as file:
        data = file.read()
    # Include the read data in your prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Rewrite this file:\n" + data,
    )
    filename = "rewritten"
    with open(filename, "w") as f:
        f.write(response.choices[0].text.strip())
    print(f"File saved as {filename}")

def custom_prompt(api_key):
    openai.api_key = api_key
    prompt = input("What would you ask chatgpt? ")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
    )
    filename = "chat"
    with open(filename, "w") as f:
        f.write(response.choices[0].text.strip())
    print(f"File saved as {filename}")

def main():
    api_key = get_api_key()
    choice = input("Would you like to rewrite a file (rewrite) or ask a custom prompt (custom)? ")
    if choice == "rewrite":
        filepath = input("Enter the filepath of the file you want to rewrite: ")
        rewrite_file(api_key, filepath)
    elif choice == "custom":
        custom_prompt(api_key)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

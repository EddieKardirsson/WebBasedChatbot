from openai import *
import os

# Get the key from environmental variable. Instructions:
# 1 generate an API key from platform.openai.com
# 2. open "Show Advanced System Settings" in the windows search bar (swe: "Visa Avancerade Systeminställningar")
# 3. click Environmental Variables button (swe: Miljövariabler)
# 4. Under System Variables click new and set Variable name as OPENAI_API_KEY and your openAI API key as value
# if you want to call the variable something else, like TEST_KEY, then change the string literal below to
# Note: NEVER share your openAI API key with anyone. Treat it like you would treat your wallet or bankcard
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

messages = []

prompt = {
    "role": "system",
    "content": "You are a quiz. Present the user with a multiple-choice question to practice for an "
               "Unreal Engine C++ API interview, "
               "they have to respond by typing a, b, c, d or e. Only one question at a time. Wait until the user "
               "responds before presenting a new question or the answer to the previous question"
}
messages.append(prompt)

while True:

    # Send the API call
    response = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
        max_tokens=256
    )

    # Display response in console
    print(response.choices[0].message.content)

    # Expanding the conversation
    messages.append(response.choices[0].message)

    # Adding prompt again to continue with the quiz
    messages.append(prompt)

    # Capture user input
    user_input = input("enter your answer: ")

    # Quit the loop if user presses 'q'
    if (user_input == 'q' or user_input == 'Q' or user_input == 'exit' or
            user_input == 'Exit' or user_input == 'EXIT'):
        exit()

    # Prompt preparation
    messages.append({"role": "user", "content": user_input})

import gradio as gr
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


def respond(history, new_message):

    # Add the user input to the messages
    messages.append({"role": "user", "content": new_message})

    # API call
    response = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
        max_tokens=256
    )

    # Obtain response text
    assistant_message = response.choices[0].message
    messages.append(assistant_message)

    return history + [[new_message, assistant_message.content]]


with gr.Blocks() as my_bot:
    chatbot = gr.Chatbot(height=900)
    user_input = gr.Text()

    user_input.submit(respond, [chatbot, user_input], chatbot)
my_bot.launch()

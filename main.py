import openai
import gradio


openai.api_key = "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"

messages = [{"role": "system", "content": "You are a mental health advisor name 'mental health buddy' that helps college students deal with their mental health as well as make appointments with guidence counselors in their college. "}]

def CustomChatGPT(You):
    messages.append({"role": "user", "content": You})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Mental Health Buddy")


demo.launch(share=True)


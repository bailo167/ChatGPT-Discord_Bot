import discord
import openai

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

openai.api_key = "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"

def generate_response(prompt):
    model_engine = "text-davinci-002"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = generate_response(message.content)
    await message.channel.send(response)

client.run("qr4O_6TTgVGKJbT7WXmTSOXELcCgxwqG")
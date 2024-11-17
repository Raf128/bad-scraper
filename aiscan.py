#I can't freaking test this bc I don't have a phone number to get an api key, use at your own risk.
#use 0.28 bc I don't feel like fixing it
import os
try:
    import openai
except:
    aiInstall = input('Openai Package is not installed, Install? y/n\n')
    if aiInstall.lower() == "y":
        try:
            os.system('pip install openai==0.28')
            import openai
        except Exception as e:
            print("Error Installing", e)
            exit(2)
    else:
        exit(1)

model = input('Enter your chat api model (gpt-4o, gpt-4 etc.). Defalts to gpt-4o-mini\n')

if not model:
    model = 'gpt-4o-mini'

try:
    data = open('data.txt').read()
except Exception as e:
    print('Error reading data.txt, did you run main.py?\n', e)

def chat():
    history = []

    while True:
        userPrompt = input('You: ')

        if userPrompt.lower() == 'done':
            print(history)
            exit(1)

        if 'scan' in userPrompt.lower():
            userPrompt += data
        
        #Pretty Sure this is JSON (I know it's JSON)
        history.append({"role": "user", "content": userPrompt})
        
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages = history
            )
        except Exception as e:
            print('\nError connecting to OpenAi:', e)
            exit(2)
            
        message = response['choices'][0]['message']['content']
        print(f"Bot: {message}")
        history.append({"role": "assistant", "content": message})


aiKey = input('Please input an OpenAi key, it will not be stored. I pwomise!\n')

openai.api_key = aiKey

print('\nUse "done" to stop, "scan" to read data.txt.\n')

chat()
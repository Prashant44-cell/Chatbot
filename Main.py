import ollama # AI bot with 14B paramters
from colorama import init, Fore, Style # for styling
import pyttsx3 #This is used for voice speech
import cgi # Used for  UI

# #This is text to speech code using pyttsx3
# engine=pyttsx3.init() # to initite pyttx3
# engine.say("Hello I am Vyahant. ")
# engine.runAndWait()
# engine.say("I am a Chatbot develop by Prashant Gupta")

# Initialize colorama
init()


system_prompt = "You are a helpful, polite, and intelligent assistant. Answer all questions clearly and with context."

# Track conversation history
messages = [
    {"role": "system", "content": system_prompt}
]

def chat_with_phi3(user_input):
    messages.append({"role": "user", "content": user_input})
    try:
        short_context = [messages[0]] + messages[-4:] 
        response = ollama.chat(model='phi3', messages=short_context)

        reply = response['message']['content'].strip()
        messages.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(Fore.GREEN + "🤖 How can i assist you  " + Style.RESET_ALL)
    while True:
        user_input = input(Fore.YELLOW + "You: " + Style.RESET_ALL).strip()
        if user_input.lower() in ["exit", "quit", "bye"]:
            print(Fore.GREEN + "Chatbot: See you Again, Goodbye! 👋" + Style.RESET_ALL)
            break
        response = chat_with_phi3(user_input)
        print(Fore.GREEN + "Chatbot:", response + Style.RESET_ALL)


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "training_data.txt"

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend 😃",
])
trainer.train([
    "How are you?",
    "I'm good.",
])
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])
# cleaned_corpus = clean_corpus(CORPUS_FILE)
# trainer.train(cleaned_corpus)

exit_conditions = (":q", "quit", "exit")

while True:
    query = input(">>> ")
    if query in exit_conditions:
        break
    else:
        print(f"🌱 {chatbot.get_response(query)}")

import nltk
from nltk.chat.util import Chat, reflections

#Create questions and answers we expect the user to ask

Questions_And_Answers=[(r"Hello|Hi|Hey",
                      ["Hello, how can I help you?"]),
                        (r"I would like to know how the weather will be tomorrow?",
                      ["Well, the weather reports that it's going to be sunny all week"]),
                        (r"What do you suggest for me to wear?",
                      ["I'd say wear a basic t-shirt or shirt and a pair of trousers"]),
                        (r"I think I'll go with this ,thank you",
                      ["Glad that I helped! do you need to ask about anything else?"]),
                        (r"Who's the president of the united states?",
                      ["The current president of the united states is Joe Biden"]),
                        (r"Okay, thanks a lot for your help now I'm done",
                      ["No need, whenever you need my assistance ,type in!"])]
    
print("Start a chat by entering a prompt")
chat= Chat(Questions_And_Answers)
chat.converse()

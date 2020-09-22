def chatterbotx():
    import chatterbot
    from chatterbot.trainers import ChatterBotCorpusTrainer
    from chatterbot import ChatBot # import the chatbot
    from chatterbot.logic import LogicAdapter
    from chatterbot import filters
    import time
    import random

    chatbot = ChatBot('Chatterbot')

    #training the chatbot with data corpus (it contains alot of phrases and stuff)
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.english')

    #stores data in file so that it can remember
    trainer.export_for_training('./my_export.json')

    while True:
        request = input('You: ')
        response = chatbot.get_response(request)

        if chatbot.confidence > 0.80:    #remove if dont work
            print('Chatterbot: ' + response)
        if chatbot.confidence < 0.80:    #remove if dont work
            print("Chatterbot: Sorry, I don't quite understand.")

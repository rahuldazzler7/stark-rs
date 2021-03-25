from decison_controllers.speaker import speak, take_speech, speech_control, wish_me
from decison_controllers.io import decision_divider
from os import environ as env
import random
from train_stark.model_trainer import TrainBot
from decison_controllers.decision_out import bag_of_words
import numpy

tb = TrainBot(end_point=env['OVERRIDE_S3_ENDPOINT'], aws_access=env['access'], aws_secret=env['secret'],
              region_name=env['region'])
data = tb.read_json(bucket_name=env['SOURCE_BUCKET'], json_key=env['JSON_KEY'])
words, labels, tb_model = tb.generate_network(data=data)


def initialize_app():
    speak(f"Hi {env['ME']} , I am Stark")
    wish_me()
    try:
        tb_model.load(f"{env['MODEL']}")
        print("Start talking with the bot (type quit to stop)!")
        while True:
            inp = take_speech()
            if inp.lower() == "quit" or inp.lower() == "shutdown" or inp.lower() == "close":
                break
            results = tb_model.predict([bag_of_words(inp, words)])
            results_index = numpy.argmax(results)
            tag = labels[results_index]
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            reply = f"{random.choice(responses)}"
            decision_divider(inp.lower(), reply)
    except Exception as err:
        decision_divider("Did not understand", "Did not understand")
        return "Did not understand"


if __name__ == '__main__':
    initialize_app()

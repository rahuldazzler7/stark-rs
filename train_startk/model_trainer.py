import tflearn
from tensorflow.python.framework import ops
import nltk
from nltk.stem.lancaster import LancasterStemmer
import boto3
from botocore.client import Config
import json
from tflearn import DNN
from os import environ as env


class TrainBot:
    stemmer = LancasterStemmer()
    labels, words, docs_x, docs_y, training, output = ([] for i in range(6))

    def __init__(self, aws_secret: str = None, aws_access: str = None, end_point: str = None, region_name: str = None):
        if end_point is not None:
            self.__s3_resource = boto3.resource('s3', endpoint_url=end_point,
                                                aws_access_key_id=aws_access,
                                                aws_secret_access_key=aws_secret,
                                                region_name=region_name,
                                                config=Config(signature_version='s3v4'))

        else:
            self.__s3_resource = boto3.resource('s3')

    def read_json(self, bucket_name: str, json_key: str):
        file_to_read = json.load(
            self.__s3_resource.Object(bucket_name, f"{json_key}").get()['Body'])
        return file_to_read

    def pattern_evaluation(self, data: dict):
        for intent in data['intents']:
            for pattern in intent['patterns']:
                wrds = nltk.word_tokenize(pattern)
                self.words.extend(wrds)
                self.docs_x.append(wrds)
                self.docs_y.append(intent["tag"])
            self.labels.append(intent["tag"]) if intent["tag"] not in self.labels else None
        self.words = [self.stemmer.stem(w.lower()) for w in self.words if w != "?"]
        self.words = sorted(list(set(self.words)))
        self.labels = sorted(self.labels)

    def training_evaluation(self):
        out_empty = [0 for _ in range(len(self.labels))]
        for x, doc in enumerate(self.docs_x):
            bag = []
            wrds = [self.stemmer.stem(w.lower()) for w in doc]
            for w in self.words:
                bag.append(1) if w in wrds else bag.append(0)
            output_row = out_empty[:]
            output_row[self.labels.index(self.docs_y[x])] = 1
            self.training.append(bag)
            self.output.append(output_row)
        ops.reset_default_graph()

    def generate_network(self, data: dict):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        self.pattern_evaluation(data=data)
        self.training_evaluation()
        net = tflearn.input_data(shape=[None, len(self.training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net: object = tflearn.fully_connected(net, len(self.output[0]), activation="softmax")
        net = tflearn.regression(net)
        model: DNN = tflearn.DNN(net)
        return self.words, self.labels, model

    def save_model(self):
        data = self.read_json(bucket_name=env['SOURCE_BUCKET'], json_key=env['JSON_KEY'])
        a, b, model = self. generate_network(data= data)
        model.fit(self.training, self.output, n_epoch=1000, batch_size=8, show_metric=True)
        model.save(f"{env['MODEL']}")


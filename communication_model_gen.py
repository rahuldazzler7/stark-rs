from  train_stark.model_trainer import TrainBot
from os import environ as env

tb = TrainBot(end_point=env['OVERRIDE_S3_ENDPOINT'], aws_access=env['access'], aws_secret=env['secret'],
                  region_name=env['region'])
tb.save_model()
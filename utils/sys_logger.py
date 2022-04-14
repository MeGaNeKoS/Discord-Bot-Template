""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.0
"""
import logging


class STDERRLogger:
    def __init__(self):
        self.logger = logging.getLogger("STDERR")
        formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

        file_handler = logging.FileHandler('stderr.log')
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

        self.buf = []

    def write(self, msg):

        if msg.endswith('\n'):
            self.buf.append(msg.removesuffix('\n'))
            self.logger.error(''.join(self.buf))
            self.buf = []
        else:
            self.buf.append(msg)

    def flush(self):
        pass

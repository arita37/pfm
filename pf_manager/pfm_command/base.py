# from abc import ABCMeta, abstractmethod


class BaseCommand:
    def __init__(self, config):
        self.config = config

    #   @abstractmethod
    def run(self):
        pass
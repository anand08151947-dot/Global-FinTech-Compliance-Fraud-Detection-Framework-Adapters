from abc import ABC, abstractmethod

class BaseAdapter(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def fetch(self, query=None):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def validate(self, data):
        pass

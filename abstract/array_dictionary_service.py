from abc import ABC, abstractmethod


class array_dictionary_service(ABC):

    @abstractmethod
    def add(self, key, value):
        pass

    @abstractmethod
    def remove(self, key):
        pass

    @abstractmethod
    def contains_key(self, key):
        pass

    @abstractmethod
    def contains_value(self, value):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def clear(self):
        pass

from abc import ABC, abstractmethod


class calculate_service(ABC):

    @abstractmethod
    def check_regex_and_parentheses(self, input):
        pass

    @abstractmethod
    def check_parentheses_match(self, input):
        pass

    @abstractmethod
    def convert_infix_to_postfix(self, input):
        pass

    @abstractmethod
    def evaluate_postfix_expression(self, input):
        pass

    @abstractmethod
    def separate_the_input(self, input):
        pass

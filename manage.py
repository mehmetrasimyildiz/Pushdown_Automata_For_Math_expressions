import re
from calculate.calculatemanager import CalculatorManager

def main():
    calculator_manager = CalculatorManager()
    is_continue = True
    while is_continue:
        input_str = input("Lütfen bir ifade giriniz: ")
        is_true = calculator_manager.check_regex_and_parentheses(input_str)
        if not is_true:
            print("Söz dizilimi hatalıdır")
            continue

        input_str = calculator_manager.seperate_the_input(input_str)
        print("Girdiniz: " + input_str)
        input_str = calculator_manager.convert_infix_to_postfix(input_str)
        try:
            result = calculator_manager.evaluate_postfix_expression(input_str)
        except ValueError as e:
            print(e)
            continue
        print("\nSöz dizilimi doğru: " + str(result))
        print("Devam etmek için <Enter> tuşuna basınız\nDevam etmek istemiyorsanız farklı bir tuşa basınız")
        user_input = input()
        if user_input:
            is_continue = False
        else:
            print("tekrar giriniz")
    print("hatalı girdi")

if __name__ == "__main__":
    main()

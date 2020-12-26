from googletrans import Translator
import random
import string

def menu():
    print("[1] Reverse your message")
    print("[2] Translate your message to another language")
    print("[3] English to Pig Latin")
    print("[4] Password Generator")
    print("[5] Exit")


menu()
option = int(input("Enter the number which corresponds to the subject that you need help with: "))
print(" ")


def reverse_string(x):
    return x[::-1]


while option != 0:
    if option == 1:
        print("You have chosen to reverse your message")
        print(" ")
        print("Enter your message below,")
        message = input("Message: ")
        print(" ")
        reversedMessage = reverse_string(message)
        print(reversedMessage)

####################################################################################################################

    elif option == 2:
        print("You have chosen to translate a message ")
        print(" ")
        print("Here are the languages supported: ")

        def language_menu():
            print("[1] Russian")
            print("[2] Spanish")
            print("[3] German")
            print("[4] Japanese")
            print("[5] Chinese")
            print("[6] French")
            print("[7] Dutch")
            print("[8] Korean")
            print("[9] English")
            print("")

        language_menu()
        language = int(input("Enter the number which corresponds to the language that you would like to translate your message to: "))

        while language != 0:
            if language == 1:
                translator = Translator()
                toRussian = input("Enter the message that you would like to translate to Russian: ")
                print(" ")
                translated = translator.translate(
                    toRussian, dest='ru'
                )
                print(f'{translated.origin} -> {translated.text}')
                exit()
            elif language == 2:
                translator = Translator()
                toSpanish = input("Enter the message that you would like to translate to Spanish: ")
                print(" ")
                translated = translator.translate(
                    toSpanish, dest='es'
                )
                print(f'{translated.origin} -> {translated.text}')
                exit()
            elif language == 3:
                translator = Translator()
                toGerman = input("Enter the message that you would like to translate to German: ")
                print(" ")
                translated = translator.translate(
                    toGerman, dest='de'
                )
                print(f'{translated.origin} -> {translated.text}')
                exit()
            elif language == 4:
                translator = Translator()
                toJapanese = input("Enter the message that you would like to translate to Japanese: ")
                print(" ")
                translated = translator.translate(
                    toJapanese, dest='ja'
                )
                print(f'{translated.origin} -> {translated.text}')
                exit()
            elif language == 5:
                translator = Translator()
                toChinese = input("Enter the message that you would like to translate to Chinese: ")
                print(" ")
                translated = translator.translate(
                    toChinese, dest='zh-cn'
                )
                print(f'{translated.origin} -> {translated.text}')
                exit()
            elif language == 6:
                translator = Translator()
                toFrench = input("Enter the message that you would like to translate to French: ")
                print(" ")
                translated = translator.translate(
                    toFrench, dest='fr'
                )
                print(f'{translated.origin} -> {translated.text}')
                exit()
            elif language == 7:
                translator = Translator()
                toDutch = input("Enter the message that you would like to translate to Dutch: ")
                print(" ")
                translated = translator.translate(
                    toDutch, dest='nl'
                )
                print(f'{translated.origin} -> {translated.text}')
                exit()
            elif language == 8:
                translator = Translator()
                toKorean = input("Enter the message that you would like to translate to Korean: ")
                print(" ")
                translated = translator.translate(
                    toKorean, dest='ko'
                )
                print(f'{translated.origin} -> {translated.text}')
                exit()
            elif language == 9:
                translator = Translator()
                toEnglish = input("Enter the message that you would like to translate to English: ")
                print(" ")
                translated = translator.translate(
                    toEnglish, dest='en'
                )
                print(f'{translated.origin} -> {translated.text}')
                exit()
            else:
                print("Invalid option, exiting the program.")
                exit()


####################################################################################################################

    elif option == 3:
        print("You have chosen English to Pig Latin")
        print(" ")
        print("Enter the two numbers that you're multiplying")
        print(" ")

        def main():
            words = str(input("Input Sentence:")).split()
            for word in words:
                print(word[1:] + word[0] + "ay", end=" ")
            print()

        main()
        exit()

####################################################################################################################

    elif option == 4:
        print("You have chosen password generator")
        print(" ")
        choice = input("Would you like 8 characters or 16 characters in your password?: ")

        print(" ")

        if int(choice) == 8:
            print(" ")


            def get_random_alphanumeric_string(letters_count, digits_count):
                sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
                sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

                # Convert string to list and shuffle it to mix letters and digits
                sample_list = list(sample_str)
                random.shuffle(sample_list)
                final_string = ''.join(sample_list)
                return final_string


            # 5 letters and 3 digits
            print("Your password is:", get_random_alphanumeric_string(5, 3))
            exit()

        elif int(choice) == 16:
            print(" ")


            def get_random_alphanumeric_string(letters_count, digits_count):
                sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
                sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

                # Convert string to list and shuffle it to mix letters and digits
                sample_list = list(sample_str)
                random.shuffle(sample_list)
                final_string = ''.join(sample_list)
                return final_string

            print("Your password is:", get_random_alphanumeric_string(10, 6))
            exit()
        else:
            print("Please re-run the program but enter a valid option.")
            exit()


####################################################################################################################

    elif option == 5:
        exit()
    else:
        print("Please run the program again and enter a valid option.")

    print()
    menu()
    option = int(input("Enter the number which corresponds to the subject that you need help with: "))
    print(" ")

print("Thanks for using this program!")




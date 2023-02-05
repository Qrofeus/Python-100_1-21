# Ask whether to encode or decode
# get message
# ask for encryption key
# perform operation
# ask to go again

from string import ascii_lowercase as characters


def operate(message, key, op_code):
    new_message = ""
    if op_code == "encode":
        for letter in message:
            if letter == " ":
                new_message += "-"
            else:
                new_message += characters[(characters.index(letter) + key) % 26]
    else:
        for letter in message:
            if letter == "-":
                new_message += " "
            else:
                new_message += characters[(characters.index(letter) - key) % 26]
    return new_message


if __name__ == '__main__':
    while True:
        op = input("Encode or Decode?\n>>").strip().lower()
        if op not in ["encode", "decode"]:
            print("Invalid input... Try again...")
            continue
        n_message = input("Write down your message:\n>>").strip().lower()
        n_key = int(input("Encryption key:\n>>").strip())
        # Perform error checks
        result = operate(n_message, n_key, op)
        print(f"Your message has been {op}d to: {result}")
        again = input("\nContinue running? 'yes' or 'no'\n>>").strip().lower()
        if again != "yes":
            break

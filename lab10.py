# Define the Morse code dictionary.
def make_morse_dict():
    morse_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'  # '/' shows space between words
    }
    return morse_dict
def modify_input(eng_text, morse_dict):
    eng_text = eng_text.lower()
    clean_eng_text = ""
    for letter in eng_text:
        if letter in morse_dict:
            clean_eng_text += letter
    return clean_eng_text

def to_morse_code(clean_eng_text, morse_dict):
    morse_code = []
    words = clean_eng_text.split()
    for i in range(len(words)):
        word = words[i]
        for j in range(len(word)):
            letter = word[j]
            morse_code.append(morse_dict[letter])
            if j < len(word) - 1:
                morse_code.append(" ")
            elif i < len(words) - 1:
                morse_code.append("//")
    return morse_code

def main():
    try:
        eng_text = input("Enter an English text: ").strip()
        if not eng_text:
            raise ValueError("Text cannot be empty")
    except Exception as e:
        print("Error with input:", e)
        return

    morse_dict = make_morse_dict()
    eng_text = modify_input(eng_text, morse_dict)
    morse_code = to_morse_code(eng_text, morse_dict)

    morse_text = " ".join(morse_code)
    print("Morse code:", morse_text)

main()




import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2)

def make_morse_dict():
    morse_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
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

def lights_on(color):
    pixels.fill(color)

def lights_off():
    pixels.fill((0, 0, 0))

def show_morse(morse_code, unit_time, color):
    for i in morse_code:
        if i == ".":
            lights_on(color)
            time.sleep(unit_time)
            lights_off()
            time.sleep(unit_time)
        elif i == "-":
            lights_on(color)
            time.sleep(unit_time * 3)
            lights_off()
            time.sleep(unit_time)
        elif i == " ":
            time.sleep(unit_time * 2)
        elif i == "//":
            time.sleep(unit_time * 6)
        else:
            for symbol in i:
                if symbol == ".":
                    lights_on(color)
                    time.sleep(unit_time)
                    lights_off()
                    time.sleep(unit_time)
                elif symbol == "-":
                    lights_on(color)
                    time.sleep(unit_time * 3)
                    lights_off()
                    time.sleep(unit_time)
    lights_off()

def main():
    while True:
        try:
            speed_input = input("Enter light speed (0 to 1): ").strip()
            if not speed_input:
                print("Speed cannot be empty, please enter a number between 0 and 1")
                continue
            unit_time = float(speed_input)
            if not (0 <= unit_time <= 1):
                print("Speed must be between 0 and 1, please try again")
                continue
            break
        except ValueError:
            print("Invalid speed format, please enter a number between 0 and 1")

    while True:
        try:
            eng_text = input("Enter an English text: ").strip()
            if not eng_text:
                print("Text cannot be empty, please enter some text")
                continue
            break
        except Exception as e:
            print("Error with text input, please try again:", e)

    valid_colors = ["red", "green", "blue"]
    while True:
        try:
            color_choice = input("Pick a color (red/green/blue): ").lower().strip()
            if not color_choice:
                print("Color cannot be empty, please enter red, green, or blue")
                continue
            if color_choice not in valid_colors:
                print("Invalid color, please enter red, green, or blue")
                continue
            break
        except Exception as e:
            print("Error with color input, please try again:", e)

    color = (255, 0, 0)
    if color_choice == "green":
        color = (0, 255, 0)
    elif color_choice == "blue":
        color = (0, 0, 255)

    morse_dict = make_morse_dict()
    eng_text = modify_input(eng_text, morse_dict)
    morse_code = to_morse_code(eng_text, morse_dict)
    show_morse(morse_code, unit_time, color)

    morse_text = " ".join(morse_code)
    print("Morse code:", morse_text)
    print("Done")

main()

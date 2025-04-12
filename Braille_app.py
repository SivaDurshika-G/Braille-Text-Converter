

def convert_to_braille(text):
    braille_dict = {
        'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋',
        'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
        'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
        's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
        'y': '⠽', 'z': '⠵', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙',
        '5': '⠑', '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
        ' ': ' ', '.': '⠨', ',': '⠂', '?': '⠦', '!': '⠖', '-': '⠤'
    }
    
    braille_text = ''.join(braille_dict.get(char, char) for char in text.lower())
    return braille_text

# Main Program
if __name__ == "__main__":
    user_input = input("Enter text to convert to Braille: ")
    braille_output = convert_to_braille(user_input)
    print("Braille Conversion: ", braille_output)

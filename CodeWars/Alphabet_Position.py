def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text_alpha_pos = ""
    text = text.lower()
    print(text)

    for x in text:
        if x.isalpha() and x is not ' ':
            text_alpha_pos = text_alpha_pos + str(alphabet.index(x) +1) + " " 
            
    text_alpha_pos = text_alpha_pos.strip()       
    return text_alpha_pos

result = alphabet_position("The sunset sets at twelve o' clock.")
print(result)

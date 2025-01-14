def custom_encoder(string):

    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    string = string.casefold()
    encode = []

    for character in string:
        i = 0
        if character not in reference_string:
            encode.append(-1)
        else:
            for letter in reference_string:
                if character == letter:
                    encode.append(i)
                    break
                else:
                    i += 1



    return encode






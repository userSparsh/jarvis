import re


def extract_yt_term(command):
    # define a regular expression pattern to capture the song name

    pattern = r'play\s+(.*?)\s+on\s+youtube'

    # use re.search to find the match in command

    match = re.search(pattern, command , re.IGNORECASE)

    # if a match is found ,return the extracted song anme; otherwise ,return None

    return match.group(1) if match else None

def remove_words(input_string, words_to_remove):
    #split the input string into words
    words = input_string.split()

    # remove unwanted words

    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # join the remaining words back into a string

    result_strings = ' '.join(filtered_words)
    return result_strings

'''
 example

input_string = "make a phone call to pappa"
words_to_remove = ['make','a','to','phone','call','send','message','whatsapp','']

result = remove_words(input_string,words_to_remove)
print(result)

'''
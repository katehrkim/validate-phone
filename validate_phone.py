import re
# Does a string contain a phone number?
def has_phone_number(input_string):
    return re.search('[0-9]{3}-[0-9]{3}-[0-9]{4}', input_string)

# Get a phone number back from a string
def get_phone_number(input_string):
    output = ''
    if has_phone_number(input_string):
        for char in input_string:
            if char == '-' or char.isnumeric():
                output += char
        return output
    return None

# Gets and returns all phone numbers from an inputed string
def get_all_phone_numbers(input_string):
    output = []
    word_list = input_string.split(', ')
    for word in word_list:
        if has_phone_number(word):
            output.append(word)
    return output

# Hide all numbers in a phone number except the last 4 digits. An example of this looks like: XXX-XXX-1234
def hide_phone_numbers(input_string):
    word_list = input_string.split(',')
    result = ''
    for word in word_list:
        output = ''
        for i, letter in enumerate(word):
            if re.search('[0-9]', letter) and i < 8:
                output += 'X'
            else:
                output += letter
        result += output
        result += ','
    result = result[0:-1]
    return result

# Get the string of the phone number and format it for our pretend application. Ensure all of the phone numbers use dashes for delimiters.
# Example: 312-111-2222, 312.111.2222, (312) 111-2222 would all be 312-111-2222
def format_phone_number(input_string):
    word_list = input_string.split(',')
    result = ''
    for word in word_list:
        output = ''
        for letter in word:
            if re.match('[0-9]', letter):
                output += letter
        for i in range(0, 3):
            result += output[i]
        result += '-'
        for i in range(3, 6):
            result += output[i]
        result += '-'
        for i in range(6, len(output)):
            result += output[i]
        result += ', '
    result = result[0:-2]
    return result

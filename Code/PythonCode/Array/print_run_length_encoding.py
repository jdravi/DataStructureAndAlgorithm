def encode(string):

    prev_char = string[0]
    count = 1
    result  = ""
    for char in string[1:]:
        if prev_char == char:
            count = count+1
        else:
            result = result + prev_char + str(count)
            prev_char = char
            count = 1
    result+=prev_char+str(count)
    return result

def run_encoding(string):
    char_array = [0]*26

    for char in string:
        index = ord(char)-97
        char_array[index] += 1

    result = ""
    index = 0
    while index<len(string):
        char  = string[index]
        result = result + char +str(char_array[ord(char)-97])
        index = index+char_array[ord(char)-97]
    return result


if __name__ == '__main__':
    string = "aaabcca"
    print(encode(string))
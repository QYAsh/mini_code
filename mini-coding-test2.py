unit_word_list = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ten_word_list = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
special_word_dict = {
    0:"zero",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    15:"fifteen",
    16:"sixteen",
    18:"eighteen"
}

def convert_digit_to_word(digit):
    try:
        digit = int(digit)
    except TypeError:
        print("Invalid input!")
    unit_place = digit%10
    ten_place = digit//10 
    
    if digit in special_word_dict.keys():
        word = special_word_dict[digit]
    elif digit < 10:
        word = unit_word_list[unit_place]
    elif digit < 20:
        word = unit_word_list[unit_place] + "teen"
    elif 20 <= digit <100:        
        if unit_place != 0:
            word = "%s-%s" % (ten_word_list[ten_place], unit_word_list[unit_place])
        else:
            word = ten_word_list[ten_place]
    else:
        print("Invalid input!")
    return word

if __name__ == "__main__":
    for i in range(0, 100):
        print("%d : %s" % (i, convert_digit_to_word(i)))

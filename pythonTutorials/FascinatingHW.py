import time

target_string = "Welcome to QBit!"
letters_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !?"


found_string = ""
for target_char in target_string:
    for possible_letter in letters_list:
        time.sleep(0.01)
        print(found_string+possible_letter)
        if possible_letter == target_char:
            found_string+=target_char
            break



# შექმენით ფუნქცია რომელიც არგუმენტად იღებს სტრინგს და აბრუნებს dictonary’ის რომელშიც ეწერება ასოების რაოდენობა ( მაგალითად “hello” -> {“h”:1,”e”:1,”l”:2,”o”:1}


def Character_count(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
            
    return count



print(Character_count('hello'))
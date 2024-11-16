# შექმენით ფუნქცია რომელიც არგუმენტად იღებს სტრინგს და აბრუნებს True თუ ყველა ასო უნიკალურია და False თუ კი რომელიმე ასო დუბლირდება

def Unique_character(s):
    if len(s) == len(set(s)):
        return True
    else:
        return False
    
print(Unique_character("abc"))
print(Unique_character("abccbc"))
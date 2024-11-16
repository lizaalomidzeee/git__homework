# შექმენით ფუნქცია, რომელიც არგუმენტად იღებს სტრინგს და აბრუნებს მის შემოტრიალებულ ვერსიას ( არ გამოიყენოთ ჩაშენებული რევერსინგი )

def Reverse_string(s):
    reverse_string = ""
    for i in s:
        reverse_string = i + reverse_string
        
    return reverse_string


print(Reverse_string("hello"))
def sanitize_text(text):
    text = text.replace('@marcusgabrields', '')
    text = text.strip()

    if len(text) > 280 or text.isdigit() is False:
        return None
    
    return int(text) 


def fizzbuzz(text):
    num = sanitize_text(text)

    if num is None:
        return None
     
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


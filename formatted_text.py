# Напишите функцию, которая отображает на экран
# форматированный текст:
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
# Bill Gates

def formatted_text():
    """Return text in a given format"""
    first_string = "\"Don't compare yourself with anyone in this world…"
    second_string = "if you do so, you are insulting yourself.\""
    last_string = "Bill Gates"
    text = "\x1B[3m" + first_string + "\n" + second_string +  "\n\t\t\t\t\t" + last_string + "\x1B[0m"
    return text

print(formatted_text())
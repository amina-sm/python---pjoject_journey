def format_name(  f_name,l_name):
    formatted_f_name= f_name.title()
    formatted_l_name=l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("what is your name? "),input("what is your name? ")))
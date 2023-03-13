# Functions with inputs
#def my_function(something):
# Do this with somthing
# Then do this
# Finally do this

# def my_function():
#     result = 3 * 2
#     return result

# output = my_function()

# Functions with Outputs


# def format_name(f_name, l_name):
#     # f_name = input("What is your first name? ")
#     # l_name = input("What is your last name? ")
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     # print(f"{formated_f_name} {formated_l_name}")
#     return f"{formated_f_name} {formated_l_name}"

# formated_string = format_name("Gary", "Blueberry")
# print(formated_string)
# # format_name("Gary", "Blueberry")

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
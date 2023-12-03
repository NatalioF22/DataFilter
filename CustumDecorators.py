from ColoredText import TerminalColors

#keyboard interrupt
def handle_keyboard_interrupt():

    print(TerminalColors.CYAN + "\n\nPlease Enter '>q' or '>Q' to exit the Program\n" + TerminalColors.RESET)


def wrapped_function(function_name, *args, **kwargs):
   
    try:
        return function_name(*args, **kwargs)
    except KeyboardInterrupt:
        handle_keyboard_interrupt()


def keyboard_interrupt_handler(function_name):
   
    return lambda *args, **kwargs: wrapped_function(function_name, *args, **kwargs)


#value error handler

def print_value_error_message():
    print(TerminalColors.RED + "\n\nPLEASE ENTER ONLY INTEGERS ACCORDING TO THE INSTRUCTIONS, ANYTHING ELSE WILL BE IGNORED\n" + TerminalColors.RESET)

def handle_value_error(function_name):
    try:
        return function_name()
    except ValueError:
        print_value_error_message()

def handle_value_error_in_loop(function_name):
    valid = False
    while not valid:
        valid = True if handle_value_error(function_name) else False

def value_error_handler_decorator(function_name):
    return lambda *args, **kwargs: handle_value_error_in_loop(function_name)



#handle value error

def handle_value_error_message():

    print(TerminalColors.RED + "Please enter a valid integer." + TerminalColors.RESET)


def value_error_handler_inner(function_name, *args, **kwargs):
    try:
        return function_name(*args, **kwargs)
    except ValueError:
        handle_value_error_message()


def value_error_handler(function_name):
   
    return lambda *args, **kwargs: value_error_handler_inner(function_name, *args, **kwargs)


def input_validation_decorator(function_name):
    def decorator_function(*args, **kwargs):
        while True:
            try: return function_name(*args, **kwargs)
            except ValueError: print(TerminalColors.RED + "Invalid limit. Please enter a number." + TerminalColors.RESET)
            except KeyboardInterrupt:
                print(TerminalColors.CYAN + "\n\nPlease Enter '>q' or '>Q' to exit the Program\n" + TerminalColors.RESET)
    return decorator_function
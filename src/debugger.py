#########################
# For console debugging #
#########################

from colorama import Style, Fore, Back, init

init()

def log_passing(msg):
    print(Back.GREEN + "✓ PASSING" + Back.RESET, msg)

def log_warning(msg):
    print(Back.YELLOW + "⚠ WARNING" + Back.RESET, msg)

def log_error(msg):
    print(Back.RED + "ⓧ ERROR" + Back.RESET, msg)
import colorama
RED = '\u001b[31m'
RESET = '\u001b[0m'


print(RED, "this will be in red")


def colour_print(text: str, effect: str ) -> None:
    """Print text usint he ansi sequences
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)

colorama.init()
colour_print("Hello, Red", RED)
colour_print("Hello, Red", RESET)
colorama.deinit()

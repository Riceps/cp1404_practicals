"""Client code to use the programming language class"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    """Utilise programming language class"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print the given programming languages with class str method
    print(ruby)
    print(python)
    print(visual_basic)

    # Create list containing programming languages
    programming_languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for i, language in enumerate(programming_languages):
        if language.is_dynamic():
            print(i, language.program_name)


main()

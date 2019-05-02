"""Programming language class"""


class ProgrammingLanguage:
    def __init__(self, program_name="", program_typing="", program_reflection=False, program_year=0):
        self.program_name = program_name
        self.program_typing = program_typing
        self.program_reflection = program_reflection
        self.program_year = program_year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.program_name, self.program_typing,
                                                                           self.program_reflection, self.program_year)

    def is_dynamic(self):
        if self.program_typing == "Dynamic":
            return True
        else:
            return False

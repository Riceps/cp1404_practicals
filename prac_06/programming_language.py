"""Programming language class"""


class ProgrammingLanguage:
    def __init__(self, program_name="", program_typing="", program_reflection=False, program_year=0):
        """Initialise programming language class"""
        self.program_name = program_name
        self.program_typing = program_typing
        self.program_reflection = program_reflection
        self.program_year = program_year

    def __str__(self):
        """Produce printable string"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.program_name, self.program_typing,
                                                                           self.program_reflection, self.program_year)

    def is_dynamic(self):
        """Check if programming language is dynamic"""
        return self.program_typing == "Dynamic"

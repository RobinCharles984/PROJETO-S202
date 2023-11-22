class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class PersonagemCLI(SimpleCLI):
    def __init__(self, personagem_model):
        super().__init__()
        self.personagem_model = personagem_model
        self.add_command("create", self.)
        self.add_command("read", self.)
        self.add_command("update", self.)
        self.add_command("delete", self.)
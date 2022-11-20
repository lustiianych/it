class Name:
    def __init__(self, name) -> None:
        if name not in ["Юрій", "Анонім"]:
            raise ValueError("Дозволені імена: Юрій, Анонім")
        self.name = name

a = Name("Юрєц")
from rich.prompt import Prompt


class Scanner:
    def __init__(self) -> None:
        pass

    @staticmethod
    def ask(String: str) -> str:
        return Prompt.ask(f"[underline]{String}[/]")

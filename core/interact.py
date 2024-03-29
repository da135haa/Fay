class Interact:

    def __init__(self, interleaver: str, interact_type: int, data: dict):
        self.interleaver = interleaver
        self.interact_type = interact_type
        self.data = data
    def __str__(self):
        return f"Interact(interleaver={self.interleaver}, interact_type={self.interact_type}, data={self.data})"

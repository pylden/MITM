from module.protocol.network.message import Message


class BreachGameFightEndMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4165
        self.budget = {"type": "int", "value": ""}

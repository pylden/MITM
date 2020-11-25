from module.protocol.network.message import Message


class BreachCharactersMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5583
        self.characters = {"type": "Vector.<Number>", "value": ""}

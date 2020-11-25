from module.protocol.network.message import Message


class BreachCharactersMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5583
        self.characters = {"type": "Vector.<Number>", "value": ""}

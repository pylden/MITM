from module.protocol.network.message import Message


class CharactersListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9869
        self.hasStartupActions = {"type": "Boolean", "value": ""}

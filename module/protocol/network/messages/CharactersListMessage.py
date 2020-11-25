from module.protocol.network.message import Message


class CharactersListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9869
        self.hasStartupActions = {"type": "Boolean", "value": ""}

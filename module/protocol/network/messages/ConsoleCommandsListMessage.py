from module.protocol.network.message import Message


class ConsoleCommandsListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1923
        self.aliases = {"type": "Vector.<String>", "value": ""}
        self.args = {"type": "Vector.<String>", "value": ""}
        self.descriptions = {"type": "Vector.<String>", "value": ""}

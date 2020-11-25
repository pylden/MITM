from module.protocol.network.message import Message


class GameFightOptionToggleMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5741
        self.option = {"type": "uint", "value": ""}

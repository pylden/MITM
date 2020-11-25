from module.protocol.network.message import Message


class ServerSelectionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1927
        self.serverId = {"type": "uint", "value": ""}

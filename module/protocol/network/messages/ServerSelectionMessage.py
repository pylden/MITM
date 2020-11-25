from module.protocol.network.message import Message


class ServerSelectionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1927
        self.serverId = {"type": "uint", "value": ""}

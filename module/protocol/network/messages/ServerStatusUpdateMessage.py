from module.protocol.network.message import Message


class ServerStatusUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3937
        self.server = {"type": "GameServerInformations", "value": ""}

from module.protocol.network.message import Message


class SelectedServerRefusedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6211
        self.serverId = {"type": "uint", "value": ""}
        self.error = {"type": "uint", "value": ""}
        self.serverStatus = {"type": "uint", "value": ""}

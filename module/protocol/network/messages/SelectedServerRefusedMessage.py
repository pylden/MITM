from module.protocol.network.message import Message


class SelectedServerRefusedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6211
        self.serverId = {"type": "uint", "value": ""}
        self.error = {"type": "uint", "value": ""}
        self.serverStatus = {"type": "uint", "value": ""}

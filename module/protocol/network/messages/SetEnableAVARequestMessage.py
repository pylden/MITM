from module.protocol.network.message import Message


class SetEnableAVARequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4687
        self.enable = {"type": "Boolean", "value": ""}

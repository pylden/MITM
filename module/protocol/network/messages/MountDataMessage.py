from module.protocol.network.message import Message


class MountDataMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8157
        self.mountData = {"type": "MountClientData", "value": ""}

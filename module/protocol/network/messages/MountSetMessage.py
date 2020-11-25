from module.protocol.network.message import Message


class MountSetMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8199
        self.mountData = {"type": "MountClientData", "value": ""}

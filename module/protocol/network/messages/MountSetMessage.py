from module.protocol.network.message import Message


class MountSetMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8199
        self.mountData = {"type": "MountClientData", "value": ""}

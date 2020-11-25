from module.protocol.network.message import Message


class MountReleasedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3002
        self.mountId = {"type": "int", "value": ""}

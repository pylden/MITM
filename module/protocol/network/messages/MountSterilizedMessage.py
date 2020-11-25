from module.protocol.network.message import Message


class MountSterilizedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4700
        self.mountId = {"type": "int", "value": ""}

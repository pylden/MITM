from module.protocol.network.message import Message


class MountRenamedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7458
        self.mountId = {"type": "int", "value": ""}
        self.name = {"type": "String", "value": ""}

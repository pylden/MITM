from module.protocol.network.message import Message


class HavenBagPermissionsUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1176
        self.permissions = {"type": "uint", "value": ""}

from module.protocol.network.message import Message


class MigratedServerListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5457
        self.migratedServerIds = {"type": "Vector.<uint>", "value": ""}

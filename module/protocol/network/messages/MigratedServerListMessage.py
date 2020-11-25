from module.protocol.network.message import Message


class MigratedServerListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5457
        self.migratedServerIds = {"type": "Vector.<uint>", "value": ""}

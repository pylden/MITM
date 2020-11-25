from module.protocol.network.message import Message


class ZaapDestinationsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7339
        self.spawnMapId = {"type": "Number", "value": ""}

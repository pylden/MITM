from module.protocol.network.message import Message


class ZaapDestinationsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7339
        self.spawnMapId = {"type": "Number", "value": ""}

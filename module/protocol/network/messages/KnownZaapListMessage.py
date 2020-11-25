from module.protocol.network.message import Message


class KnownZaapListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9552
        self.destinations = {"type": "Vector.<Number>", "value": ""}

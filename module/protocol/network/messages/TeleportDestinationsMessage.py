from module.protocol.network.message import Message


class TeleportDestinationsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1851
        self.type = {"type": "uint", "value": ""}
        self.destinations = {"type": "Vector.<TeleportDestination>", "value": ""}

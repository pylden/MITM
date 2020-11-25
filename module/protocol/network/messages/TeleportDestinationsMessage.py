from module.protocol.network.message import Message


class TeleportDestinationsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1851
        self.type = {"type": "uint", "value": ""}
        self.destinations = {"type": "Vector.<TeleportDestination>", "value": ""}

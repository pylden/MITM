from module.protocol.network.message import Message


class OnConnectionEventMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2093
        self.eventType = {"type": "uint", "value": ""}

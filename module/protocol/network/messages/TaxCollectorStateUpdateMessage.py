from module.protocol.network.message import Message


class TaxCollectorStateUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5755
        self.uniqueId = {"type": "Number", "value": ""}
        self.state = {"type": "int", "value": ""}

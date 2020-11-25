from module.protocol.network.message import Message


class TaxCollectorMovementRemoveMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6992
        self.collectorId = {"type": "Number", "value": ""}

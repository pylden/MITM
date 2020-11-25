from module.protocol.network.message import Message


class TaxCollectorMovementAddMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9684
        self.informations = {"type": "TaxCollectorInformations", "value": ""}

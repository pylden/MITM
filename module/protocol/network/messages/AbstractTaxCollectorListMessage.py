from module.protocol.network.message import Message


class AbstractTaxCollectorListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4914
        self.informations = {"type": "Vector.<TaxCollectorInformations>", "value": ""}

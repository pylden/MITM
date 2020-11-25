from module.protocol.network.message import Message


class ExchangeMultiCraftSetCrafterCanUseHisRessourcesMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2395
        self.allow = {"type": "Boolean", "value": ""}

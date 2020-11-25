from module.protocol.network.message import Message


class ExchangeSetCraftRecipeMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 49
        self.objectGID = {"type": "uint", "value": ""}

from module.protocol.network.message import Message


class ExchangeSetCraftRecipeMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 49
        self.objectGID = {"type": "uint", "value": ""}

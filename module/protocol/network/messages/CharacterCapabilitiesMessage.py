from module.protocol.network.message import Message


class CharacterCapabilitiesMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4411
        self.guildEmblemSymbolCategories = {"type": "uint", "value": ""}

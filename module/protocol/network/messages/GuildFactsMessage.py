from module.protocol.network.message import Message


class GuildFactsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6652
        self.infos = {"type": "GuildFactSheetInformations", "value": ""}
        self.creationDate = {"type": "uint", "value": ""}
        self.nbTaxCollectors = {"type": "uint", "value": ""}
        self.members = {"type": "Vector.<CharacterMinimalGuildPublicInformations>", "value": ""}

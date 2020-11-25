from module.protocol.network.message import Message


class GuildFactsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6652
        self.infos = {"type": "GuildFactSheetInformations", "value": ""}
        self.creationDate = {"type": "uint", "value": ""}
        self.nbTaxCollectors = {"type": "uint", "value": ""}
        self.members = {"type": "Vector.<CharacterMinimalGuildPublicInformations>", "value": ""}

from module.protocol.network.message import Message


class GuildHousesInformationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 872
        self.housesInformations = {"type": "Vector.<HouseInformationsForGuild>", "value": ""}

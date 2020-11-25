from module.protocol.network.message import Message


class AllianceInsiderInfoMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4742
        self.allianceInfos = {"type": "AllianceFactSheetInformations", "value": ""}
        self.guilds = {"type": "Vector.<GuildInsiderFactSheetInformations>", "value": ""}
        self.prisms = {"type": "Vector.<PrismSubareaEmptyInfo>", "value": ""}

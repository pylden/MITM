from module.protocol.network.message import Message


class AllianceListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5246
        self.alliances = {"type": "Vector.<AllianceFactSheetInformations>", "value": ""}

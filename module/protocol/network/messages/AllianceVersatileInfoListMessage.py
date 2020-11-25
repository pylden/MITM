from module.protocol.network.message import Message


class AllianceVersatileInfoListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2433
        self.alliances = {"type": "Vector.<AllianceVersatileInformations>", "value": ""}

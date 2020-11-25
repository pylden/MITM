from module.protocol.network.message import Message


class SlaveSwitchContextMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9736
        self.masterId = {"type": "Number", "value": ""}
        self.slaveId = {"type": "Number", "value": ""}
        self.slaveSpells = {"type": "Vector.<SpellItem>", "value": ""}
        self.slaveStats = {"type": "CharacterCharacteristicsInformations", "value": ""}
        self.shortcuts = {"type": "Vector.<Shortcut>", "value": ""}

from module.protocol.network.message import Message


class SlaveSwitchContextMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9736
        self.masterId = {"type": "Number", "value": ""}
        self.slaveId = {"type": "Number", "value": ""}
        self.slaveSpells = {"type": "Vector.<SpellItem>", "value": ""}
        self.slaveStats = {"type": "CharacterCharacteristicsInformations", "value": ""}
        self.shortcuts = {"type": "Vector.<Shortcut>", "value": ""}

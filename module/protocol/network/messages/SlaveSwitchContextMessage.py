from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SlaveSwitchContextMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9736
        self.masterId = {"type": "Number", "value": ""}
        self.slaveId = {"type": "Number", "value": ""}
        self.slaveSpells = {"type": "Vector.<SpellItem>", "value": ""}
        self.slaveStats = {"type": "CharacterCharacteristicsInformations", "value": ""}
        self.shortcuts = {"type": "Vector.<Shortcut>", "value": ""}

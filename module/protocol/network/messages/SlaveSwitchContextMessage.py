from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SlaveSwitchContextMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9736
        self.vars.append({"name": "masterId", "type": "Number", "value": ""})
        self.vars.append({"name": "slaveId", "type": "Number", "value": ""})
        self.vars.append({"name": "slaveSpells", "type": "Vector.<SpellItem>", "value": ""})
        self.vars.append({"name": "slaveStats", "type": "CharacterCharacteristicsInformations", "value": ""})
        self.vars.append({"name": "shortcuts", "type": "Vector.<Shortcut>", "value": ""})

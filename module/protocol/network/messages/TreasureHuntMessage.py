from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4631
        self.vars.append({"name": "questType", "type": "uint", "value": ""})
        self.vars.append({"name": "startMapId", "type": "Number", "value": ""})
        self.vars.append({"name": "knownStepsList", "type": "Vector.<TreasureHuntStep>", "value": ""})
        self.vars.append({"name": "totalStepCount", "type": "uint", "value": ""})
        self.vars.append({"name": "checkPointCurrent", "type": "uint", "value": ""})
        self.vars.append({"name": "checkPointTotal", "type": "uint", "value": ""})
        self.vars.append({"name": "availableRetryCount", "type": "int", "value": ""})
        self.vars.append({"name": "flags", "type": "Vector.<TreasureHuntFlag>", "value": ""})

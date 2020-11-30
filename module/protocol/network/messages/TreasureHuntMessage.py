from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4631
        self.questType = {"type": "uint", "value": ""}
        self.startMapId = {"type": "Number", "value": ""}
        self.knownStepsList = {"type": "Vector.<TreasureHuntStep>", "value": ""}
        self.totalStepCount = {"type": "uint", "value": ""}
        self.checkPointCurrent = {"type": "uint", "value": ""}
        self.checkPointTotal = {"type": "uint", "value": ""}
        self.availableRetryCount = {"type": "int", "value": ""}
        self.flags = {"type": "Vector.<TreasureHuntFlag>", "value": ""}

from module.protocol.network.messages.NetworkMessage import NetworkMessage


class UpdateMountCharacteristicsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9975
        self.vars.append({"name": "rideId", "type": "int", "value": ""})
        self.vars.append({"name": "boostToUpdateList", "type": "Vector.<UpdateMountCharacteristic>", "value": ""})

from module.protocol.network.messages.NetworkMessage import NetworkMessage


class UpdateMountCharacteristicsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9975
        self.rideId = {"type": "int", "value": ""}
        self.boostToUpdateList = {"type": "Vector.<UpdateMountCharacteristic>", "value": ""}

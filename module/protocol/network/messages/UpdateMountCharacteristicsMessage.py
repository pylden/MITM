from module.protocol.network.message import Message


class UpdateMountCharacteristicsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9975
        self.rideId = {"type": "int", "value": ""}
        self.boostToUpdateList = {"type": "Vector.<UpdateMountCharacteristic>", "value": ""}

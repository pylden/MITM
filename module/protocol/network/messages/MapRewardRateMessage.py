from module.protocol.network.message import Message


class MapRewardRateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9715
        self.mapRate = {"type": "int", "value": ""}
        self.subAreaRate = {"type": "int", "value": ""}
        self.totalRate = {"type": "int", "value": ""}

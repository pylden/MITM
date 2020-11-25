from module.protocol.network.message import Message


class MapRewardRateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9715
        self.mapRate = {"type": "int", "value": ""}
        self.subAreaRate = {"type": "int", "value": ""}
        self.totalRate = {"type": "int", "value": ""}

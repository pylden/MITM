from module.protocol.network.message import Message


class MapObstacleUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5663
        self.obstacles = {"type": "Vector.<MapObstacle>", "value": ""}

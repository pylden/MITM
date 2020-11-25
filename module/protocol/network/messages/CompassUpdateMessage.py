from module.protocol.network.message import Message


class CompassUpdateMessage(Message):
    def __init__(self):
        self.id = 3439

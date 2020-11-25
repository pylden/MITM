from module.protocol.network.message import Message


class CompassUpdatePvpSeekMessage(Message):
    def __init__(self):
        self.id = 6287
        self.memberName = {"type": "String", "value": ""}

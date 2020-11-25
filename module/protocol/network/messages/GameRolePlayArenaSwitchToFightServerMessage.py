from module.protocol.network.message import Message


class GameRolePlayArenaSwitchToFightServerMessage(Message):
    def __init__(self):
        self.id = 9880
        self.address = {"type": "String", "value": ""}

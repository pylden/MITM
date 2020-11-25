from module.protocol.network.message import Message


class GameActionFightDeathMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4815
        self.targetId = {"type": "Number", "value": ""}

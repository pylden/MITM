from module.protocol.network.message import Message


class GameContextMoveElementMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8769
        self.movement = {"type": "EntityMovementInformations", "value": ""}

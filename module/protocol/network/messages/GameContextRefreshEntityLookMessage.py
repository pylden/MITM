from module.protocol.network.message import Message


class GameContextRefreshEntityLookMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5695
        self.id = {"type": "Number", "value": ""}
        self.look = {"type": "EntityLook", "value": ""}

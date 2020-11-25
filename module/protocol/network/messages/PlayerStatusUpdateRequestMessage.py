from module.protocol.network.message import Message


class PlayerStatusUpdateRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6455
        self.status = {"type": "PlayerStatus", "value": ""}

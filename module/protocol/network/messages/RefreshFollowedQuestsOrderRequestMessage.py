from module.protocol.network.message import Message


class RefreshFollowedQuestsOrderRequestMessage(Message):
    def __init__(self):
        self.id = 8535

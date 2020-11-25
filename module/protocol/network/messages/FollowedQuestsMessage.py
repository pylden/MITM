from module.protocol.network.message import Message


class FollowedQuestsMessage(Message):
    def __init__(self):
        self.id = 9768

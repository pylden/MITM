from module.protocol.network.message import Message


class InteractiveElementUpdatedMessage(Message):
    def __init__(self):
        self.id = 2801

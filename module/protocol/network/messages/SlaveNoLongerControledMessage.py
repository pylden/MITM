from module.protocol.network.message import Message


class SlaveNoLongerControledMessage(Message):
    def __init__(self):
        self.id = 8594

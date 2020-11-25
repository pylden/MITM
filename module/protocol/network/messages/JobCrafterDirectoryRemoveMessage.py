from module.protocol.network.message import Message


class JobCrafterDirectoryRemoveMessage(Message):
    def __init__(self):
        self.id = 2166

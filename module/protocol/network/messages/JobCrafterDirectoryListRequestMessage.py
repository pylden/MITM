from module.protocol.network.message import Message


class JobCrafterDirectoryListRequestMessage(Message):
    def __init__(self):
        self.id = 2533
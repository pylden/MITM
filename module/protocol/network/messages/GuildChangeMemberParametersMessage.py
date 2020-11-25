from module.protocol.network.message import Message


class GuildChangeMemberParametersMessage(Message):
    def __init__(self):
        self.id = 2513

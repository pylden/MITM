from module.protocol.network.message import Message


class GameRolePlayFightRequestCanceledMessage(Message):
    def __init__(self):
        self.id = 7446

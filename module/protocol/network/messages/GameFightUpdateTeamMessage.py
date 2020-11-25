from module.protocol.network.message import Message


class GameFightUpdateTeamMessage(Message):
    def __init__(self):
        self.id = 8783

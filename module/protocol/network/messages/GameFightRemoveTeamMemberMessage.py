from module.protocol.network.message import Message


class GameFightRemoveTeamMemberMessage(Message):
    def __init__(self):
        self.id = 6353

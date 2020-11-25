from module.protocol.network.message import Message


class AchievementFinishedInformationMessage(Message):
    def __init__(self):
        self.id = 7636
        self.name = {"type": "String", "value": ""}

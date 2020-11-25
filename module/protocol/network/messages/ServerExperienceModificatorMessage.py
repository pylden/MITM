from module.protocol.network.message import Message


class ServerExperienceModificatorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4756
        self.experiencePercent = {"type": "uint", "value": ""}

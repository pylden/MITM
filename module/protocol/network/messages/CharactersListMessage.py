from module.protocol.network.messages.BasicCharactersListMessage import BasicCharactersListMessage


class CharactersListMessage(BasicCharactersListMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        BasicCharactersListMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9869
        self.hasStartupActions = {"type": "Boolean", "value": ""}

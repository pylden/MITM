from module.protocol.network.messages.IdentificationSuccessMessage import IdentificationSuccessMessage


class IdentificationSuccessWithLoginTokenMessage(IdentificationSuccessMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        IdentificationSuccessMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5260
        self.loginToken = {"type": "String", "value": ""}

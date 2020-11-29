from module.protocol.network.messages.MailStatusMessage import MailStatusMessage


class NewMailMessage(MailStatusMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        MailStatusMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7617
        self.vars.append({"name": "sendersAccountId", "type": "Vector.<uint>", "value": ""})

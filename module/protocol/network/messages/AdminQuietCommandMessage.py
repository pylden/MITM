from module.protocol.network.messages.AdminCommandMessage import AdminCommandMessage


class AdminQuietCommandMessage(AdminCommandMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AdminCommandMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1379

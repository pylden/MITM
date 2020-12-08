from module.protocol.processor.protocol_processor import ProtocolProcessor
from module.protocol.network.message_factory import MessageFactory
from module.bot.bot import Bot


class D2Protocol(ProtocolProcessor):
    def __init__(self, client):
        ProtocolProcessor.__init__(self, client)
        self.bot = Bot(client)

    def get_messages(self, buffer, from_client=False):
        messages = list()
        while len(buffer) and (message := MessageFactory.message(buffer, from_client=from_client)):
            messages.append(message)
            buffer = buffer[message.get_message_size():]
        return messages, buffer

    def from_client(self, data):
        messages, self._client_buffer = self.get_messages(self._client_buffer + data, from_client=True)
        bot_data = self.bot.read_messages(messages)
        print("From client : %s" % data.hex())
        if bot_data:
            print("From server after : %s" % bot_data.hex())
        return bot_data

    def from_server(self, data):
        messages, self._server_buffer = self.get_messages(self._server_buffer + data)
        bot_data = self.bot.read_messages(messages)
        print("From server : %s" % data.hex())
        if bot_data:
            print("From server after : %s" % bot_data.hex())
        return bot_data

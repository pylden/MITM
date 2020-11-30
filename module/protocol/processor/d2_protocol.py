from module.protocol.processor.protocol_processor import ProtocolProcessor
from module.protocol.network.message_factory import MessageFactory


class D2Protocol(ProtocolProcessor):
    def __init__(self, client):
        ProtocolProcessor.__init__(self, client)

    def get_messages(self, buffer, from_client=False):
        messages = list()
        while len(buffer) and (message := MessageFactory.message(buffer, from_client=from_client)):
            messages.append(message)
            buffer = buffer[message.get_message_size():]
        return messages, buffer

    def from_client(self, data):
        messages, self._client_buffer = self.get_messages(self._client_buffer + data, from_client=True)
        if len(messages):
            for message in messages:
                print(message)

    def from_server(self, data):
        messages, self._server_buffer = self.get_messages(self._server_buffer + data)
        if len(messages):
            for message in messages:
                print(message)

    def send_server(self, message):
        self._client.write(message)


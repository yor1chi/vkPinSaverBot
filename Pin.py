import json
from Connection import Connection
from vk_api.utils import get_random_id


class Pin:
    con = Connection()
    longpoll = con.createSession()[0]
    vk = con.createSession()[1]

    def isPin(self, message):
        if message.action is not None:
            if message.action['type'] == 'chat_pin_message':
                return True
        else:
            return False

    def printPinList(self, event):
        with open('pin_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        if len(data) != 0:
            name, text, attach = [], [], []
            for i in data.keys():
                name.append(data[i][0]['Name'])
                text.append(data[i][0]['Text'])
                attach.append(data[i][0]['Attachments'])
            printData = self.formatOutput(name, text, attach)
        else:
            printData = 'Список закрепов пуст'

        json_query = json.dumps({
            'peer_id': event.message.peer_id,
            'conversation_message_ids': [event.message.conversation_message_id],
            'is_reply': True
        })

        self.vk.messages.send(
            key=(self.con.getKey()),
            server=(self.con.getServer()),
            ts=(self.con.getTs()),
            random_id=get_random_id(),
            forward=[json_query],
            message=printData,
            chat_id=event.chat_id)

    def savePinList(self, event):
        if self.isPin(event.message):
            messageId = event.message.action['conversation_message_id']
            with open('messages_data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)

            with open('pin_data.json', 'r', encoding='utf-8') as f:
                pinData = json.load(f)
            pinData[len(pinData)] = data[str(messageId)]

            with open('pin_data.json', 'w', encoding='utf-8') as f:
                json.dump(pinData, f, ensure_ascii=False)

    def formatOutput(self, name, text, attach):
        printData = ''


        for i in range(len(name)):
            if text[i] == '':
                if attach[i] == 'Empty':
                    printData = printData + f'{i + 1}: {name[i]}' + '\n'
                else:
                    printData = printData + f'{i + 1}: {name[i]}, {attach[i]}' + '\n'
            if attach[i] == 'Empty' and text[i] != '':
                printData = printData + f'{i + 1}: {name[i]}, {text[i]}' + '\n'
            elif text[i] != '' and attach[i] != 'Empty':
                printData = printData + f'{i + 1}: {name[i]}, {text[i]}, {attach[i]}' + '\n'
        if "'" in printData:
            printData = printData.replace("'", '')
        return printData

    def clearPinList(self, event):
        if self.isAdmin(event):
            pinData = {}

            with open('pin_data.json', 'w', encoding='utf-8') as f:
                json.dump(pinData, f, ensure_ascii=False)

            json_query = json.dumps({
                'peer_id': event.message.peer_id,
                'conversation_message_ids': [event.message.conversation_message_id],
                'is_reply': True
            })

            self.vk.messages.send(
                key=(self.con.getKey()),
                server=(self.con.getServer()),
                ts=(self.con.getTs()),
                random_id=get_random_id(),
                forward=[json_query],
                message='Закреп очищен',
                chat_id=event.chat_id)
        else:
            json_query = json.dumps({
                'peer_id': event.message.peer_id,
                'conversation_message_ids': [event.message.conversation_message_id],
                'is_reply': True
            })
            self.vk.messages.send(
                key=(self.con.getKey()),
                server=(self.con.getServer()),
                ts=(self.con.getTs()),
                random_id=get_random_id(),
                forward=[json_query],
                message='Пошел нахуй',
                chat_id=event.chat_id)

    def isAdmin(self, event):
        user_get = self.vk.users.get(user_ids=event.message.from_id, fields='screen_name')
        name = user_get[0]['first_name'] + ' ' + user_get[0]['last_name']
        if name == 'Семен Майоров':
            return True
        else:
            return False

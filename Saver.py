import json
from Connection import Connection


class Saver:
    con = Connection()
    longpoll = con.createSession()[0]
    vk = con.createSession()[1]

    def dataSave(self, event):
        user_get = self.vk.users.get(user_ids=event.message.from_id, fields='screen_name')
        name = user_get[0]['first_name'] + ' ' + user_get[0]['last_name']
        message_text = event.message.text
        message_id = event.message.conversation_message_id
        print(name, message_text, message_id)
        attachmentData = self.checkAttachmentType(event.message.attachments)

        with open('messages_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        data[message_id] = [{'Name': name, 'Text': message_text, 'Attachments': attachmentData}]
        with open('messages_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

    def checkAttachmentType(self, attachments):
        if len(attachments) == 0:
            return 'Empty'
        else:
            dataToSave = []
            for i in attachments:
                if i['type'] == 'doc':
                    dataToSave.append(('Гифка ' + i['doc']['title'], i['doc']['url']))
                elif i['type'] == 'audio':
                    dataToSave.append(('Песня ' + i['audio']['title'], i['audio']['url']))
                elif i['type'] == 'photo':
                    dataToSave.append(('Фот', i['photo']['sizes'][-1]['url']))
                elif i['type'] == 'video':
                    dataToSave.append(('Видео ' + i['video']['title'], 'vk.com/video' + str(
                        i['video']['owner_id']) + '_' + str(i['video']['id'])))
                elif i['type'] == 'poll':
                    dataToSave.append(('Опрос', i['poll']['question']))
                elif i['type'] == 'wall':
                    dataToSave.append(('Запись со стены', 'vk.com/wall' + str(i['wall']['from_id']) + '_' + str(
                        i['wall']['id'])))
            return dataToSave






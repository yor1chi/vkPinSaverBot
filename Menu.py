from Connection import Connection
from Pin import Pin
from Saver import Saver


class Menu:
    __trigger_words = ['!закреп', '!звкреп', '!pfrhtg', '!закреа']
    __trigger_words2 = ['!очистить', '!jxbcnbnm']
    con = Connection()
    pin = Pin()
    saver = Saver()
    longpoll = con.createSession()[0]
    vk = con.createSession()[1]

    def Menu(self):
        for event in self.longpoll.listen():
            self.saver.dataSave(event)
            self.pin.savePinList(event)
            if event.message.text.lower() in self.__trigger_words:
                self.pin.printPinList(event)
            elif event.message.text.lower() in self.__trigger_words2:
                self.pin.clearPinList(event)



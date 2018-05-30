#log - environmental variable for remebering login and password
from os import environ

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.core.text import LabelBase
from kivy.core.text.markup import MarkupLabel
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from filewrite import writing
from fileread import reading

KIVY_FONTS = [
    {
        "name":"fontt",
        "fn_regular": "coolfont.ttf"
    }
]
for font in KIVY_FONTS:
    LabelBase.register(**font)

    
class Logging_page(Screen):
    remember = ObjectProperty()
    mainlabeltext = StringProperty("Welcome, please Enter your login and password")
    def idcheck(self, log, pas):
        return sum([ord(i) for i in log + pas  if i !=" " and i!="\n"])
    def checklogpas(self):
        database = reading()
        log = self.ids.mail.text
        pas = self.ids.parole.text
        try:
            if database[str(self.idcheck(log,pas))] == (pas,log) \
               and log !="" and pas != "":
                self.rememberloginandpass()                    
                app = App.get_running_app()
                app.root.current = "sub"
        except KeyError:
            self.createanerrrorwidget()
    def createanerrrorwidget(self):
        self.ids.labe.text = "Wrong login or password"
    def rememberloginandpass(self):
        pass     
                  

        

class Submitting_page(Screen):
    def locationsend(self):
        raise NotImplementedError
    def constlocation(self):
        raise NotImplementedError

class SenderEmail(Screen):
    def getmail(self):
        sendermail = self.ids.sendermail.text
        with open ("data.txt","a",encoding = "utf-8") as file:
            file.write(" "+sendermail+"\n")
        app = App.get_running_app()
        app.root.current = "sub"
        

class Registration_page(Screen):
    def returnmail(self):
        self.mail = self.ids.mail.text
    def returnpassword(self):
        self.parole = self.ids.parole.text
    def idcreation(self):
        self.idd = sum([ord(i) for i in self.parole + self.mail if i !=" " and i!="\n"])
    def writetofile(self):
        writing((self.mail,self.parole,self.idd))
    def goforward(self):
        app = App.get_running_app()
        app.root.current = "sendi"
        
class ScreenM(ScreenManager):
    def __init__(self):
        super().__init__()
        self.add_widget(Logging_page(name = "log"))    
        self.add_widget(Submitting_page(name ="sub"))
        self.add_widget(SenderEmail(name="sendi"))
        self.add_widget(Registration_page(name="reg"))



class Logging(App):
    def build(self):
        return ScreenM()

if __name__ == "__main__":
    Logging().run()

import glob
import json
import pathlib
import random
from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

from hoverable import HoverBehavior

Builder.load_file('design.kv')


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, uname, pword):
        with open('user.json') as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = 'login_success_screen'
        else:
            self.ids.invalid_login.text = "Invalid username or password!"


class SignUpScreen(Screen):
    def add_user(self, username, password):
        with open('user.json') as file:
            user = json.load(file)
        user[username] = {'username': username, 'password': password,
                          "date": datetime.now().strftime('%Y-%m-%d %H-%M-%S')}

        with open("user.json", 'w') as file:
            json.dump(user, file)
        self.manager.current = "sign_up_success_screen"


class SignUpSuccessScreen(Screen):
    def login_page(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'


class LoginSuccessScreen(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob('quotes/*txt')
        available_feelings = [pathlib.Path(filename).stem for filename in available_feelings]

        if feel in available_feelings:
            with open(f'quotes/{feel}.txt', encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another keyword"


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()

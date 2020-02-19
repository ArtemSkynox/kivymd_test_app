from kivy import Config
from kivy.lang import Builder
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.texture import Texture
from kivy.uix.behaviors import ButtonBehavior
from PIL import Image, ImageDraw, ImageFilter
import kivy.properties as props
from kivy.clock import Clock
from kivy.animation import Animation

Config.set("graphics", "width", "480")
Config.set("graphics", "height", "820")

from kivymd.app import MDApp


class Content(BoxLayout):
    pass

class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)
        
MainApp().run()
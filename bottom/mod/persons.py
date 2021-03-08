from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, TwoLineAvatarIconListItem, ImageLeftWidget


class MyItem(TwoLineAvatarIconListItem):
    def __init__(self, i, *args, **kwargs):
        js = JsonStore('names.json')
        super(MyItem, self).__init__(*args)
        state = js.get(i)['state']
        self.text = js.get(i)['name']
        self.secondary_text = js.get(i)['state']
        self._no_ripple_effect = True
        self.image = ImageLeftWidget(source=f"images/{state}.jpg")
        self.add_widget(self.image)

class Persons(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Persons, self).__init__(orientation="horizontal")
        scrollview = ScrollView()
        list = MDList()
        for i in range(3):
            list.add_widget(MyItem(str(i)))
        scrollview.add_widget(list)
        self.add_widget(scrollview)

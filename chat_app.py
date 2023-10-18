# tried to use chat gpt to take chatclient.py and chatserver.py into 1 file, this doesn't work but maybe is useful.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from threading import Thread
import socket

class ChatApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.label = Label(size_hint_y=None, height=44, markup=True)
        self.text_input = TextInput(hint_text="Type your message")
        send_button = Button(text="Send")
        send_button.bind(on_press=self.send_message)

        chat_scroll = ScrollView(size_hint=(1, 0.8))
        chat_scroll.add_widget(self.label)

        layout.add_widget(chat_scroll)
        layout.add_widget(self.text_input)
        layout.add_widget(send_button)

        # Socket setup
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("127.0.0.1", 5002))
        
        Thread(target=self.receive_message, daemon=True).start()

        return layout

    def send_message(self, instance):
        message = self.text_input.text
        self.sock.send(message.encode())
        self.text_input.text = ""

    def receive_message(self):
        while True:
            message = self.sock.recv(1024).decode()
            self.label.text += '\n' + message

if __name__ == "__main__":
    ChatApp().run()

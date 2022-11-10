from guizero import App, Box, TextBox, Text, PushButton

def change_message():
    message.value = "You pressed the button!"

app = App(title="Hello world")

message = Text(app, text="Welcome to the Hello world app!")

message2 = Text(app, text="Enter your name")
name = TextBox(app)

button = PushButton(app, text="Press me", command=change_message)

app.display()
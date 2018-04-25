from flask import *
from gmail import GMail, Message
app = Flask(__name__)



@app.route('/')

def index():
    gmail = GMail(username="duchoapc99techkids@gmail.com",
                  password="duchoa119")

    msg = Message("send mail", to="duchoapc99@gmail.com", text="Test")
    gmail.send(msg)

    return "Sent"
if __name__ == '__main__':
  app.run(debug=True)

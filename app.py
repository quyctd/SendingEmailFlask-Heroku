from flask import *
from gmail import GMail, Message
app = Flask(__name__)



@app.route('/')

def index():
    gmail = GMail("duchoapc99techkids@gmail.com",
                  "duchoa119")

    msg = Message("send mail", to="quy.dc98@gmail.com", text="Test")
    gmail.send(msg)

    return "Sent"
if __name__ == '__main__':
  app.run(debug=True)

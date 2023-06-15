from flask import Flask, render_template
import insta

app = Flask(__name__)

@app.route('/')
def home():
    insta.bot.infinity_polling()
    return "Hello, World!"

if __name__ == '__main__':
    app.run()

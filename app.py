from flask import Flask

app = Flask (__name__)
@app.rout("/")
def index ():
  return "Olá, <b>tudo bem</b>?"

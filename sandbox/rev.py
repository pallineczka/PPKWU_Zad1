from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/<text>')
def rev(text):
  #returns the rev text
  return 'rev text: %s' % revText(text)

def revText(text):
  s1 = ''.join(reversed(text))
  return s1

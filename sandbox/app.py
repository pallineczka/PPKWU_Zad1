from flask import Flask
import re
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/text/<text>')
def rev(text):
  #returns the rev text
  duza = 0
  mala = 0
  cyfra = 0
  specjalny = 0
  for x in text:
    if x.isupper():
      duza += 1
    if x.islower():
      mala += 1
    if x.isdigit():
      cyfra += 1
    if not re.match("^[a-zA-Z0-9_]*$", x):
      specjalny += 1
  return 'duza: %d mala: %d cyfra: %d znak specjalny: %d \n rev text: %s' %(duza, mala, cyfra, specjalny, revText(text))

def revText(text):
  s1 = ''.join(reversed(text))
  return s1
import requests as rq
from flask import Flask, jsonify, request


# route 1 -- ping
def call_ping_route():
  r = rq.get('http://localhost:5000/ping') # make the request
  return r

# route 2 -- random word
def call_random_word_route():
  r = rq.get('http://localhost:5000/word') # make the request
  return r

# route 3 -- string count
def call_string_count():
  r = rq.post('http://localhost:5000/string-count', json = 'some') # make the request
  return r

route_callers = [
  call_ping_route,
  call_random_word_route,
  call_string_count
  ]

for call_route in route_callers:
  r = call_route()
  r.status_code # first, check r for errors

  data = r.json()
  print(data, f' --- STATUS CODE {r.status_code}') # print the response
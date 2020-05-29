import stomp
import time

class MyListener(object):
    def on_error(self, headers, message):
        print('received an error %s' % message)
    def on_message(self, headers, message):
        print('received a message %s' % headers)
conn = stomp.Connection10([('192.168.60.15',8089)])
conn.set_listener('logicServerQueue', MyListener())

conn.connect(wait=True)

conn.send(body='{ "uuid": "27abbe9d-d913-4fc7-9e55-1c40c29d43e3", "width": 1920, "height": 1200, "quality": 0.8 }', destination='/app/setSize')

conn.subscribe(destination='/app/setSize')

while True:
    try:
        time.sleep(1)
    except:
        break

conn.disconnect()

time.sleep(2)
conn.disconnect()

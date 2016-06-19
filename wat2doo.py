from mymeetup import  get_data
from flask import Flask, render_template, request, g
import json
import datetime

application = Flask(__name__)

@application.route('/')
def hello_world():
  return 'Hello from Flask!'

application.config.from_object(__name__)
application.debug = True

@application.route("/mymeetup")
def viewevents():
    data=get_data()
    total_events= data['meta']['count']
    last_upd_ts= data['meta']['updated']
    upd_ts=datetime.datetime.fromtimestamp(last_upd_ts/1000)
    m_events=data['results']
    my_events=[]
    for event in m_events:
        event['time']=datetime.datetime.fromtimestamp(event['time']/1000.0)
        my_events.append(event)

    return render_template('event_template.html', total_events=total_events, last_upd_ts=upd_ts,my_events=my_events)


if __name__ == "__main__":
    application.run(host='0.0.0.0')

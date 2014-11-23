from flask.ext.script import Server, Shell, Manager, prompt_bool
from app import app_
from app.foundation import db
from app.models import Friend
import json

app_.debug = False

manager = Manager(app_)
manager.add_command("runserver", Server('0.0.0.0',port=8001, threaded=True))

@manager.option(dest='raw_data_path', default=None)
def createall(raw_data_path = None):
    "Creates database tables"
    db.create_all()

    if raw_data_path:
        with open(raw_data_path) as f:
            for line in f:
                info = json.loads(line.strip())
                for k, v in info['attr'].items():
                    info[k] = v
                info['correction'] = ','.join(map(str, info['correction']))
                info.pop('weapon')
                info.pop('attr')
                friend = Friend(**info)
                db.session.add(friend)
                print info

    db.session.commit()

@manager.command                                                   
def dropall():
    "Drops all database tables"
    if prompt_bool("Are you sure ? You will lose all your data !"):
        db.drop_all()

if __name__ == "__main__":
    manager.run()


import pprint

import org.wayround.softengine.rtenv
import org.wayround.softengine.modules

db = org.wayround.softengine.rtenv.DB(
    'sqlite:////home/agu/tmp/mydb.sqlite',
    echo=True
    )


rtenv = org.wayround.softengine.rtenv.RuntimeEnvironment(
    db
    )

org.wayround.softengine.modules.Nodes(rtenv)

rtenv.init()

rtenv.db.create_all()

pprint.pprint(rtenv.modules)

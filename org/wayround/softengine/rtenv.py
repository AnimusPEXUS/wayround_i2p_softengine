
import inspect

import sqlalchemy.ext
import sqlalchemy.ext.declarative
import sqlalchemy.orm

class ModulesMissing(Exception): pass
class DBSessionAbsent(Exception): pass

class DB:

    def __init__(self, config, echo=False):

        self.db_base = sqlalchemy.ext.declarative.declarative_base()

        self.db_engine = (
                sqlalchemy.create_engine(
                config,
                echo=echo
                )
            )

        self.db_base.metadata.bind = self.db_engine

        self._sess = sqlalchemy.orm.Session(bind=self.db_engine)

        return

    def __del__(self):
        self.stop()

    def stop(self):

        if self._sess:
            self._sess.commit()
            self._sess.close()
            self._sess = None

        return

    def create_all(self, *args, **kwargs):
        return self.db_base.metadata.create_all(*args, **kwargs)

    @property
    def sess(self):
        if not self._sess:
            raise DBSessionAbsent("No DB Session")

        return self._sess

class RuntimeEnvironment:

    def __init__(self, db):

        if not isinstance(db, DB):
            raise TypeError("`db' must be of DB class type")

        self.db = db
        self.modules = {}
        self.models = {}
        self.module_requirements = {}
        self.templates = {}
        self.renderers = {}


    def init(self):

        self.check_modules()

    def check_modules(self):

        for i in self.modules.keys():

            if not isinstance(self.modules[i], ModulePrototype):
                raise TypeError(
                    "`{}' is not ModulePrototype's subclass".format(
                        self.modules[i]
                        )
                    )

        loaded_modules = self.modules.keys()
        missing_modules = []

        for i in self.module_requirements.keys():

            for j in self.module_requirements[i]:

                if not j in loaded_modules:
                    missing_modules.append(j)

        missing_modules = list(set(missing_modules))

        missing_modules.sort()

        if len(missing_modules) != 0:
            missing_modules_text = ''

            for i in missing_modules:
                missing_modules_text += '    {}\n'.format(i)

            raise ModulesMissing(
                "Some modules required:\n{}".format(missing_modules_text)
                )

        return


    def init_modules(self):

        for i in self.modules.keys():

            self.modules[i].init(self)


    def send_event(self, from_name, to_name, event, data):

        if not from_name.isidentifer():
            raise ValueError("Wrong from_name")

        if not to_name.isidentifer():
            raise ValueError("Wrong to_name")

        if not event.isidentifer():
            raise ValueError("Wrong event")

        for i in self.modules.keys():

            self.modules[i].event(from_name, event, data)


class ModulePrototype:
    pass

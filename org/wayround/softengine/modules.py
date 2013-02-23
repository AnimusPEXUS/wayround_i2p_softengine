
import sqlalchemy

import org.wayround.softengine.rtenv

_required_modules = [
    'org.wayround.softengine.modules.node',
    'org.wayround.softengine.modules.node_access',
    'org.wayround.softengine.modules.user',
    'org.wayround.softengine.modules.group',
    'org.wayround.softengine.modules.group_membership'
    ]

class Nodes(org.wayround.softengine.rtenv.ModulePrototype):

    def __init__(self, rtenv):

        self.module_name = 'org.wayround.softengine.modules.node'

        self.rtenv = rtenv

        self.rtenv.modules[self.module_name] = self

        self.rtenv.module_requirements[self.module_name] = _required_modules

        class Node(self.rtenv.db.db_base):

            __tablename__ = self.module_name + '.Node'

            node_id = sqlalchemy.Column(
                sqlalchemy.Integer,
                primary_key=True
                )

            parent_node_id = sqlalchemy.Column(
                sqlalchemy.Integer,
                nullable=False,
                default=0
                )

            content_type = sqlalchemy.Column(
                sqlalchemy.UnicodeText,
                nullable=False,
                default=None
                )

            content_id = sqlalchemy.Column(
                sqlalchemy.Integer,
                nullable=False,
                default=0
                )

        self.rtenv.models[self.module_name] = {
            'Node': Node
            }

class NodeAccesses(org.wayround.softengine.rtenv.ModulePrototype):

    def __init__(self, rtenv):

        self.module_name = 'org.wayround.softengine.modules.node_access'

        self.rtenv = rtenv

        self.rtenv.modules[self.module_name] = self

        self.rtenv.module_requirements[self.module_name] = _required_modules

        class NodeAccess(self.rtenv.db.db_base):

            __tablename__ = self.module_name + '.NodeAccess'

            node_id = sqlalchemy.Column(
                sqlalchemy.Integer,
                primary_key=True
                )

            owner_uid = sqlalchemy.Column(
                sqlalchemy.Integer,
                nullable=False,
                default=0
                )

            owner_gid = sqlalchemy.Column(
                sqlalchemy.Integer,
                nullable=False,
                default=0
                )

            user_read = sqlalchemy.Column(
                sqlalchemy.Boolean,
                nullable=False,
                default=False
                )

            user_write = sqlalchemy.Column(
                sqlalchemy.Boolean,
                nullable=False,
                default=False
                )

            user_execute = sqlalchemy.Column(
                sqlalchemy.Boolean,
                nullable=False,
                default=False
                )

            group_read = sqlalchemy.Column(
                sqlalchemy.Boolean,
                nullable=False,
                default=False
                )

            group_write = sqlalchemy.Column(
                sqlalchemy.Boolean,
                nullable=False,
                default=False
                )

            group_execute = sqlalchemy.Column(
                sqlalchemy.Boolean,
                nullable=False,
                default=False
                )

        self.rtenv.models[self.module_name] = {
            'NodeAccess': NodeAccess
            }


class Users(org.wayround.softengine.rtenv.ModulePrototype):

    def __init__(self, rtenv):

        self.module_name = 'org.wayround.softengine.modules.user'

        self.rtenv = rtenv

        self.rtenv.modules[self.module_name] = self

        self.rtenv.module_requirements[self.module_name] = _required_modules

        class User(self.rtenv.db.db_base):

            __tablename__ = self.module_name + '.User'

            name = sqlalchemy.Column(
                sqlalchemy.UnicodeText,
                primary_key=True
                )

            password = sqlalchemy.Column(
                sqlalchemy.UnicodeText,
                nullable=True,
                default=None
                )

            uid = sqlalchemy.Column(
                sqlalchemy.Integer,
                nullable=False,
                default=0
                )

            gid = sqlalchemy.Column(
                sqlalchemy.Integer,
                nullable=False,
                default=0
                )

            notes = sqlalchemy.Column(
                sqlalchemy.UnicodeText,
                nullable=True,
                default=None
                )

        self.rtenv.models[self.module_name] = {
            'User': User
            }

class Groups(org.wayround.softengine.rtenv.ModulePrototype):

    def __init__(self, rtenv):

        self.module_name = 'org.wayround.softengine.modules.group'

        self.rtenv = rtenv

        self.rtenv.modules[self.module_name] = self

        self.rtenv.module_requirements[self.module_name] = _required_modules

        class Group(self.rtenv.db.db_base):

            __tablename__ = self.module_name + '.Group'

            name = sqlalchemy.Column(
                sqlalchemy.UnicodeText,
                nullable=True,
                default=None
                )

            gid = sqlalchemy.Column(
                sqlalchemy.Integer,
                primary_key=True
                )

        self.rtenv.models[self.module_name] = {
            'Group': Group
            }

class GroupMemberships(org.wayround.softengine.rtenv.ModulePrototype):

    def __init__(self, rtenv):

        self.module_name = 'org.wayround.softengine.modules.group_membership'

        self.rtenv = rtenv

        self.rtenv.modules[self.module_name] = self

        self.rtenv.module_requirements[self.module_name] = _required_modules

        class GroupMembership(self.rtenv.db.db_base):

            __tablename__ = self.module_name + '.GroupMembership'

            ide = sqlalchemy.Column(
                sqlalchemy.Integer,
                name='id',
                primary_key=True
                )

            uid = sqlalchemy.Column(
                sqlalchemy.Integer,
                nullable=False
                )

            gid = sqlalchemy.Column(
                sqlalchemy.Integer,
                nullable=False
                )

        self.rtenv.models[self.module_name] = {
            'GroupMembership': GroupMembership
            }

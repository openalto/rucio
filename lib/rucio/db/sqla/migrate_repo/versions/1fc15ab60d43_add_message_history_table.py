# Copyright 2013-2019 CERN for the benefit of the ATLAS collaboration.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors:
# - Mario Lassnig <mario.lassnig@cern.ch>, 2015-2019
# - Vincent Garonne <vincent.garonne@cern.ch>, 2017

''' add message_history table '''

import datetime

import sqlalchemy as sa

from alembic import context
from alembic.op import create_table, drop_table

from rucio.db.sqla.types import GUID

# Alembic revision identifiers
revision = '1fc15ab60d43'
down_revision = '4783c1f49cb4'


def upgrade():
    '''
    Upgrade the database to this revision
    '''

    if context.get_context().dialect.name in ['oracle', 'mysql']:
        create_table('messages_history',
                     sa.Column('id', GUID()),
                     sa.Column('created_at', sa.DateTime, default=datetime.datetime.utcnow),
                     sa.Column('updated_at', sa.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
                     sa.Column('event_type', sa.String(1024)),
                     sa.Column('payload', sa.String(4000)))

    elif context.get_context().dialect.name == 'postgresql':
        pass


def downgrade():
    '''
    Downgrade the database to the previous revision
    '''

    if context.get_context().dialect.name in ['oracle', 'mysql']:
        drop_table('messages_history')

    elif context.get_context().dialect.name == 'postgresql':
        pass

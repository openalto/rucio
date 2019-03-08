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
# - Martin Barisits <martin.barisits@cern.ch>, 2015
# - Vincent Garonne <vincent.garonne@cern.ch>, 2017
# - Mario Lassnig <mario.lassnig@cern.ch>, 2019

''' created rule history tables '''

import datetime

import sqlalchemy as sa

from alembic import context
from alembic.op import create_table, create_index, drop_table, drop_index, create_primary_key

from rucio.db.sqla.constants import (DIDType, RuleGrouping, RuleState, RuleNotification)
from rucio.db.sqla.types import GUID


# Alembic revision identifiers
revision = '384b96aa0f60'
down_revision = '4cf0a2e127d4'


def upgrade():
    '''
    Upgrade the database to this revision
    '''

    if context.get_context().dialect.name in ['oracle', 'mysql']:
        create_table('rules_hist_recent',
                     sa.Column('history_id', GUID()),
                     sa.Column('id', GUID()),
                     sa.Column('subscription_id', GUID()),
                     sa.Column('account', sa.String(25)),
                     sa.Column('scope', sa.String(25)),
                     sa.Column('name', sa.String(255)),
                     sa.Column('did_type', DIDType.db_type()),
                     sa.Column('state', RuleState.db_type()),
                     sa.Column('error', sa.String(255)),
                     sa.Column('rse_expression', sa.String(255)),
                     sa.Column('copies', sa.SmallInteger),
                     sa.Column('expires_at', sa.DateTime),
                     sa.Column('weight', sa.String(255)),
                     sa.Column('locked', sa.Boolean()),
                     sa.Column('locks_ok_cnt', sa.BigInteger),
                     sa.Column('locks_replicating_cnt', sa.BigInteger),
                     sa.Column('locks_stuck_cnt', sa.BigInteger),
                     sa.Column('source_replica_expression', sa.String(255)),
                     sa.Column('activity', sa.String(50)),
                     sa.Column('grouping', RuleGrouping.db_type()),
                     sa.Column('notification', RuleNotification.db_type()),
                     sa.Column('stuck_at', sa.DateTime),
                     sa.Column('purge_replicas', sa.Boolean()),
                     sa.Column('ignore_availability', sa.Boolean()),
                     sa.Column('ignore_account_limit', sa.Boolean()),
                     sa.Column('updated_at', sa.DateTime, default=datetime.datetime.utcnow),
                     sa.Column('created_at', sa.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow))
        create_table('rules_history',
                     sa.Column('history_id', GUID()),
                     sa.Column('id', GUID()),
                     sa.Column('subscription_id', GUID()),
                     sa.Column('account', sa.String(25)),
                     sa.Column('scope', sa.String(25)),
                     sa.Column('name', sa.String(255)),
                     sa.Column('did_type', DIDType.db_type()),
                     sa.Column('state', RuleState.db_type()),
                     sa.Column('error', sa.String(255)),
                     sa.Column('rse_expression', sa.String(255)),
                     sa.Column('copies', sa.SmallInteger),
                     sa.Column('expires_at', sa.DateTime),
                     sa.Column('weight', sa.String(255)),
                     sa.Column('locked', sa.Boolean()),
                     sa.Column('locks_ok_cnt', sa.BigInteger),
                     sa.Column('locks_replicating_cnt', sa.BigInteger),
                     sa.Column('locks_stuck_cnt', sa.BigInteger),
                     sa.Column('source_replica_expression', sa.String(255)),
                     sa.Column('activity', sa.String(50)),
                     sa.Column('grouping', RuleGrouping.db_type()),
                     sa.Column('notification', RuleNotification.db_type()),
                     sa.Column('stuck_at', sa.DateTime),
                     sa.Column('purge_replicas', sa.Boolean()),
                     sa.Column('ignore_availability', sa.Boolean()),
                     sa.Column('ignore_account_limit', sa.Boolean()),
                     sa.Column('updated_at', sa.DateTime, default=datetime.datetime.utcnow),
                     sa.Column('created_at', sa.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow))
        create_primary_key('RULES_HIST_RECENT_PK', 'rules_hist_recent', ['history_id'])
        create_index('RULES_HIST_RECENT_ID_IDX', 'rules_hist_recent', ["id"])

    elif context.get_context().dialect.name == 'postgresql':
        pass


def downgrade():
    '''
    Downgrade the database to the previous revision
    '''

    if context.get_context().dialect.name in ['oracle', 'mysql']:
        drop_index('RULES_HIST_RECENT_ID_IDX', 'rules_hist_recent')
        drop_table('rules_hist_recent')
        drop_table('rules_history')

    elif context.get_context().dialect.name == 'postgresql':
        pass

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
# - Vincent Garonne <vincent.garonne@cern.ch>, 2014-2017
# - Mario Lassnig <mario.lassnig@cern.ch>, 2019

''' add tokens index '''

from alembic import context
from alembic.op import (create_foreign_key, create_index,
                        drop_constraint, drop_index)


# Alembic revision identifiers
revision = '49a21b4d4357'
down_revision = '2eef46be23d4'


def upgrade():
    '''
    Upgrade the database to this revision
    '''

    if context.get_context().dialect.name in ['oracle', 'mysql']:
        drop_constraint('tokens_account_fk', 'tokens', type_='foreignkey')
        create_index('TOKENS_ACCOUNT_EXPIRED_AT_IDX', 'tokens', ['account', 'expired_at'])
        create_foreign_key('tokens_account_fk', 'tokens', 'accounts', ['account'], ['account'])

    elif context.get_context().dialect.name == 'postgresql':
        pass


def downgrade():
    '''
    Downgrade the database to the previous revision
    '''

    if context.get_context().dialect.name in ['oracle', 'mysql']:
        drop_constraint('tokens_account_fk', 'tokens', type_='foreignkey')
        drop_index('TOKENS_ACCOUNT_EXPIRED_AT_IDX', 'tokens')
        create_foreign_key('tokens_account_fk', 'tokens', 'accounts', ['account'], ['account'])

    elif context.get_context().dialect.name == 'postgresql':
        pass

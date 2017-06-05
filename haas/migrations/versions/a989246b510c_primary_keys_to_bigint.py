"""Primary keys to BIGINT

Revision ID: a989246b510c
Revises: 3b2dab2e0d7d
Create Date: 2017-06-01 16:52:57.371068

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a989246b510c'
down_revision = '3b2dab2e0d7d'
branch_labels = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('headnode', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                        'headnode_id_seq'::regclass)"))
    op.alter_column('headnode', 'project_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=False)
    op.alter_column('hnic', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    autoincrement=True)
    op.alter_column('hnic', 'network_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=True)
    op.alter_column('hnic', 'owner_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=False)
    op.alter_column('metadata', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    autoincrement=True)
    op.alter_column('metadata', 'owner_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=False)
    op.alter_column('network', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                            'network_id_seq'::regclass)"))
    op.alter_column('network', 'owner_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=True)
    op.alter_column('network_attachment', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    autoincrement=True)
    op.alter_column('network_attachment', 'network_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=False)
    op.alter_column('network_attachment', 'nic_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=False)
    op.alter_column('network_projects', 'network_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=True)
    op.alter_column('network_projects', 'project_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=True)
    op.alter_column('networking_action', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    autoincrement=True)
    op.alter_column('networking_action', 'new_network_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=True)
    op.alter_column('networking_action', 'nic_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=False)
    op.alter_column('nic', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                            'nic_id_seq'::regclass)"))
    op.alter_column('nic', 'owner_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=False)
    op.alter_column('nic', 'port_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=True)
    op.alter_column('node', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                            'node_id_seq'::regclass)"))
    op.alter_column('node', 'project_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=True)
    op.alter_column('obm', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    autoincrement=True)
    op.alter_column('port', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                            'port_id_seq'::regclass)"))
    op.alter_column('port', 'owner_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=False)
    op.alter_column('project', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                            'project_id_seq'::regclass)"))
    op.alter_column('switch', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                            'switch_id_seq'::regclass)"))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('switch', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                            'switch_id_seq'::regclass)"))
    op.alter_column('project', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                            'project_id_seq'::regclass)"))
    op.alter_column('port', 'owner_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=False)
    op.alter_column('port', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                            'port_id_seq'::regclass)"))
    op.alter_column('obm', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    autoincrement=True)
    op.alter_column('node', 'project_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=True)
    op.alter_column('node', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                            'node_id_seq'::regclass)"))
    op.alter_column('nic', 'port_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=True)
    op.alter_column('nic', 'owner_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=False)
    op.alter_column('nic', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                            'nic_id_seq'::regclass)"))
    op.alter_column('networking_action', 'nic_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=False)
    op.alter_column('networking_action', 'new_network_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=True)
    op.alter_column('networking_action', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    autoincrement=True)
    op.alter_column('network_projects', 'project_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=True)
    op.alter_column('network_projects', 'network_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=True)
    op.alter_column('network_attachment', 'nic_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=False)
    op.alter_column('network_attachment', 'network_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=False)
    op.alter_column('network_attachment', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    autoincrement=True)
    op.alter_column('network', 'owner_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=True)
    op.alter_column('network', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval(\
                        'network_id_seq'::regclass)"))
    op.alter_column('metadata', 'owner_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=False)
    op.alter_column('metadata', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    autoincrement=True)
    op.alter_column('hnic', 'owner_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=False)
    op.alter_column('hnic', 'network_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=True)
    op.alter_column('hnic', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    autoincrement=True)
    op.alter_column('headnode', 'project_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=False)
    op.alter_column('headnode', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    autoincrement=True,
                    existing_server_default=sa.text(u"nextval('\
                            headnode_id_seq'::regclass)"))
    # ### end Alembic commands ###

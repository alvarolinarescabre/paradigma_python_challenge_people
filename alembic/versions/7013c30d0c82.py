"""baseline

Revision ID: 7013c30d0c82
Revises: 
Create Date: 2019-06-24 20:37:48.219013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7013c30d0c82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    people = op.create_table('people',
                            sa.Column('id', sa.Integer, primary_key = True),
                            sa.Column('name', sa.String(120), nullable = False, unique = True),
                            sa.Column('is_alive', sa.Integer, default = 1),
                            sa.Column('place_id', sa.Integer)
    )

    op.bulk_insert(people,
        [
            {'id':1, 'name':'Sensei Lamister', 'is_alive':1, 'place_id':1},
            {'id':2, 'name':'Aiba Stack', 'is_alive':1, 'place_id':2},
            {'id':3, 'name':'Joaquín Nevad', 'is_alive':1, 'place_id':3},
            {'id':4, 'name':'Dedo Gordo', 'is_alive':1, 'place_id':4},
            {'id':5, 'name':'Juanito Lamister', 'is_alive':1, 'place_id':1},
            {'id':6, 'name':'Nerf Stack', 'is_alive':1, 'place_id':2},
            {'id':7, 'name':'Chamo Nevad', 'is_alive':1, 'place_id':3},
            {'id':8, 'name':'Bonifacio Gordo', 'is_alive':1, 'place_id':4}            
        ],
        multiinsert = False 
    )

def downgrade():
        op.drop_table(
            'people'
    )

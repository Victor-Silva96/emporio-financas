"""Initial migration.

Revision ID: 47354395c3a9
Revises: 
Create Date: 2023-02-05 21:53:38.979789

"""
from alembic import op
import sqlalchemy as sa

from emporio import Collaborator, Service

# revision identifiers, used by Alembic.
revision = '47354395c3a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collaborator',
                    sa.Column('collaborator_id', sa.Integer(), nullable=False),
                    sa.Column('collaborator_name', sa.String(length=100), nullable=False),
                    sa.PrimaryKeyConstraint('collaborator_id')
                    )
    op.create_table('service',
                    sa.Column('service_id', sa.Integer(), nullable=False),
                    sa.Column('service_name', sa.String(length=100), nullable=False),
                    sa.Column('service_price', sa.Float(precision=2), nullable=True),
                    sa.PrimaryKeyConstraint('service_id')
                    )
    op.create_table('service_collaborator',
                    sa.Column('service_collaborator_id', sa.Integer(), nullable=False),
                    sa.Column('service_id', sa.Integer(), nullable=False),
                    sa.Column('collaborator_id', sa.Integer(), nullable=False),
                    sa.Column('client_name', sa.String(length=100), nullable=False),
                    sa.Column('service_collaborator_date', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['collaborator_id'], ['collaborator.collaborator_id'], ),
                    sa.ForeignKeyConstraint(['service_id'], ['service.service_id'], ),
                    sa.PrimaryKeyConstraint('service_collaborator_id')
                    )

    insert_collaborators()
    insert_services()
    # ### end Alembic commands ###


def insert_collaborators():
    op.bulk_insert(Collaborator.__table__,
                   [
                       {'collaborator_name': 'Kalina'},
                       {'collaborator_name': 'Luciana'},
                       {'collaborator_name': 'Rebeca'},
                       {'collaborator_name': 'Dayane'}
                   ])


def insert_services():
    op.bulk_insert(Service.__table__,
                   [
                       {'service_name': 'DESIGN DE SOBRANCELHA', 'service_price': 50.00},
                       {'service_name': 'DESIGN DE SOBRANCELHA COM HENNA', 'service_price': 60.00},
                       {'service_name': 'DESIGN DE SOBRANCELHA COM TINTURA', 'service_price': 65.00},
                       {'service_name': 'SÓ APLICAÇÃO DE HENNA', 'service_price': 30.00},
                       {'service_name': 'SÓ APLICAÇÃO DE TINTURA', 'service_price': 35.00},
                       {'service_name': 'SPA DA SOBRANCELHA', 'service_price': 30.00},
                       {'service_name': 'MAQUIAGEM', 'service_price': 120.00},
                       {'service_name': 'MAQUIAGEM COM CÍLIOS', 'service_price': 150.00},
                       {'service_name': 'ALONGAMENTO DE CÍLIOS', 'service_price': 120.00},
                       {'service_name': 'MANUTENÇÃO DE CÍLIOS', 'service_price': 100.00},
                       {'service_name': 'REMOÇÃO DE CÍLIOS', 'service_price': 30.00},
                       {'service_name': 'REMOÇÃO DE CÍLIOS', 'service_price': 30.00},
                       {'service_name': 'LIFTING DE CÍLIOS', 'service_price': 80.00},
                       {'service_name': 'CÍLIOS POSTIÇOS', 'service_price': 45.00},
                       {'service_name': 'DEPILAÇÃO BUÇO COM CERA', 'service_price': 30.00},
                       {'service_name': 'DEPILAÇÃO BUÇO COM LINHA', 'service_price': 35.00},
                       {'service_name': 'DEPILAÇÃO COSTELETA NA LINHA', 'service_price': 40.00},
                       {'service_name': 'DEPILAÇÃO SOBRANCELHA NA LINHA', 'service_price': 50.00},
                       {'service_name': 'DEPILAÇÃO QUEIXO', 'service_price': 25.00},
                       {'service_name': 'DEPILAÇÃO ROSTO', 'service_price': 60.00},
                       {'service_name': 'DEPILAÇÃO ORELHAS', 'service_price': 25.00},
                       {'service_name': 'DEPILAÇÃO SEIOS', 'service_price': 25.00},
                       {'service_name': 'DEPILAÇÃO AXILAS', 'service_price': 35.00},
                       {'service_name': 'DEPILAÇÃO AXILAS NA LINHA', 'service_price': 45.00},
                       {'service_name': 'DEPILAÇÃO BRAÇOS', 'service_price': 40.00},
                       {'service_name': 'DEPILAÇÃO FAIXA PARTE DA PERNA', 'service_price': 40.00},
                       {'service_name': 'DEPILAÇÃO LINHA ABDOMINAL', 'service_price': 35.00},
                       {'service_name': 'DEPILAÇÃO BARRIGA', 'service_price': 45.00},
                       {'service_name': 'DEPILAÇÃO COSTAS', 'service_price': 50.00},
                       {'service_name': 'DEPILAÇÃO PEDAÇO DAS COSTAS', 'service_price': 50.00},
                       {'service_name': 'DEPILAÇÃO VIRILHA', 'service_price': 40.00},
                       {'service_name': 'DEPILAÇÃO VIRILHA COMPLETA', 'service_price': 60.00},
                       {'service_name': 'DEPILAÇÃO X2', 'service_price': 35.00},
                       {'service_name': 'DEPILAÇÃO BORBOLETA', 'service_price': 65.00},
                       {'service_name': 'DEPILAÇÃO NÁDEGAS', 'service_price': 40.00},
                       {'service_name': 'DEPILAÇÃO PERNA COMPLETA', 'service_price': 60.00},
                       {'service_name': 'DEPILAÇÃO PERNA COMPLETA NA LINHA', 'service_price': 70.00},
                       {'service_name': 'DEPILAÇÃO MEIA PERNA', 'service_price': 40.00},
                       {'service_name': 'DEPILAÇÃO MEIA PERNA NA LINHA', 'service_price': 50.00},
                       {'service_name': 'DEPILAÇÃO COXA', 'service_price': 50.00},
                       {'service_name': 'DEPILAÇÃO PÉ', 'service_price': 20.00},
                       {'service_name': 'DEPILAÇÃO NARIZ', 'service_price': 25.00},
                       {'service_name': 'DEPILAÇÃO NARIZ COM LINHA', 'service_price': 30.00},
                       {'service_name': 'PODOLOGIA', 'service_price': 85.00},
                       {'service_name': 'PODOLOGIA + PINTURA', 'service_price': 95.00},
                       {'service_name': 'PODOLOGIA + MASSAGEM', 'service_price': 105.00},
                       {'service_name': 'REFLEXOLOGIA 30 MINUTOS', 'service_price': 75.00},
                       {'service_name': 'REFLEXOLOGIA 1 HORA', 'service_price': 105.00},
                       {'service_name': 'UNHA CONFECCIONADA COM CURATIVOS', 'service_price': 205.00},
                       {'service_name': 'APLICAÇÃO DE FIBRA', 'service_price': 80.00},
                       {'service_name': 'MANUTENÇÃO DE FIBRA', 'service_price': 65.00},
                       {'service_name': 'REMOÇÃO DE CALOS', 'service_price': 80.00},
                       {'service_name': 'MANICURE E PEDICURE', 'service_price': 55.00},
                       {'service_name': 'MANICURE', 'service_price': 40.00},
                       {'service_name': 'PEDICURE', 'service_price': 40.00},
                       {'service_name': 'SÓ PINTURA MÃO OU PÉ', 'service_price': 30.00},
                       {'service_name': 'SÓ PINTURA MÃO E PÉ', 'service_price': 50.00},
                       {'service_name': 'SPA DOS PÉS', 'service_price': 65.00},
                       {'service_name': 'HIDRATAÇÃO DE PARAFINA PARA OS PÉS', 'service_price': 40.00},
                       {'service_name': 'BANHO DE GEL', 'service_price': 65.00},
                       {'service_name': 'APLICAÇÃO UNHA GEL', 'service_price': 150.00},
                       {'service_name': 'MANUTENÇÃO EM GEL', 'service_price': 120.00},
                       {'service_name': 'UNHA POR UNIDADE GEL', 'service_price': 25.00},
                       {'service_name': 'APLICAÇÃO UNHA FIBRA', 'service_price': 130.00},
                       {'service_name': 'MANUTENÇÃO UNHA FIBRA', 'service_price': 100.00},
                       {'service_name': 'APLICAÇÃO UNHA PORCELANA', 'service_price': 120.00},
                       {'service_name': 'ESMALTAÇÃO GEL', 'service_price': 40.00},
                       {'service_name': 'REMOÇÃO GEL', 'service_price': 50.00},
                       {'service_name': 'BLINDAGEM', 'service_price': 40.00},
                       {'service_name': 'REMOÇÃO BLINDAGEM', 'service_price': 25.00},
                   ])


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service_collaborator')
    op.drop_table('service')
    op.drop_table('collaborator')
    # ### end Alembic commands ###
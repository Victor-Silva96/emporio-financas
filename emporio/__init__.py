from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from emporio.config import Config
from flask_migrate import Migrate
import sqlalchemy as sa

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    from emporio.services_collaborators.routes import services_collaborator
    from emporio.faturamento_pdf.routes import faturamento_pdf
    app.register_blueprint(services_collaborator)
    app.register_blueprint(faturamento_pdf)

    return app


class Service(db.Model):
    __tablename__ = 'service'
    service_id = sa.Column(sa.Integer, primary_key=True)
    service_name = sa.Column(sa.String(100), nullable=False)
    service_price = sa.Column(sa.Float(precision=2))


class Collaborator(db.Model):
    __tablename__ = 'collaborator'
    collaborator_id = sa.Column(sa.Integer, primary_key=True)
    collaborator_name = sa.Column(sa.String(100), nullable=False)


class ServiceCollaborator(db.Model):
    __tablename__ = 'service_collaborator'
    service_collaborator_id = sa.Column(sa.Integer, primary_key=True)
    service_id = sa.Column(sa.Integer, sa.ForeignKey('service.service_id'), nullable=False)
    collaborator_id = sa.Column(sa.Integer, sa.ForeignKey('collaborator.collaborator_id'), nullable=False)
    client_name = sa.Column(sa.String(100), nullable=False)
    service_collaborator_date = sa.Column(sa.DateTime, nullable=False)
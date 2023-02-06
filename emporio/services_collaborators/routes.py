from datetime import datetime

import flask
from flask import Blueprint, request, render_template

from emporio import Collaborator, db, Service, ServiceCollaborator

services_collaborator = Blueprint('services_collaborator', __name__)


@services_collaborator.route("/")
def home():
    result = {}
    services = db.session.execute(db.select(Service.service_id, Service.service_name)).all()
    collaborators = db.session.execute(
        db.select(Collaborator.collaborator_id, Collaborator.collaborator_name)).all()
    result['services'] = services
    result['collaborators'] = collaborators
    return render_template('service_collaborator/home.html', result=result)


@services_collaborator.route("/services_collaborator", methods=['POST'])
def insert_services_collaborator():
    services_collaborators_form = request.get_json()
    for service in services_collaborators_form['services']:
        db.session.add(
            ServiceCollaborator(service_id=service, collaborator_id=services_collaborators_form['collaborator'],
                                service_collaborator_date=datetime.now(),
                                client_name=services_collaborators_form['client']))
    db.session.commit()
    return flask.Response(status=201)

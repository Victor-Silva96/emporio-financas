from datetime import datetime
import flask
import pytz
from flask import Blueprint, request, render_template
from sqlalchemy import func

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
    date = datetime.strptime(services_collaborators_form['serviceData'], '%Y-%m-%d') \
        if services_collaborators_form['serviceData'] \
        else datetime.now(tz=pytz.timezone('America/Recife'))

    for service in services_collaborators_form['services']:
        db.session.add(
            ServiceCollaborator(service_id=service, collaborator_id=services_collaborators_form['collaborator'],
                                service_collaborator_date=date,
                                client_name=services_collaborators_form['client']))
    db.session.commit()
    return flask.Response(status=201)

@services_collaborator.route("/delete")
def delete():
    result = {}
    services = db.session.execute(db.select(Service.service_id, Service.service_name)).all()
    collaborators = db.session.execute(
        db.select(Collaborator.collaborator_id, Collaborator.collaborator_name)).all()
    result['services'] = services
    result['collaborators'] = collaborators
    return render_template('service_collaborator/delete.html', result=result)


@services_collaborator.route("/services_collaborator", methods=['DELETE'])
def delete_services_collaborator():
    services_collaborators_form = request.get_json()
    date = datetime.strptime(services_collaborators_form['serviceData'], '%Y-%m-%d') \
        if services_collaborators_form['serviceData'] \
        else datetime.now(tz=pytz.timezone('America/Recife'))

    result = ServiceCollaborator.query.filter(
        ServiceCollaborator.collaborator_id == services_collaborators_form['collaborator'],
        ServiceCollaborator.client_name == services_collaborators_form['client'],
        func.DATE(ServiceCollaborator.service_collaborator_date) == func.DATE(date),
        ServiceCollaborator.service_id.in_(services_collaborators_form['services'])).delete()
    print(result)
    db.session.commit()
    if result:
        return flask.Response(status=200)
    else:
        return flask.Response(status=404)

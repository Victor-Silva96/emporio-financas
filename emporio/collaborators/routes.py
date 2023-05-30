import flask
from flask import Blueprint, request, render_template
from emporio import Collaborator, db, ServiceCollaborator

collaborators = Blueprint('collaborators', __name__)


@collaborators.route("/collaborator")
def home():
    result = db.session.execute(
        db.select(Collaborator.collaborator_id, Collaborator.collaborator_name)).all()
    return render_template('collaborator/home.html', result=result)


@collaborators.route("/collaborator", methods=['PUT'])
def update_collaborator():
    collaborator_form = request.get_json()
    collaborator = db.session.execute(
        db.select(Collaborator).where(Collaborator.collaborator_id == collaborator_form['collaborator_id'])
    ).scalar_one()
    print(collaborator.collaborator_name)
    collaborator.collaborator_name = collaborator_form['collaborator_name']
    db.session.commit()
    return flask.Response(status=200)


@collaborators.route("/collaborator", methods=['DELETE'])
def delete_collaborator():
    collaborator_form = request.get_json()
    collaborator = db.session.execute(
        db.select(Collaborator).where(Collaborator.collaborator_id == collaborator_form['collaborator_id'])
    ).scalar_one_or_none()
    db.session.delete(collaborator)
    ServiceCollaborator.query.filter(ServiceCollaborator.collaborator_id == collaborator_form['collaborator_id']).delete()
    db.session.commit()
    return flask.Response(status=200)



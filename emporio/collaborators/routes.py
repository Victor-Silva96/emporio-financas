from flask import Blueprint, request, render_template
from emporio import Collaborator, db

collaborators = Blueprint('collaborators', __name__)


@collaborators.route("/collaborator")
def home():
    result = db.session.execute(
        db.select(Collaborator.collaborator_id, Collaborator.collaborator_name)).all()
    return render_template('collaborator/home.html', result=result)

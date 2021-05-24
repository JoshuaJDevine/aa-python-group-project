from flask import Blueprint, jsonify, session, request

# app.models imports go here:
from app.models import Skill, db

skills_routes = Blueprint('skills', __name__)


def validation_errors_to_error_messages(validation_errors):
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages

@skills_routes.route("/")
def skills():
    skills = Skill.query.all()
    return {"skills": [skill.to_dict() for skill in skills]}

@skills_routes.route('<int:id>')
def skill(id):
    skill = Skill.query.get(id)
    return skill.to_dict()

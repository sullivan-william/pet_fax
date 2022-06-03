from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix="/pets")

# Method to find specific pet, called later for show route
def find_pet(id):
    for pet in pets:
        if pet["pet_id"] == id:
            return pet

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/<int:pet_id>')
def show(pet_id):
    return render_template('show.html', pet=find_pet(pet_id))
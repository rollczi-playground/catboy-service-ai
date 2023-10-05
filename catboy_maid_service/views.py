## views.py
from flask import Blueprint, request, jsonify
from .models import db, Restaurant, Service, Catboy
from .forms import RestaurantForm, ServiceForm, CatboyForm

bp = Blueprint('views', __name__)

@bp.route('/restaurant', methods=['POST'])
def create_restaurant():
    form = RestaurantForm(request.form)
    if form.validate():
        restaurant = Restaurant(id=form.id.data, name=form.name.data, location=form.location.data, type=form.type.data)
        db.session.add(restaurant)
        db.session.commit()
        return jsonify(restaurant.to_dict()), 200
    else:
        return jsonify(form.errors), 400

@bp.route('/service', methods=['POST'])
def create_service():
    form = ServiceForm(request.form)
    if form.validate():
        service = Service(id=form.id.data, description=form.description.data, price=form.price.data)
        db.session.add(service)
        db.session.commit()
        return jsonify(service.to_dict()), 200
    else:
        return jsonify(form.errors), 400

@bp.route('/catboy', methods=['POST'])
def create_catboy():
    form = CatboyForm(request.form)
    if form.validate():
        catboy = Catboy(id=form.id.data, name=form.name.data, age=form.age.data, costume=form.costume.data)
        db.session.add(catboy)
        db.session.commit()
        return jsonify(catboy.to_dict()), 200
    else:
        return jsonify(form.errors), 400

@bp.route('/restaurant/<int:restaurant_id>/service', methods=['POST'])
def add_service_to_restaurant(restaurant_id):
    form = ServiceForm(request.form)
    if form.validate():
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant:
            service = Service(id=form.id.data, description=form.description.data, price=form.price.data)
            restaurant.add_service(service)
            db.session.commit()
            return jsonify(service.to_dict()), 200
        else:
            return jsonify({'error': 'Restaurant not found'}), 404
    else:
        return jsonify(form.errors), 400

@bp.route('/service/<int:service_id>/catboy', methods=['POST'])
def assign_catboy_to_service(service_id):
    form = CatboyForm(request.form)
    if form.validate():
        service = Service.query.get(service_id)
        if service:
            catboy = Catboy(id=form.id.data, name=form.name.data, age=form.age.data, costume=form.costume.data)
            service.catboys.append(catboy)
            db.session.commit()
            return jsonify(catboy.to_dict()), 200
        else:
            return jsonify({'error': 'Service not found'}), 404
    else:
        return jsonify(form.errors), 400

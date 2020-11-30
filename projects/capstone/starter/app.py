import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Ourhome, Cuisine
from auth import AuthError, requires_auth

MENUS_PER_PAGE = 10


def paginate_menus(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * MENUS_PER_PAGE
    end = start + MENUS_PER_PAGE

    menus = [menu.format() for menu in selection]
    current_menus = menus[start:end]

    return current_menus


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
    @ Set up CORS. Allow '*' for origins.
    '''
    CORS(app, resources={r"*": {"origins": "*"}})

    '''
    @ Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    '''
    @ Create an endpoint to handle GET requests
    for all available cuisines.
    '''
    @app.route('/cuisines', methods=['GET'])
    def get_cuisines():
        cuisines = Cuisine.query.all()

        if cuisines is None:
            abort(404)

        return jsonify({
            'success': True,
            'cuisines': {
                cuisine.id: cuisine.type for cuisine in cuisines
            },
            'total_cuisines': len(cuisines)
        })

    '''
    @ Create an endpoint to handle GET requests for menus,
    including pagination (every 10 menus).
    This endpoint should return a list of menus,
    number of total menus, current cuisine, cuisines.
    '''
    @app.route('/menus', methods=['GET'])
    def get_menus():
        selection = Ourhome.query.all()
        cuisines = Cuisine.query.all()

        current_menus = paginate_menus(request, selection)

        return jsonify({
            'success': True,
            'menus': current_menus,
            'total_menus': len(selection),
            'current_cuisine': list(set([menu['cuisine']
                                    for menu in current_menus])),
            'cuisines': {
                cuisine.id: cuisine.type for cuisine in cuisines
            }
        })

    '''
    @ Create an endpoint to GET menu using a menu ID
    '''
    @app.route('/menus/<int:menu_id>', methods=['GET'])
    def get_menu(menu_id):
        menu = Ourhome.query.filter(Ourhome.id == menu_id).one_or_none()

        if menu is None:
            abort(404)

        return jsonify({
            'success': True,
            'menu': menu.format()
        })

    '''
    @ Create an endpoint to DELETE menu using a menu ID.
    '''
    @app.route('/menus/<int:menu_id>', methods=['DELETE'])
    @requires_auth('edit:menu')
    def delete_menu(token, menu_id):
        try:
            menu = Ourhome.query.filter(Ourhome.id == menu_id).one_or_none()

            if menu is None:
                abort(404)

            menu.delete()
            selection = Ourhome.query.all()
            current_menus = paginate_menus(request, selection)

            return jsonify({
                'success': True,
                'deleted': menu_id,
                'menus': current_menus,
                'total_menus': len(selection)
            })

        except Exception:
            abort(400)

    '''
    @ Create an endpoint to PATCH a exist menu,
    which will require the menu and description text,
    cuisine, and preference score.
    '''
    @app.route('/menus/<int:menu_id>', methods=['PATCH'])
    @requires_auth('edit:menu')
    def edit_menu(token, menu_id):
        body = request.get_json()

        new_menu = body.get('menu', None)
        new_description = body.get('description', None)
        new_cuisine = body.get('cuisine', None)
        new_preference = body.get('preference', None)

        menu = Ourhome.query.filter(Ourhome.id == menu_id).one_or_none()

        if menu is None:
            abort(404)

        menu.menu = new_menu
        menu.description = new_description
        menu.cuisine = new_cuisine
        menu.preference = new_preference

        menu.update()

        selection = Ourhome.query.all()
        current_menus = paginate_menus(request, selection)

        return jsonify({
            'success': True,
            'edited': menu_id,
            'menus': current_menus,
            'total_menus': len(selection)
        })

    '''
    @ Create an endpoint to POST a new menu,
    which will require the menu and description text,
    cuisine, and preference score.
    '''
    @app.route('/menus', methods=['POST'])
    @requires_auth('edit:menu')
    def create_menu(token):
        body = request.get_json()

        new_menu = body.get('menu', None)
        new_description = body.get('description', None)
        new_cuisine = body.get('cuisine', None)
        new_preference = body.get('preference', None)

        try:
            menu = Ourhome(
                menu=new_menu,
                description=new_description,
                cuisine=new_cuisine,
                preference=new_preference)
            menu.insert()

            selection = Ourhome.query.all()
            current_menus = paginate_menus(request, selection)

            return jsonify({
                'success': True,
                'created': menu.id,
                'menus': current_menus,
                'total_menus': len(selection)
            })

        except Exception:
            abort(400)

    '''
    @ Create a POST endpoint to get menus based on a search term.
    It should return any menus for whom the search term
    is a substring of the menu.
    '''
    @app.route('/menus_search', methods=['POST'])
    def menus_search():
        body = request.get_json()
        search = body.get('searchTerm', None)

        try:
            selection = Ourhome.query.filter(
                                Ourhome.menu.ilike('%{}%'.format(search)))
            current_menus = paginate_menus(request, selection)

            return jsonify({
                'success': True,
                'menus': current_menus,
                'total_menus': len(current_menus)
            })

        except Exception:
            abort(400)

    '''
    @ Create a GET endpoint to get menus based on cuisine.
    '''
    @app.route('/cuisines/<int:cuisine_id>', methods=['GET'])
    def menus_by_cuisine(cuisine_id):
        try:
            selection = Ourhome.query.filter_by(cuisine=str(cuisine_id)).all()
            current_menus = paginate_menus(request, selection)

            if len(current_menus) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'menus': current_menus,
                'total_menus': len(selection)
            })

        except Exception:
            abort(400)

    '''
    @ Create a POST endpoint to get menu to eat the meal.
    This endpoint should take cuisine parameters and return
    a random menu within the given cuisine.
    '''
    @app.route('/ourhome', methods=['POST'])
    @requires_auth('eat:menu')
    def ourhome(token):
        try:
            body = request.get_json()

            menu_cuisine = body.get('menu_cuisine', None)
            menus_pool = Ourhome.query.all()

            menus = []
            for menu in menus_pool:
                if str(menu.format()['cuisine']) == menu_cuisine:
                    menus.append(menu.format())

            menu = random.choice(menus)

            return jsonify({
                'success': True,
                'menu': menu
            })

        except Exception:
            abort(400)

    # Error Handling
    '''
    @ implement error handler for AuthError
        error handler should conform to general task
    '''
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad_request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "forbidden"
        }), 403

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    '''
    @ implement error handler for 404
        error handler should conform to general task above
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

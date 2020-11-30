import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Ourhome, Cuisine


class OurhomeTestCase(unittest.TestCase):
    """This class represents the ourhome test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "ourhome_test"
        self.database_path = "postgresql://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_menu = {
            'menu': 'test',
            'description': "test_desc",
            'cuisine': 5,
            'preference': 1
        }

        self.updated_menu = {
            'menu': 'test_updated',
            'description': 'test_desc_updated',
            'cuisine': 4,
            'preference': 2
        }

        self.search_term = {
            'searchTerm': 'beef'
        }

        self.menu_cuisine = {
            'menu_cuisine': '1'
        }

        nutritionist_token = os.environ['NUTRITIONIST_TOKEN']

        self.nutritionist = {
            'Authorization': 'Bearer ' + nutritionist_token
        }

        student_token = os.environ['STUDENT_TOKEN']

        self.student = {
            'Authorization': 'Bearer ' + student_token
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    Write at least one test for expected success
    and error behavior for each endpoint using the unittest library.
    Write tests demonstrating role-based access control, at least two per role.
    """
    def test_get_paginated_menus(self):
        res = self.client().get('/menus')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_menus'])
        self.assertTrue(len(data['menus']))

    def test_get_menu_by_id(self):
        res = self.client().get('/menus/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['menu'])

    def test_get_menu_by_beyond_valid_id(self):
        res = self.client().get('/menus/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_menu_without_auth(self):
        res = self.client().post('/menus')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(
              data['code'],
              'authorization_header_missing')
        self.assertEqual(
              data['description'],
              'Authorization header is expected.')

    def test_delete_menu_by_id_without_auth(self):
        res = self.client().delete('/menus/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(
                data['code'],
                'authorization_header_missing')
        self.assertEqual(
                data['description'],
                'Authorization header is expected.')

    def test_edit_menu_by_id_without_auth(self):
        res = self.client().patch('/menus/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(
                data['code'],
                'authorization_header_missing')
        self.assertEqual(
                data['description'],
                'Authorization header is expected.')

    def test_get_cuisines(self):
        res = self.client().get('/cuisines')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['cuisines'])
        self.assertTrue(data['total_cuisines'])

    def test_create_menu_with_auth(self):
        res = self.client().post(
                '/menus',
                json=self.new_menu,
                headers=self.nutritionist)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['menus'])
        self.assertTrue(data['total_menus'])

    def test_edit_menu_with_auth(self):
        res = self.client().patch(
                '/menus/15',
                json=self.updated_menu,
                headers=self.nutritionist)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['edited'])
        self.assertTrue(data['menus'])
        self.assertTrue(data['total_menus'])

    def test_delete_menu_with_auth(self):
        res = self.client().delete(
                '/menus/17',
                headers=self.nutritionist)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        self.assertTrue(data['menus'])
        self.assertTrue(data['total_menus'])

    def test_search_menu_by_term(self):
        res = self.client().post(
                'menus_search',
                json=self.search_term)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['menus'])
        self.assertTrue(data['total_menus'])

    def test_get_menus_by_cuisine(self):
        res = self.client().get('/cuisines/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['menus'])
        self.assertTrue(data['total_menus'])

    def test_get_menus_by_not_exist_cuisine(self):
        res = self.client().get('/cuisines/6')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad_request')

    def test_get_meal_at_cafeteria_with_auth(self):
        res = self.client().post(
                '/ourhome',
                json=self.menu_cuisine,
                headers=self.student)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['menu'])

    def test_get_meal_at_cafeteria_without_auth(self):
        res = self.client().post(
                'ourhome',
                json=self.menu_cuisine)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(
                data['description'],
                'Authorization header is expected.')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

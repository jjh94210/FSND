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
    self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
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

    self.nutritionist = {
      'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlNMNmFtaXA1NHlCcksyNTF0cU1oZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYXV0aG8udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYmQzMzMyZDFmMzZlMDA3Njc4MGE3NSIsImF1ZCI6Im91cmhvbWUiLCJpYXQiOjE2MDY1NDg2MjYsImV4cCI6MTYwNjYzNDkyNiwiYXpwIjoiWUxhSWxvZ2ZucWpsYVpYb0J5dm1TUnFRTGFJZHRsOHgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImVhdDptZW51IiwiZWRpdDptZW51Il19.m21-cvKir7wdfFq08HBmyTmWncMMLgEUXEoTjbKspMRJhtG30fB8ZzCWHld6oWl8msH5HibiOCFhtbs4Ewcv_mTJIcoMU5-2l_qhyTrRc60JzDMxfltDOrfPCySt_hqIntgvh9211Pyg8LcRZkQdzGRZHvIVgepNefhdLfd7Q7dGl002o87shPaZRM5mzWbYJVxQxin2uVg7YNljRUecXBejPQ6rtoqEudG8m6IKf7Zfj7HpyuNWjlnY7YDGH4ayeBQlIWd39K8izzYHt1YpPzDcYGvQACumJ-mVu5p5fnovQ-ojGnX-ajkQuaiBy7haNoxDU1Lrk46GnD-SOsAUHQ'
    }

    self.student = {
      'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlNMNmFtaXA1NHlCcksyNTF0cU1oZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYXV0aG8udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYzEzMzM1MTE4ZDBmMDA2ZmEwZDRiZCIsImF1ZCI6Im91cmhvbWUiLCJpYXQiOjE2MDY1NDg3MTUsImV4cCI6MTYwNjYzNTAxNSwiYXpwIjoiWUxhSWxvZ2ZucWpsYVpYb0J5dm1TUnFRTGFJZHRsOHgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImVhdDptZW51Il19.NN1RXrx-lYVtQpES_YpvA21qOW2fIw6gMOuJxlSVCORnwtby3ksIK5qUicrepoB5bx-rK-O1MhjGA_6NJ1jpfjhWM2Jc0gdkC8SGJdI3jE11uzgodfR-fFqC3n1cPczxzNGVigemGLQOXbZoTG6uUMnBDY_-XPUYQNsZxSG2-kEJq_tzF9tSu_ZzkcWxTV0Bx8wL4n6nYk5TwHjLHwGBNX1W0VkX8-TTch-rFODY5eIPkdaaLKDE9zIN8_L6WTSxg_BkHqP0mpSPCmvV_7MFKAU_qUPkqo0Ptq5goglQL_9slf9sFQYrbEJreJYeIogL2w2t5gJpZ_AjFj9Lnfjx4g'
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
  Write at least one test for expected success and error behavior for each endpoint using the unittest library.
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
    self.assertEqual(data['code'],'authorization_header_missing')
    self.assertEqual(data['description'], 'Authorization header is expected.')

  def test_delete_menu_by_id_without_auth(self):
    res = self.client().delete('/menus/1')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
    self.assertEqual(data['code'],'authorization_header_missing')
    self.assertEqual(data['description'], 'Authorization header is expected.')

  def test_edit_menu_by_id_without_auth(self):
    res = self.client().patch('/menus/1')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
    self.assertEqual(data['code'],'authorization_header_missing')
    self.assertEqual(data['description'], 'Authorization header is expected.')

  def test_get_cuisines(self):
    res = self.client().get('/cuisines')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['cuisines'])
    self.assertTrue(data['total_cuisines'])

  def test_create_menu_with_auth(self):
    res = self.client().post('/menus', json=self.new_menu, headers=self.nutritionist)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['created'])
    self.assertTrue(data['menus'])
    self.assertTrue(data['total_menus'])

  def test_edit_menu_with_auth(self):
    res = self.client().patch('/menus/15', json=self.updated_menu, headers=self.nutritionist)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['edited'])
    self.assertTrue(data['menus'])
    self.assertTrue(data['total_menus'])

  def test_delete_menu_with_auth(self):
    res = self.client().delete('/menus/17', headers=self.nutritionist)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['deleted'])
    self.assertTrue(data['menus'])
    self.assertTrue(data['total_menus'])

  def test_search_menu_by_term(self):
    res = self.client().post('menus_search', json=self.search_term)
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
    res = self.client().post('/ourhome', json=self.menu_cuisine, headers=self.student)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['menu'])

  def test_get_meal_at_cafeteria_without_auth(self):
    res = self.client().post('ourhome', json=self.menu_cuisine)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
    self.assertEqual(data['code'],'authorization_header_missing')
    self.assertEqual(data['description'], 'Authorization header is expected.')

# Make the tests conveniently executable
if __name__ == "__main__":
  unittest.main()
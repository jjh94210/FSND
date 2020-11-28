# Ourhome Cafeteria Menu Lookup and Recommendation Service
This project is my capstone project of this course. It provides menu lookup service for nutritionist and student. Everyone can lookup and search menus. Also everyone can lookup menus by cuisine. Nutritionist can create and edit menus. Student and nutritionist can eat random recommended menu by Ourhome Cafeteria.

There are 2 roles: Nutritionist, Student.
Nutritionist can access every endpoint and only admin can create and edit data. Student can only access to the public endpoints and eat random recommended menu by Ourhome Cafeteria. Here's the details.

## Nutritionist
- edit:menu
- eat:menu

## Student
- eat:menu


# Getting Started
The application is run on https://fsnd-ourhome.herokuapp.com/ by default.
The authorization page is https://fsnd-autho.us.auth0.com/authorize?audience=ourhome&response_type=token&client_id=YLaIlogfnqjlaZXoByvmSRqQLaIdtl8x&redirect_uri=http://localhost:5000/menus

This application only has backend except the index page. At the provided authorization page, you can login as a specific role. After you logged in, use the token as a header.

### Installing Dependencies

#### Python 3.8.2

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the ourhome.psql file provided. From the starter folder in terminal run:
```bash
psql ourhome < ourhome.psql
```

## Running the server

From within the `starter` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use `app.py` file to find the application. 


# API Reference
- Base URL: https://fsnd-ourhome.herokuapp.com/
- Authentication: This project used Third-Party Authentication with Auth0. Please use the token out of the URL after you logged in and add it to 'Authentication: Bearer YOUR_TOKEN' as a header.


## Error Handling
Errors are returned as JSON objects in the following format:
```
{
  'success': False,
  'error': 422,
  'maessage': 'unprocessable',
}
```
The API will return four error types when requests fail:
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Resource Not Found
- 422: Unprocessable

## Endpoints

### Ourhome
---
### GET /menus
- General:
  - Returns a list of menu objects, success value, total number of menus, current cuisine, cuisines.
  - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1(default).
- Required Permission: All of the roles can access to this endpoint.
- Sample:
```
curl --request GET \
  --url 'https://fsnd-ourhome.herokuapp.com/menus'
```
- Response Sample
```
{
  "cuisines": {
    "1": "Korean",
    "2": "Western",
    "3": "Chinese",
    "4": "Japanese",
    "5": "Halal"
  },
  "current_cuisine": [
    "3",
    "4",
    "1",
    "2"
  ],
  "menus": [
    {
      "cuisine": "1",
      "description": "Ginseng (kor. sam) - chicken (kor. gye) - soup (kor. tang) in Korean, consists primarily of a whole young chicken (poussin) - filled with garlic, rice, jujube, and ginseng.",
      "id": 1,
      "menu": "ginseng chicken soup",
      "preference": 5
    },
    {
      "cuisine": "2",
      "description": "A meatball is ground meat rolled into a small ball, sometimes along with other ingredients, such as bread crumbs, minced onion, eggs, butter, and seasoning.",
      "id": 4,
      "menu": "Meatball",
      "preference": 3
    },
    {
      "cuisine": "2",
      "description": "A steak is a meat generally sliced across the muscle fibers, potentially including a bone. It is normally grilled, though can also be pan-fried.",
      "id": 5,
      "menu": "Steak",
      "preference": 1
    },
    {
      "cuisine": "2",
      "description": "Pasta is a type of food typically made from an unleavened dough of wheat flour mixed with water or eggs, and formed into sheets or other shapes, then cooked by boiling or baking.",
      "id": 6,
      "menu": "Pasta",
      "preference": 2
    },
    {
      "cuisine": "3",
      "description": "Jajangmyeon is a Chinese-style Korean noodle dish topped with a thick sauce made of chunjang, diced pork, and vegetables.",
      "id": 7,
      "menu": "Jajangmyeon",
      "preference": 1
    },
    {
      "cuisine": "3",
      "description": "Tangsuyuk is a Korean Chinese meat dish with sweet and sour sauce. It can be made with either pork or beef.",
      "id": 8,
      "menu": "Tangsuyuk",
      "preference": 3
    },
    {
      "cuisine": "3",
      "description": "Jjamppong is a Korean noodle soup with red, spicy seafood- or pork-based broth flavored with gochugaru (chili powder). Common ingredients include onions, garlic, Korean zucchini, carrots, cabbages, squid, mussels, and pork.",
      "id": 9,
      "menu": "Jjamppong",
      "preference": 4
    },
    {
      "cuisine": "4",
      "description": "Ramen is a Japanese noodle soup. It consists of Chinese wheat noodles served in a meat or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, nori (dried seaweed), menma, and scallions.",
      "id": 10,
      "menu": "Ramen",
      "preference": 2
    },
    {
      "cuisine": "4",
      "description": "Soba is the Japanese name for buckwheat. It usually refers to thin noodles made from buckwheat flour, or a combination of buckwheat and wheat flours (Nagano soba). They contrast to thick wheat noodles, called udon. Soba noodles are served either chilled with a dipping sauce, or in hot broth as a noodle soup.",
      "id": 11,
      "menu": "Soba",
      "preference": 1
    },
    {
      "cuisine": "4",
      "description": "Udon is a type of thick, wheat-flour noodle used frequently in Japanese cuisine. It is often served hot as a noodle soup in its simplest form, as kake udon, in a mildly flavoured broth called kakejiru, which is made of dashi, soy sauce, and mirin.",
      "id": 12,
      "menu": "Udon",
      "preference": 1
    }
  ],
  "success": true,
  "total_menus": 15
}
```


### POST /menus
- General:
  - Creates a new menu using the submitted data. Returns id of the created menu, success value, current_menus success and total number of menus. 
- Required Permission: 'edit:menu'. Nutritionist can access to this endpoint.
- Sample:
```
curl --request POST \
  --data '{"menu": "test", "description": "test_desc", "cuisine": "5", "preference": "3"}'\
  --header "Content-Type: application/json"\
  --url 'https://fsnd-ourhome.herokuapp.com/menus'\
  --header 'Authorization: Bearer YOUR_TOKEN'
```
- Response Sample
```
{
  "created": 18,
  "menus": [
    {
      "cuisine": "1",
      "description": "Ginseng (kor. sam) - chicken (kor. gye) - soup (kor. tang) in Korean, consists primarily of a whole young chicken (poussin) - filled with garlic, rice, jujube, and ginseng.",
      "id": 1,
      "menu": "ginseng chicken soup",
      "preference": 5
    },
    {
      "cuisine": "2",
      "description": "A meatball is ground meat rolled into a small ball, sometimes along with other ingredients, such as bread crumbs, minced onion, eggs, butter, and seasoning.",
      "id": 4,
      "menu": "Meatball",
      "preference": 3
    },
    {
      "cuisine": "2",
      "description": "A steak is a meat generally sliced across the muscle fibers, potentially including a bone. It is normally grilled, though can also be pan-fried.",
      "id": 5,
      "menu": "Steak",
      "preference": 1
    },
    {
      "cuisine": "2",
      "description": "Pasta is a type of food typically made from an unleavened dough of wheat flour mixed with water or eggs, and formed into sheets or other shapes, then cooked by boiling or baking.",
      "id": 6,
      "menu": "Pasta",
      "preference": 2
    },
    {
      "cuisine": "3",
      "description": "Jajangmyeon is a Chinese-style Korean noodle dish topped with a thick sauce made of chunjang, diced pork, and vegetables.",
      "id": 7,
      "menu": "Jajangmyeon",
      "preference": 1
    },
    {
      "cuisine": "3",
      "description": "Tangsuyuk is a Korean Chinese meat dish with sweet and sour sauce. It can be made with either pork or beef.",
      "id": 8,
      "menu": "Tangsuyuk",
      "preference": 3
    },
    {
      "cuisine": "3",
      "description": "Jjamppong is a Korean noodle soup with red, spicy seafood- or pork-based broth flavored with gochugaru (chili powder). Common ingredients include onions, garlic, Korean zucchini, carrots, cabbages, squid, mussels, and pork.",
      "id": 9,
      "menu": "Jjamppong",
      "preference": 4
    },
    {
      "cuisine": "4",
      "description": "Ramen is a Japanese noodle soup. It consists of Chinese wheat noodles served in a meat or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, nori (dried seaweed), menma, and scallions.",
      "id": 10,
      "menu": "Ramen",
      "preference": 2
    },
    {
      "cuisine": "4",
      "description": "Soba is the Japanese name for buckwheat. It usually refers to thin noodles made from buckwheat flour, or a combination of buckwheat and wheat flours (Nagano soba). They contrast to thick wheat noodles, called udon. Soba noodles are served either chilled with a dipping sauce, or in hot broth as a noodle soup.",
      "id": 11,
      "menu": "Soba",
      "preference": 1
    },
    {
      "cuisine": "4",
      "description": "Udon is a type of thick, wheat-flour noodle used frequently in Japanese cuisine. It is often served hot as a noodle soup in its simplest form, as kake udon, in a mildly flavoured broth called kakejiru, which is made of dashi, soy sauce, and mirin.",
      "id": 12,
      "menu": "Udon",
      "preference": 1
    }
  ],
  "success": true,
  "total_menus": 16
}
```


### POST /menus_search
- Parameter
  - searchTerm(Required): The keyword of the menu name which you want to find.
- General:
  - Search menus using the searchTerm parameter. Returns success value, searched menus list and numbers of them.
- Required Permission: All of the roles can access to this endpoint.
- Sample:
```
curl --request POST \
  --data '{"searchTerm": "pork"}'\
  --header "Content-Type: application/json"\
  --url 'https://fsnd-ourhome.herokuapp.com/menus_search'
```
- Response Sample
```
{
  "menus": [
    {
      "cuisine": "1",
      "description": "Thick, fatty slices of pork belly, sometimes with the skin left on and sometimes scored on the diagonal, are grilled on a slanted metal griddle or a gridiron at the diners table, inset with charcoal grills or convex gas burners.",
      "id": 2,
      "menu": "grilled pork belly (Samgyeopsal)",
      "preference": 5
    }
  ],
  "success": true,
  "total_menus": 1
}
```

### GET /mensu/{menu_id}
- General:
  - Returns success value, menu id and information of the menu.
- Required Permission: All of the roles can access to this endpoint.
- Sample:
```
curl --request GET \
  --url 'https://fsnd-ourhome.herokuapp.com/menus/1'
```
- Response Sample:
```
{
  "menu": {
    "cuisine": "1",
    "description": "Ginseng (kor. sam) - chicken (kor. gye) - soup (kor. tang) in Korean, consists primarily of a whole young chicken (poussin) - filled with garlic, rice, jujube, and ginseng.",
    "id": 1,
    "menu": "ginseng chicken soup",
    "preference": 5
  },
  "success": true
}
```


### DELETE /menus/{menu_id}
- General:
  - Delete a menu. Returns success value, id of deleted menu, list of current menus and total number of menus.
- Required Permission: 'edit:menu'. Nutritionist can access to this endpoint.
- Sample:
```
curl --request DELETE \
  --url 'https://fsnd-ourhome.herokuapp.com/menus/18' \
  --header 'Authorization: Bearer YOUR_TOKEN'
```
- Response Sample
```
{
  "deleted": 18,
  "menus": [
    {
      "cuisine": "1",
      "description": "Ginseng (kor. sam) - chicken (kor. gye) - soup (kor. tang) in Korean, consists primarily of a whole young chicken (poussin) - filled with garlic, rice, jujube, and ginseng.",
      "id": 1,
      "menu": "ginseng chicken soup",
      "preference": 5
    },
    {
      "cuisine": "2",
      "description": "A meatball is ground meat rolled into a small ball, sometimes along with other ingredients, such as bread crumbs, minced onion, eggs, butter, and seasoning.",
      "id": 4,
      "menu": "Meatball",
      "preference": 3
    },
    {
      "cuisine": "2",
      "description": "A steak is a meat generally sliced across the muscle fibers, potentially including a bone. It is normally grilled, though can also be pan-fried.",
      "id": 5,
      "menu": "Steak",
      "preference": 1
    },
    {
      "cuisine": "2",
      "description": "Pasta is a type of food typically made from an unleavened dough of wheat flour mixed with water or eggs, and formed into sheets or other shapes, then cooked by boiling or baking.",
      "id": 6,
      "menu": "Pasta",
      "preference": 2
    },
    {
      "cuisine": "3",
      "description": "Jajangmyeon is a Chinese-style Korean noodle dish topped with a thick sauce made of chunjang, diced pork, and vegetables.",
      "id": 7,
      "menu": "Jajangmyeon",
      "preference": 1
    },
    {
      "cuisine": "3",
      "description": "Tangsuyuk is a Korean Chinese meat dish with sweet and sour sauce. It can be made with either pork or beef.",
      "id": 8,
      "menu": "Tangsuyuk",
      "preference": 3
    },
    {
      "cuisine": "3",
      "description": "Jjamppong is a Korean noodle soup with red, spicy seafood- or pork-based broth flavored with gochugaru (chili powder). Common ingredients include onions, garlic, Korean zucchini, carrots, cabbages, squid, mussels, and pork.",
      "id": 9,
      "menu": "Jjamppong",
      "preference": 4
    },
    {
      "cuisine": "4",
      "description": "Ramen is a Japanese noodle soup. It consists of Chinese wheat noodles served in a meat or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, nori (dried seaweed), menma, and scallions.",
      "id": 10,
      "menu": "Ramen",
      "preference": 2
    },
    {
      "cuisine": "4",
      "description": "Soba is the Japanese name for buckwheat. It usually refers to thin noodles made from buckwheat flour, or a combination of buckwheat and wheat flours (Nagano soba). They contrast to thick wheat noodles, called udon. Soba noodles are served either chilled with a dipping sauce, or in hot broth as a noodle soup.",
      "id": 11,
      "menu": "Soba",
      "preference": 1
    },
    {
      "cuisine": "4",
      "description": "Udon is a type of thick, wheat-flour noodle used frequently in Japanese cuisine. It is often served hot as a noodle soup in its simplest form, as kake udon, in a mildly flavoured broth called kakejiru, which is made of dashi, soy sauce, and mirin.",
      "id": 12,
      "menu": "Udon",
      "preference": 1
    }
  ],
  "success": true,
  "total_menus": 15
}
```

### PATCH /menus/{menu_id}
- General:
  - Edit a menu. Returns success value, id of edited menu and list of current menus.
- Required Permission: 'edit:menu'. Nutritionist can access to this endpoint.
- Sample:
```
curl --request PATCH \
  --data '{"menu": "patch", "description": "patch_desc", "cuisine": "3", "preference": "2"}'\
  --header "Content-Type: application/json"\
  --url 'https://fsnd-ourhome.herokuapp.com/menus/19' \
  --header 'Authorization: Bearer YOUR_TOKEN'
```
- Response Sample
```
{
  "edited": 19,
  "menus": [
    {
      "cuisine": "1",
      "description": "Ginseng (kor. sam) - chicken (kor. gye) - soup (kor. tang) in Korean, consists primarily of a whole young chicken (poussin) - filled with garlic, rice, jujube, and ginseng.",
      "id": 1,
      "menu": "ginseng chicken soup",
      "preference": 5
    },
    {
      "cuisine": "2",
      "description": "A meatball is ground meat rolled into a small ball, sometimes along with other ingredients, such as bread crumbs, minced onion, eggs, butter, and seasoning.",
      "id": 4,
      "menu": "Meatball",
      "preference": 3
    },
    {
      "cuisine": "2",
      "description": "A steak is a meat generally sliced across the muscle fibers, potentially including a bone. It is normally grilled, though can also be pan-fried.",
      "id": 5,
      "menu": "Steak",
      "preference": 1
    },
    {
      "cuisine": "2",
      "description": "Pasta is a type of food typically made from an unleavened dough of wheat flour mixed with water or eggs, and formed into sheets or other shapes, then cooked by boiling or baking.",
      "id": 6,
      "menu": "Pasta",
      "preference": 2
    },
    {
      "cuisine": "3",
      "description": "Jajangmyeon is a Chinese-style Korean noodle dish topped with a thick sauce made of chunjang, diced pork, and vegetables.",
      "id": 7,
      "menu": "Jajangmyeon",
      "preference": 1
    },
    {
      "cuisine": "3",
      "description": "Tangsuyuk is a Korean Chinese meat dish with sweet and sour sauce. It can be made with either pork or beef.",
      "id": 8,
      "menu": "Tangsuyuk",
      "preference": 3
    },
    {
      "cuisine": "3",
      "description": "Jjamppong is a Korean noodle soup with red, spicy seafood- or pork-based broth flavored with gochugaru (chili powder). Common ingredients include onions, garlic, Korean zucchini, carrots, cabbages, squid, mussels, and pork.",
      "id": 9,
      "menu": "Jjamppong",
      "preference": 4
    },
    {
      "cuisine": "4",
      "description": "Ramen is a Japanese noodle soup. It consists of Chinese wheat noodles served in a meat or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, nori (dried seaweed), menma, and scallions.",
      "id": 10,
      "menu": "Ramen",
      "preference": 2
    },
    {
      "cuisine": "4",
      "description": "Soba is the Japanese name for buckwheat. It usually refers to thin noodles made from buckwheat flour, or a combination of buckwheat and wheat flours (Nagano soba). They contrast to thick wheat noodles, called udon. Soba noodles are served either chilled with a dipping sauce, or in hot broth as a noodle soup.",
      "id": 11,
      "menu": "Soba",
      "preference": 1
    },
    {
      "cuisine": "4",
      "description": "Udon is a type of thick, wheat-flour noodle used frequently in Japanese cuisine. It is often served hot as a noodle soup in its simplest form, as kake udon, in a mildly flavoured broth called kakejiru, which is made of dashi, soy sauce, and mirin.",
      "id": 12,
      "menu": "Udon",
      "preference": 1
    }
  ],
  "success": true,
  "total_menus": 16
}
```

### GET /cuisines/{cuisine_id}
- General:
  - Returns success value, list of menus by cuisine.
- Required Permission: All of the roles can access to this endpoint.
- Sample:
```
curl --request GET \
  --url 'https://fsnd-ourhome.herokuapp.com/cuisines/1'
```
- Response Sample
```
{
  "menus": [
    {
      "cuisine": "1",
      "description": "Ginseng (kor. sam) - chicken (kor. gye) - soup (kor. tang) in Korean, consists primarily of a whole young chicken (poussin) - filled with garlic, rice, jujube, and ginseng.",
      "id": 1,
      "menu": "ginseng chicken soup",
      "preference": 5
    },
    {
      "cuisine": "1",
      "description": "Thick, fatty slices of pork belly, sometimes with the skin left on and sometimes scored on the diagonal, are grilled on a slanted metal griddle or a gridiron at the diners table, inset with charcoal grills or convex gas burners.",
      "id": 2,
      "menu": "grilled pork belly (Samgyeopsal)",
      "preference": 5
    },
    {
      "cuisine": "1",
      "description": "Ox leg bone soup simmered for more than 10 hours until the soup is milky-white. Usually served in a bowl containing somyeon (thin wheat flour noodles) and pieces of beef. Sliced scallions and black pepper are used as condiments. Sometimes served with rice instead of noodles.",
      "id": 3,
      "menu": "beef bone soup (Gomguk)",
      "preference": 1
    }
  ],
  "success": true,
  "total_menus": 3
}
```

### POST /ourhome
- General:
  - Returns success value, recommended random menu by cuisine.
- Required Permission: 'eat:menu'. Nutritionist and student can access to this endpoint.
- Sample:
```
curl --request POST \
  --data '{"menu_cuisine": "1"}'\
  --header "Content-Type: application/json"\
  --url 'https://fsnd-ourhome.herokuapp.com/ourhome' \
  --header 'Authorization: Bearer YOUR_TOKEN'
```
- Response Sample:
```
{
  "menu": {
    "cuisine": "1",
    "description": "Thick, fatty slices of pork belly, sometimes with the skin left on and sometimes scored on the diagonal, are grilled on a slanted metal griddle or a gridiron at the diners table, inset with charcoal grills or convex gas burners.",
    "id": 2,
    "menu": "grilled pork belly (Samgyeopsal)",
    "preference": 5
  },
  "success": true
}
```

## Provided Tokens
- Nutritionist :
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlNMNmFtaXA1NHlCcksyNTF0cU1oZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYXV0aG8udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYmQzMzMyZDFmMzZlMDA3Njc4MGE3NSIsImF1ZCI6Im91cmhvbWUiLCJpYXQiOjE2MDY1NDg2MjYsImV4cCI6MTYwNjYzNDkyNiwiYXpwIjoiWUxhSWxvZ2ZucWpsYVpYb0J5dm1TUnFRTGFJZHRsOHgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImVhdDptZW51IiwiZWRpdDptZW51Il19.m21-cvKir7wdfFq08HBmyTmWncMMLgEUXEoTjbKspMRJhtG30fB8ZzCWHld6oWl8msH5HibiOCFhtbs4Ewcv_mTJIcoMU5-2l_qhyTrRc60JzDMxfltDOrfPCySt_hqIntgvh9211Pyg8LcRZkQdzGRZHvIVgepNefhdLfd7Q7dGl002o87shPaZRM5mzWbYJVxQxin2uVg7YNljRUecXBejPQ6rtoqEudG8m6IKf7Zfj7HpyuNWjlnY7YDGH4ayeBQlIWd39K8izzYHt1YpPzDcYGvQACumJ-mVu5p5fnovQ-ojGnX-ajkQuaiBy7haNoxDU1Lrk46GnD-SOsAUHQ
```
- Student :
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlNMNmFtaXA1NHlCcksyNTF0cU1oZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYXV0aG8udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYzEzMzM1MTE4ZDBmMDA2ZmEwZDRiZCIsImF1ZCI6Im91cmhvbWUiLCJpYXQiOjE2MDY1NDg3MTUsImV4cCI6MTYwNjYzNTAxNSwiYXpwIjoiWUxhSWxvZ2ZucWpsYVpYb0J5dm1TUnFRTGFJZHRsOHgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImVhdDptZW51Il19.NN1RXrx-lYVtQpES_YpvA21qOW2fIw6gMOuJxlSVCORnwtby3ksIK5qUicrepoB5bx-rK-O1MhjGA_6NJ1jpfjhWM2Jc0gdkC8SGJdI3jE11uzgodfR-fFqC3n1cPczxzNGVigemGLQOXbZoTG6uUMnBDY_-XPUYQNsZxSG2-kEJq_tzF9tSu_ZzkcWxTV0Bx8wL4n6nYk5TwHjLHwGBNX1W0VkX8-TTch-rFODY5eIPkdaaLKDE9zIN8_L6WTSxg_BkHqP0mpSPCmvV_7MFKAU_qUPkqo0Ptq5goglQL_9slf9sFQYrbEJreJYeIogL2w2t5gJpZ_AjFj9Lnfjx4g
```
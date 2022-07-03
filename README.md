# Full Stack Trivia API Project

This project is a gaming quiz application Called Trivia API
 allows users to play a trivia game and test their knowledge either for themselves or with friends. The project was create with unit testing and following:

- Display questions - both all questions and by category. Questions should
- show the question, category and difficulty rating by default and can show/hide the answer.

1. Delete questions.
2. Add questions and require that they include question and answer text.
3. Search for questions based on a text query string.
4. Play the quiz game, randomizing either all questions or within a specific category.

All backend code follows  **EP8 style guidelines <https://peps.python.org/pep-0008/>.**

## Getting Started

## Installing Dependencies

Developers should have Python3, pip3, node, and npm installed.

## Frontend dependencies

Installing Node and NPM
This project depends on Nodejs and Node Package Manager (NPM). Find and download Node and npm which is included at: <https://nodejs.com/en/download>.

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the frontend directory of this repository. After cloning, open your terminal and run:

 > npm install

## Backend Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the **backend** directory and running:

> pip install -r requirements.txt

## Running Your Frontend in Dev Environment

The frontend app was built using create-react-app. In order to run the app in development environment use npm start. You can change the script in the **package**.json file.

Open <http://localhost:3000> to view it in the browser. The page will reload if you make edits.

>npm start

## Running the server

From within the backend directory first ensure you are working using your created virtual environment.

> source env/bin/activate

## To run the server, execute

> export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

## Testing

To run the tests, run

> dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py

## API Reference

Getting Started
Base URL: Currently this application is only hosted locally. The backend is hosted at <http://127.0.0.1:5000/>
Authentication: This version does not require authentication or API keys.

## Error Handling

Errors are returned as JSON in the following format:

{
"error": 404,
"message": "resource not found",
"success": false
}

The API will return three types of errors:

400 – bad request
404 – resource not found
422 – unprocessable

## Endpoints

GET '/categories'

- Fetches  all available categories.
- Returns an object with a single key, categories, that contains a object of
- Sample: curl <http://127.0.0.1:5000/categories>
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}

## GET /questions

- Returns a list of questions
  - Results are paginated in groups of 10.
  - Also returns list of categories and total number of questions.
  - Sample: curl <http://127.0.0.1:5000/questions>

 {
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Muhammad Ali",
      "category": "4",
      "difficulty": 1,
      "id": 2,
      "question": "What boxer original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": "5",
      "difficulty": 4,
      "id": 3,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": "5",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 5,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 6,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": "6",
      "difficulty": 4,
      "id": 7,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 9,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "3",
      "difficulty": 3,
      "id": 10,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 11,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": "2",
      "difficulty": 1,
      "id": 12,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ],
  "success": true,
  "total_questions": 18
}

## DELETE /questions/<int:id>

- Deletes a question by id using url parameters.
- Returns id of deleted question upon success.
- Sample: curl <http://127.0.0.1:5000/questions/8> -X DELETE

  {
      "deleted": 8,
      "success": true
  }

## POST /questions

This endpoint either creates a new question or returns search results.

1. If no search term is included in request:

    - Creates a new question using JSON request parameters.
    - Returns JSON object with newly created question, as well as paginated questions.
  
- Sample: curl <http://127.0.0.1:5000/questions> -X POST -H "Content-Type: application/json" -d '{"question": "Who is the richest person in the world in 22?", "answer": "Elon Musk", "difficulty": 4, "category": "1" }'
{
  "created": 21,
  "question_created": "Who is the richest person in the world in 22?",
  "questions": [
    {
      "answer": "Muhammad Ali",
      "category": "4",
      "difficulty": 1,
      "id": 2,
      "question": "What boxer original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": "5",
      "difficulty": 4,
      "id": 3,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": "5",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 5,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 6,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": "6",
      "difficulty": 4,
      "id": 7,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 9,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "3",
      "difficulty": 3,
      "id": 10,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 11,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": "2",
      "difficulty": 1,
      "id": 12,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ],
  "success": true,
  "total_questions": 19
}

2 . If search term is included in request

    - Searches for questions using search term in JSON request parameters.
    - Returns JSON object with paginated matching questions.

- Sample: curl <http://127.0.0.1:5000/questions> -X POST -H "Content-Type: application/json" -d '{"searchTerm": "Who"}'

 {
  "questions": [
    {
      "answer": "Alexander Fleming",
      "category": "1",
      "difficulty": 3,
      "id": 17,
      "question": "1\tWho discovered penicillin?"
    },
    {
      "answer": "Elon Musk",
      "category": "1",
      "difficulty": 4,
      "id": 21,
      "question": "Who is the richest person in the world in 22?"
    }
  ],
  "success": true,
  "total_questions": 2
}

## POST /quizzes

- Allows users to play the quiz game.
- Uses JSON request parameters of category and previous questions.
- Returns JSON object with random question not among previous questions.
- Sample: curl <http://127.0.0.1:5000/quizzes> -X POST -H "Content-Type: application/json" -d '{"previous_questions": [20, 21], "quiz_category": {"type": "Science", "id": "1"}}'
{
  "question": {
    "answer": "The Liver",
    "category": "1",
    "difficulty": 4,
    "id": 16,
    "question": "What is the heaviest organ in the human body?"
  },
  "success": true
}

## Credit

Kerry McCarthy instructor of Trivia API.
 Udacity.
<ALX.com/>

import os, unittest, json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    
    def setUp(self):  
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
         "student", "student", "localhost:5432", self.database_name
      )
  
        setup_db(self.app, self.database_path)
  
        setup_db(self.app, self.database_path)
        
    
        # new question
        self.new_question = {
            'id': 23,
            'question': 'test question',
            'answer': 'test answer',
            'difficulty': 3,
            'category': 1,
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
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
       # test get categories
    def test_get_all_categories(self):
        response = self.client().get('/categories')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
    # test get questions

    def test_get_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        
        # test get questions with a wrong page parameter

    def test_get_questions_404(self):
        response = self.client().get('/questions?page=1000')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

       #delete a question with id 6
    def test_delete_question(self):
        response = self.client().delete('/questions/6')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'],6)
    
    

    # test create question

    def test_create_question(self):
        response = self.client().post('/questions', json=self.new_question)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_405_question_creation_not_allowed(self):
        response = self.client().post('/questions/50', json=self.new_question)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')  
        
    # test search with results

    def est_search_questions(self):
        response = self.client().post('/questions', json={'searchTerm': 'Rice'})

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        
      # send request with search that should fail
        response = self.client().post('/questions',json={'searchTerm': 'example'})
        
        
        
    # test get questions by category
    def test_get_questions_per_category(self):
        response = self.client().get('/categories/4/questions')
        data = json.loads(response.data)
        
        # ===============
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['current_category'], 'History')
        self.assertEqual(data['success'], True)


    def test_get_404_questions_category(self):
        response = self.client().get('/categories/2000/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['success'], False)
        
        
    # # test quiz
     # ===============
    def test_play_quiz(self):
        quiz_round = {'previous_questions': [], 'quiz_category': {'type': 'History', 'id': 4}}
        response = self.client().post('/quiz', json=quiz_round)
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_422_play_quiz(self):
        response = self.client().post('/quiz', json={})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
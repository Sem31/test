from django.test import TestCase, Client

# from django.client import Client
import requests


class StudentViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/api/student/'
        self.student_data = {
            "name": "John Doe",
            "age": 18,
            "grade": "A"
        }


    def test_create_student(self):
        response = self.client.post(self.url, self.student_data)
        self.assertEqual(response.status_code, 201)

    def test_get_students_list(self):
        response = self.client.post(self.url, self.student_data)
        self.assertEqual(response.status_code, 201)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

    def test_put_students(self):
        response = self.client.post(self.url, self.student_data)
        self.assertEqual(response.status_code, 201)

        id = str(response.json()['id'])
        update_response = self.client.put(self.url+id, {
            "name": "Kamlesh",
            "age": 18,
            "grade": "A"
        }, 'application/json')

        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()['name'], "Kamlesh")

    def test_delete_students(self):

        response = self.client.post(self.url, self.student_data)
        self.assertEqual(response.status_code, 201)

        id = str(response.json()['id'])
        delete_response = self.client.delete(self.url+id)
        self.assertEqual(delete_response.status_code, 204)

    def test_patch_students(self):
        response = self.client.post(self.url, self.student_data)
        self.assertEqual(response.status_code, 201)

        id = str(response.json()['id'])
        update_response = self.client.patch(self.url+id, {
            "name": "sem",
        }, 'application/json')

        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()['name'], "sem")
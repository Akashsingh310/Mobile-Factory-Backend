import json
import sys
import unittest

sys.path.append('.')

from main import app


class OrdersTestCase(unittest.TestCase):

    def test_create_order(self):
        test_client = app.test_client()

        input_data = {
            "components": ["B", "I", "K", "L"]
        }
        response = test_client.post('/orders', data=json.dumps(input_data), content_type='application/json')

        self.assertEqual(response.status_code, 201)

        expected_data = {
                "order_id": "some-id",
                "total": 141.38,
                "parts": ["OLED Screen", "Android OS", "Metallic Body", "Plastic Body"]
        }
        self.assertEqual(response.json, expected_data)

    def test_create_order1(self):
        test_client1 = app.test_client()

        input_data = {
            "components": ["A", "D", "F"]
        }

        response = test_client1.post('/orders', data=json.dumps(input_data), content_type='application/json')

        self.assertEqual(response.status_code, 201)

        expected_data = {
            "order_id": "some-id",
            "total": 54.99,
            "parts": ["LED Screen", "Wide-Angle Camera", "USB-C Port"]
        }
        self.assertEqual(response.json, expected_data)

    def test_create_order2(self):
        test_client2 = app.test_client()

        input_data = {
            "components": ["I", "J", "K"]
        }

        response = test_client2.post('/orders', data=json.dumps(input_data), content_type='application/json')

        self.assertEqual(response.status_code, 201)

        expected_data = {
            "order_id": "some-id",
            "total": 132.31,
            "parts": ["Android OS", "iOS OS", "Metallic Body"]
        }
        self.assertEqual(response.json, expected_data)

    def test_create_order3(self):
        test_client3 = app.test_client()

        input_data = {
            "components": ["B", "H", "J", "L"]
        }

        response = test_client3.post('/orders', data=json.dumps(input_data), content_type='application/json')

        self.assertEqual(response.status_code, 201)

        expected_data = {
            "order_id": "some-id",
            "total": 119.07,
            "parts": ["OLED Screen", "Lightning Port", "iOS OS", "Plastic Body"]
        }
        self.assertEqual(response.json, expected_data)


if __name__ == '__main__':
    unittest.main()

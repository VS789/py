from jsonschema import validate
import requests
import unittest
import HtmlTestRunner

class ApiTestsForJsonplaceholder(unittest.TestCase):

    schema = {"type": "object",
     "properties": {"id": {"type": "integer"}, "name": {"type": "string"}, "username": {"type": "string"},
                    "email": {"type": "string"}, "address": {"type": "object",
                                                             "properties": {"street": {"type": "string"},
                                                                            "suite": {"type": "string"},
                                                                            "city": {"type": "string"},
                                                                            "zipcode": {"type": "string"},
                                                                            "geo": {"type": "object",
                                                                                    "properties": {"lat": {
                                                                                        "type": "string"},
                                                                                        "lng": {
                                                                                            "type": "string"}},
                                                                                    "required": ["lat",
                                                                                                 "lng"]}},
                                                             "required": ["city", "geo", "street", "suite",
                                                                          "zipcode"]},
                    "phone": {"type": "string"}, "website": {"type": "string"}, "company": {"type": "object",
                                                                                            "properties": {
                                                                                                "name": {
                                                                                                    "type": "string"},
                                                                                                "catchPhrase": {
                                                                                                    "type": "string"},
                                                                                                "bs": {
                                                                                                    "type": "string"}},
                                                                                            "required": ["bs",
                                                                                                         "catchPhrase",
                                                                                                         "name"]}},
     "required": ["address", "company", "email", "id", "name", "phone", "username", "website"]}

    def setUp(self):
        self.r = requests.get('https://jsonplaceholder.typicode.com/users')

    def test_check_response_code_is_200(self):
        assert self.r.status_code == 200, 'Unexpected request response'

    def test_check_response_has_10_JSON_objects(self):
        assert len(self.r.json()) == 10, 'Unexpected number of objects'

    def test_make_JSON_validation_with_JSON_schema(self):
        for validation_element in self.r.json():
            assert (validate(validation_element, self.schema)) == None
            print(validate(validation_element, self.schema))

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./"))

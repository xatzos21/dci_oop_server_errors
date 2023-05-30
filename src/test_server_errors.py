import unittest
from server_errors import OK, NotFound, ServerError


class TestErrors(unittest.TestCase):
    def test_ok_error(self):
        ok_error = OK()
        self.assertEqual(ok_error.code, 200)
        self.assertEqual(ok_error.message, "OK")

    def test_not_found_error(self):
        not_found_error = NotFound()
        self.assertEqual(not_found_error.code, 404)
        self.assertEqual(not_found_error.message, "Not Found")

    def test_server_error(self):
        server_error = ServerError()
        self.assertEqual(server_error.code, 500)
        self.assertEqual(server_error.message, "Server Error")


if __name__ == "__main__":
    unittest.main()

from django.test import SimpleTestCase
from utils.settings_utils import get_env_list
import os


class TestGetEnvList(SimpleTestCase):

    def test_get_env_list_with_single_value(self):
        os.environ["TEST_ENV"] = "value1"
        result = get_env_list("TEST_ENV")
        self.assertEqual(result, ["value1"])

    def test_get_env_list_with_multiple_values(self):
        os.environ["TEST_ENV"] = "value1,value2,value3"
        result = get_env_list("TEST_ENV")
        self.assertEqual(result, ["value1", "value2", "value3"])

    def test_get_env_list_with_empty_string(self):
        os.environ["TEST_ENV"] = ""
        result = get_env_list("TEST_ENV")
        self.assertEqual(result, [])

    def test_get_env_list_with_no_env_variable(self):
        result = get_env_list("NON_EXISTENT_ENV")
        self.assertEqual(result, [])

    def test_get_env_list_with_non_string_variable_name(self):
        result = get_env_list(123)
        self.assertEqual(result, [])

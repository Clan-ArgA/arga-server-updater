import unittest
from argparse import Namespace, ArgumentTypeError
from typing import List, Optional

from app_start import parser_option


class TestParserOption(unittest.TestCase):
    def create_args(self, option: Optional[List[str]]) -> Namespace:
        return Namespace(server='arma3', mods='arga', option=option, repair=None)

    def test_server_option(self):
        expected = "c"
        args = self.create_args(["server"])
        actual = parser_option(args)
        self.assertEqual(expected, actual.option)

    def test_server_option_upper(self):
        expected = "c"
        args = self.create_args(["Server"])
        actual = parser_option(args)
        self.assertEqual(expected, actual.option)

    def test_mod_option(self):
        expected = "b"
        args = self.create_args(["mod"])
        actual = parser_option(args)
        self.assertEqual(expected, actual.option)

    def test_mods_option(self):
        expected = "b"
        args = self.create_args(["mods"])
        actual = parser_option(args)
        self.assertEqual(expected, actual.option)

    def test_server_and_mod_option(self):
        expected = "a"
        args = self.create_args(["server", "mod"])
        actual = parser_option(args)
        self.assertEqual(expected, actual.option)

    def test_server_and_mods_option(self):
        expected = "a"
        args = self.create_args(["server", "mods"])
        actual = parser_option(args)
        self.assertEqual(expected, actual.option)

    def test_multiple_bad_options(self):
        args = self.create_args(["a", "b"])
        with self.assertRaises(ArgumentTypeError):
            parser_option(args)

    def test_invalid_option(self):
        expected = "invalid"
        args = self.create_args(["invalid"])
        actual = parser_option(args)
        self.assertEqual(expected, actual.option)

    def test_no_options(self):
        expected = Namespace(server='arma3', mods='arga', option=None, repair=None)
        args = self.create_args(None)
        actual = parser_option(args)
        self.assertEqual(expected, actual)

from unittest import TestCase

from pycli.cli import main


class TestCmd(TestCase):
    def test_basic(self):
        main()

"""司璋（SIZHANG）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
import unittest

from sizhang import Sizhang


class TestSizhang(unittest.TestCase):
    def setUp(self):
        self.op = Sizhang()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "sizhang")
        self.assertEqual(d["code"], "SIZHANG")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_watch_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.watch(None)

    def test_patrol_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.patrol()


if __name__ == "__main__":
    unittest.main()

"""司璋（SIZHANG）算子单测：名帖完整、行为达标、只增不覆盖。"""
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

    def test_watch_patrol(self):
        self.op.watch({"kind": "compute"})
        self.op.watch({"kind": "exfiltrate"})
        self.assertTrue(self.op.watched[0]["allowed"])
        self.assertFalse(self.op.watched[1]["allowed"])
        p = self.op.patrol()
        self.assertEqual(p, {"watched": 2, "violations": 1})


if __name__ == "__main__":
    unittest.main()

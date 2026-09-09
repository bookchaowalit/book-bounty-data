import unittest

from book_bounty_data.capture import normalize
from book_bounty_data.cli import resource, validate


class SourceTests(unittest.TestCase):
    def raw(self):
        return (
            b"<h1>Rules of Engagement | GitHub Bug Bounty</h1>"
            b"<p>GitHub's Bug Bounty program is open to eligible external researchers.</p>"
            b"<p>Only test for vulnerabilities on sites you know to be operated by GitHub.</p>"
            b"<p>Legal safe harbor applies when you follow these rules.</p>"
            b"<p>Contact bounty@github.com if you are unsure.</p>"
            b"<p>Include written instructions for reproducing the vulnerability.</p>"
        )

    def test_github_rules_fixture(self):
        source = resource("source.json")
        data = normalize(self.raw(), source, "2026-09-07T00:00:00Z")
        item = data["items"][0]
        item["provenance"].update(
            raw_object_key="landing/test",
            bronze_manifest_key="control/manifests/test",
        )
        self.assertEqual(item["title"], "GitHub Bug Bounty Program")
        self.assertEqual(item["category"], "security")
        self.assertEqual(item["status"], "open")
        self.assertEqual(item["deadline"], {"kind": "rolling", "at": None})
        self.assertEqual(item["value"], {"kind": "variable", "amount": None, "currency": "USD", "guaranteed": False})
        self.assertIn("GitHub-operated", item["terms"]["authorization_scope"])
        self.assertEqual(validate(data)["schema_version"], source["schema_version"])

    def test_source_drift_rejected(self):
        with self.assertRaises(ValueError):
            normalize(b"<h1>unrelated page</h1>", resource("source.json"), "2026-09-07T00:00:00Z")

    def test_missing_lineage_rejected(self):
        data = normalize(self.raw(), resource("source.json"), "2026-09-07T00:00:00Z")
        with self.assertRaises(ValueError):
            validate(data)


if __name__ == "__main__":
    unittest.main()

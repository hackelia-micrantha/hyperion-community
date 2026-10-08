from __future__ import annotations

import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "web"
INDEX = WEB / "index.html"


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.fragment_links: list[str] = []
        self.script_count = 0
        self.title_depth = 0
        self.title_parts: list[str] = []
        self.description = ""

    def handle_starttag(self, tag: str, attrs) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)

        if tag == "a":
            href = values.get("href", "")
            if href.startswith("#") and len(href) > 1:
                self.fragment_links.append(href[1:])

        if tag == "script":
            self.script_count += 1

        if tag == "title":
            self.title_depth += 1

        if tag == "meta" and values.get("name") == "description":
            self.description = values.get("content", "").strip()

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_parts.append(data)


class StaticSiteContractTests(unittest.TestCase):
    def parser(self) -> SiteParser:
        parser = SiteParser()
        parser.feed(INDEX.read_text(encoding="utf-8"))
        return parser

    def test_site_is_static_and_workers_runtime_is_not_required(self):
        self.assertTrue(INDEX.is_file())
        for relative in (
            "wrangler.toml",
            "wrangler.jsonc",
            "web/wrangler.toml",
            "web/wrangler.jsonc",
        ):
            self.assertFalse(
                (ROOT / relative).exists(),
                f"{relative} introduces a Workers runtime into the static-site contract",
            )

        parser = self.parser()
        self.assertEqual(
            parser.script_count,
            0,
            "the current landing-page contract is static HTML/CSS with no JS runtime",
        )

    def test_page_has_basic_metadata(self):
        parser = self.parser()
        self.assertTrue("".join(parser.title_parts).strip())
        self.assertTrue(parser.description)

    def test_fragment_navigation_targets_exist(self):
        parser = self.parser()
        missing = sorted(set(parser.fragment_links) - parser.ids)
        self.assertEqual(missing, [], f"missing fragment targets: {missing}")


if __name__ == "__main__":
    unittest.main()

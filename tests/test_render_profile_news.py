from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.render_profile_news import parse_news, update_profile


NEWS = """---
title: 中文标题
titleEn: English title
date: 2026-08-28
tag: UPDATE
summary: 中文摘要
summaryEn: English summary
---

Long body that must not enter the Profile.
"""


class RenderProfileNewsTests(unittest.TestCase):
    def test_invalid_metadata_date_preserves_profile(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "README.md"
            original = "<!-- NEWS_START -->old<!-- NEWS_END -->"
            profile.write_text(original, encoding="utf-8")
            for value in ("2026-02-30", "20260828", "not-a-date"):
                with self.subTest(date=value):
                    (root / "news.md").write_text(
                        NEWS.replace("2026-08-28", value), encoding="utf-8"
                    )
                    with self.assertRaises(ValueError):
                        update_profile(profile, root, 1)
                    self.assertEqual(profile.read_text(encoding="utf-8"), original)

    def test_limit_selects_latest_metadata_date_instead_of_filename(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "README.md"
            news_dir = root / "news"
            news_dir.mkdir()
            profile.write_text("<!-- NEWS_START -->old<!-- NEWS_END -->", encoding="utf-8")
            (news_dir / "a-newest.md").write_text(
                NEWS.replace("2026-08-28", "2026-09-10").replace(
                    "English summary", "Newest summary"
                ), encoding="utf-8",
            )
            (news_dir / "z-oldest.md").write_text(NEWS, encoding="utf-8")
            update_profile(profile, news_dir, 1)
            result = profile.read_text(encoding="utf-8")
            self.assertIn("Newest summary", result)
            self.assertNotIn("2026-08-28", result)
            self.assertFalse(update_profile(profile, news_dir, 1))

    def test_non_positive_limit_preserves_profile(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "README.md"
            original = "<!-- NEWS_START -->old<!-- NEWS_END -->"
            profile.write_text(original, encoding="utf-8")
            (root / "news.md").write_text(NEWS, encoding="utf-8")
            for limit in (0, -1):
                with self.assertRaisesRegex(ValueError, "positive"):
                    update_profile(profile, root, limit)
                self.assertEqual(profile.read_text(encoding="utf-8"), original)

    def test_parse_requires_bilingual_summary(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "news.md"
            path.write_text(NEWS, encoding="utf-8")
            item = parse_news(path)
            self.assertEqual(item.title_en, "English title")
            self.assertEqual(item.summary_en, "English summary")

    def test_update_replaces_markers_with_summary_only(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "README.md"
            news_dir = root / "news"
            news_dir.mkdir()
            profile.write_text(
                "before\n<!-- NEWS_START -->old<!-- NEWS_END -->\nafter\n",
                encoding="utf-8",
            )
            (news_dir / "2026-08-28-update.md").write_text(NEWS, encoding="utf-8")

            self.assertTrue(update_profile(profile, news_dir, 3))
            result = profile.read_text(encoding="utf-8")
            self.assertIn("中文摘要", result)
            self.assertIn("English summary", result)
            self.assertNotIn("Long body", result)

    def test_empty_news_directory_fails_closed(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "README.md"
            news_dir = root / "news"
            news_dir.mkdir()
            profile.write_text(
                "<!-- NEWS_START -->old<!-- NEWS_END -->",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "no Markdown news files"):
                update_profile(profile, news_dir, 3)

    def test_summary_backslashes_are_literal(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "README.md"
            news_dir = root / "news"
            news_dir.mkdir()
            profile.write_text(
                "<!-- NEWS_START -->old<!-- NEWS_END -->",
                encoding="utf-8",
            )
            escaped_news = NEWS.replace("中文摘要", r"Windows 路径 C:\Users\player 和 \1")
            (news_dir / "2026-08-28-update.md").write_text(escaped_news, encoding="utf-8")

            self.assertTrue(update_profile(profile, news_dir, 3))
            result = profile.read_text(encoding="utf-8")
            self.assertIn(r"C:\Users\player", result)
            self.assertIn(r"\1", result)


if __name__ == "__main__":
    unittest.main()

"""Render concise bilingual website news into the organization Profile."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


MARKER_RE = re.compile(r"<!-- NEWS_START -->.*?<!-- NEWS_END -->", re.DOTALL)


@dataclass(frozen=True)
class NewsItem:
    date: str
    title: str
    title_en: str
    summary: str
    summary_en: str


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_news(path: Path) -> NewsItem:
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", raw, re.DOTALL)
    if not match:
        raise ValueError(f"missing front matter: {path}")

    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if separator:
            metadata[key.strip()] = _unquote(value)

    required = ("date", "title", "titleEn", "summary", "summaryEn")
    missing = [key for key in required if not metadata.get(key)]
    if missing:
        raise ValueError(f"missing {', '.join(missing)}: {path}")

    return NewsItem(
        date=metadata["date"],
        title=metadata["title"],
        title_en=metadata["titleEn"],
        summary=metadata["summary"],
        summary_en=metadata["summaryEn"],
    )


def render(items: list[NewsItem]) -> str:
    sections = []
    for item in sorted(items, key=lambda current: current.date, reverse=True):
        sections.append(
            f"### {item.date} — {item.title}\n\n"
            f"{item.summary}\n\n"
            f"**{item.title_en}** — {item.summary_en}"
        )
    return "<!-- NEWS_START -->\n\n" + "\n\n".join(sections) + "\n\n<!-- NEWS_END -->"


def update_profile(profile: Path, news_dir: Path, limit: int) -> bool:
    files = sorted(news_dir.glob("*.md"), reverse=True)[:limit]
    if not files:
        raise ValueError(f"no Markdown news files found in {news_dir}")

    content = profile.read_text(encoding="utf-8")
    if not MARKER_RE.search(content):
        raise ValueError(f"NEWS markers not found in {profile}")

    rendered = render([parse_news(path) for path in files])
    updated = MARKER_RE.sub(lambda _match: rendered, content)
    if updated == content:
        return False
    profile.write_text(updated, encoding="utf-8", newline="\n")
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("profile", type=Path)
    parser.add_argument("news_dir", type=Path)
    parser.add_argument("--limit", type=int, default=3)
    args = parser.parse_args()
    update_profile(args.profile, args.news_dir, args.limit)


if __name__ == "__main__":
    main()

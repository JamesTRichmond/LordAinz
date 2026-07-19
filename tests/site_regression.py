"""Dependency-free regression checks for the interactive site surface."""

from html.parser import HTMLParser
from collections import Counter
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
MINIMUM_LIVE_REGIONS = 2  # one for demo-valence and one for demo-flatlander
INTERACTIVE_BEHAVIORS = (
    (
        "reveal button click handler",
        r"""btnReveal\.addEventListener\(\s*["']click["']\s*,\s*reveal\s*\)""",
    ),
    (
        "next-round button click handler",
        r"""btnNext\.addEventListener\(\s*["']click["']\s*,\s*newRound\s*\)""",
    ),
    (
        "valence slider input listener",
        r"""slider\.addEventListener\(\s*["']input["']\s*,\s*render\s*\)""",
    ),
    (
        "reveal button pressed-state update",
        r"""btnReveal\.setAttribute\(\s*["']aria-pressed["']\s*,\s*["']true["']\s*\)""",
    ),
)


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


def main():
    html_path = ROOT / "index.html"
    html = html_path.read_text(encoding="utf-8")
    parser = SiteParser()
    parser.feed(html)

    ids = [attrs["id"] for _, attrs in parser.elements if "id" in attrs]
    duplicates = sorted(item for item, count in Counter(ids).items() if count > 1)
    assert not duplicates, f"duplicate ids: {', '.join(duplicates)}"

    by_id = {
        attrs["id"]: (tag, attrs)
        for tag, attrs in parser.elements
        if "id" in attrs
    }
    required_elements = {
        "demo-valence": "article",
        "vf-slider": "input",
        "vf-gauge-grounded": "canvas",
        "vf-gauge-blind": "canvas",
        "vf-caption": "p",
        "demo-flatlander": "article",
        "fl-canvas-a": "canvas",
        "fl-canvas-b": "canvas",
        "fl-reveal": "button",
        "fl-next": "button",
        "fl-prompt": "p",
        "codex": "section",
    }
    for element_id, expected_tag in required_elements.items():
        assert element_id in by_id, f"missing #{element_id}"
        actual_tag, _ = by_id[element_id]
        assert actual_tag == expected_tag, (
            f"#{element_id} should be <{expected_tag}>, found <{actual_tag}>"
        )

    canvases = [
        attrs
        for tag, attrs in parser.elements
        if tag == "canvas" and attrs.get("aria-hidden") != "true"
    ]
    for attrs in canvases:
        canvas_name = attrs.get("id", "unnamed canvas")
        assert attrs.get("role") == "img", (
            f"{canvas_name} is missing role=img"
        )
        assert attrs.get("aria-label"), (
            f"{canvas_name} is missing an accessible label"
        )

    live_regions = [
        attrs
        for tag, attrs in parser.elements
        if attrs.get("aria-live") == "polite"
    ]
    assert len(live_regions) >= MINIMUM_LIVE_REGIONS, (
        f"expected at least {MINIMUM_LIVE_REGIONS} live regions, "
        f"found {len(live_regions)}"
    )

    pick_values = {
        attrs["data-pick"]
        for tag, attrs in parser.elements
        if tag == "button" and "data-pick" in attrs
    }
    assert pick_values == {"A", "B"}, (
        "demo-flatlander must provide A and B choices"
    )

    scripts = {
        attrs.get("src"): attrs
        for tag, attrs in parser.elements
        if tag == "script"
    }
    for script in ("throne.js", "reliquary.js"):
        if script not in scripts:
            raise AssertionError(f"{script} is not referenced")
        assert "defer" in scripts[script], f"{script} is not deferred"

    reliquary = (ROOT / "reliquary.js").read_text(encoding="utf-8")
    for element_id in (
        "vf-slider",
        "fl-reveal",
        "fl-next",
        "fl-canvas-a",
        "fl-canvas-b",
    ):
        assert element_id in reliquary, (
            f"{element_id} is not wired into reliquary.js"
        )
    for description, behavior in INTERACTIVE_BEHAVIORS:
        assert re.search(behavior, reliquary), (
            f"missing {description}"
        )

    print("Site regression checks passed.")


if __name__ == "__main__":
    main()

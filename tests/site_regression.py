"""Dependency-free regression checks for the interactive site surface."""

from html.parser import HTMLParser
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_LIVE_REGIONS = 2  # one status region for each interactive demo


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
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
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
        attrs for tag, attrs in parser.elements
        if attrs.get("aria-live") == "polite"
    ]
    assert len(live_regions) >= EXPECTED_LIVE_REGIONS, (
        "interactive status regions are missing"
    )

    pick_values = {
        attrs["data-pick"]
        for tag, attrs in parser.elements
        if tag == "button" and "data-pick" in attrs
    }
    assert pick_values == {"A", "B"}, "Flatlander must provide A and B choices"

    scripts = {
        attrs.get("src"): attrs
        for tag, attrs in parser.elements
        if tag == "script"
    }
    for script in ("throne.js", "reliquary.js"):
        assert script in scripts, f"{script} is not referenced"
        assert "defer" in scripts[script], f"{script} is not deferred"

    reliquary = (ROOT / "reliquary.js").read_text(encoding="utf-8")
    for behavior in (
        r"""btnReveal\.addEventListener\(\s*["']click["']\s*,\s*reveal\s*\)""",
        r"""btnNext\.addEventListener\(\s*["']click["']\s*,\s*newRound\s*\)""",
        r"""slider\.addEventListener\(\s*["']input["']\s*,\s*render\s*\)""",
        r"""btnReveal\.setAttribute\(\s*["']aria-pressed["']\s*,\s*["']true["']\s*\)""",
    ):
        assert re.search(behavior, reliquary), (
            f"missing interactive behavior: {behavior}"
        )

    print("Site regression checks passed.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Copy the confref ontology (confref-ontology/confref-ontology.md, the source) to content/ontology.md.

The headings move up one level (the title comes from the front matter); every term heading gets an anchor: the
local name for terms of confref (#Event, #inSeries), prefix-localname for other vocabularies (#schema-location).
id.confref.org links the terms to these anchors. A list of the terms by section comes after the introduction.

    python3 deploy/sync-ontology.py [path to confref-ontology]     (default: ../confref-ontology)
"""
import re
import subprocess
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
REPO = Path(sys.argv[1]) if len(sys.argv) > 1 else SITE.parent / "confref-ontology"
GITHUB = "https://github.com/confref/confref-ontology"
TERM = re.compile(r"^#### ([a-z]+):(\w+)\s*$")


def anchor(prefix, name):
    return name if prefix == "cr" else f"{prefix}-{name}"


def main():
    lines = (REPO / "confref-ontology.md").read_text(encoding="utf-8").splitlines()
    commit = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"], capture_output=True,
                            text=True, check=True).stdout.strip()
    body, sections, block = [], [], False
    for line in lines[1:]:                          # the first line is the title
        if line.startswith("```"):
            block = not block
        elif not block and (m := TERM.match(line)):
            prefix, name = m.groups()
            line = f"### {prefix}:{name} {{#{anchor(prefix, name)}}}"
            if sections:
                sections[-1][1].append((f"{prefix}:{name}", anchor(prefix, name)))
        elif not block and line.startswith("### "):
            sections.append((line[4:].strip(), []))
            line = "## " + line[4:]
        body.append(line)
    text = "\n".join(body)
    text = re.sub(r"This document is the source; the Turtle file\s+\[confref-ontology\.ttl\]\(confref-ontology\.ttl\) is"
                  r"\s+generated from its code blocks \(`python3 generate\.py`\)\.",
                  f"The Turtle file [confref-ontology.ttl]({GITHUB}/blob/main/confref-ontology.ttl) is generated from the"
                  " code blocks of this document.", text)
    text = re.sub(r" The rendered document is\s+\[www\.confref\.org/ontology/\]\([^)]*\)\.", "", text)
    terms = "\n".join(f"- **{title}:** " + " · ".join(f"[`{t}`](#{a})" for t, a in items)
                      for title, items in sections if items)
    # the list of terms goes before the first section heading
    first = text.index("\n## ")
    text = text[:first] + "\n\n## Terms\n\n" + terms + "\n" + text[first:]
    front = f'''---
title: "Ontology"
eyebrow: "Classes and properties"
lead: "The terms of the confref data: the classes and properties of confref, and how confref uses the terms of other vocabularies."
---

<!-- Copied from confref-ontology.md of {GITHUB} at {commit} by deploy/sync-ontology.py; edit it there. -->

The source of this page is the repository [confref-ontology]({GITHUB}). The ontology is also the dataset
[confref-ontology](../datasets/confref-ontology/); the namespace `https://id.confref.org/ontology/` gives this page to
a browser and the Turtle file to a linked data client.
'''
    (SITE / "content" / "ontology.md").write_text(front + text.rstrip() + "\n", encoding="utf-8")
    print(f"content/ontology.md from confref-ontology {commit}: "
          f"{sum(len(i) for _, i in sections)} terms in {len(sections)} sections")


if __name__ == "__main__":
    main()

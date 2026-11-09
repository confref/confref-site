---
title: "Identifiers"
eyebrow: "First identifier set: 9 November 2026"
lead: "Each conference series and each edition receives a confref identifier with a check character."
---

Conferences have no common identifier comparable to the ISSN of journals. Acronyms are ambiguous (there are many
*ICCC*s) and change over time; publishers, libraries and registries use their own keys. confref assigns each series
and each edition one identifier and links it to the identifiers of the other sources.

## Structure

<p><span class="idchip"><b>s</b>10aje<i>w</i></span> is a series (ISWC), <span class="idchip"><b>e</b>10k0h<i>m</i></span>
an edition (an event: ISWC 2023).</p>

- **The first letter** says what it identifies: `s` for a series, `e` for an event.
- **The number** is written in base 32 with the letters and digits that cannot be mistaken for each other (no `i`,
  `l`, `o` or `u`).
- **The last character** is a check character: a mistyped character or two swapped neighbours are recognised.

As IRIs: [`https://id.confref.org/series/s10ajew`](https://id.confref.org/series/s10ajew) and
[`https://id.confref.org/event/e10k0hm`](https://id.confref.org/event/e10k0hm). A browser receives
an HTML page (the landing page), a linked data client RDF in the format it asks for (Turtle, N-Triples, JSON-LD or
RDF/XML), each by a 303 redirect to the document in that format. The platform at `id.confref.org` is in beta. The
identifiers with their records and facts are in the dataset [ids](../datasets/ids/): 11,089 series and 78,280 events.

## Rules

- **No reuse:** if two identifiers turn out to denote the same conference, the older one remains and the other
  refers to it. If one identifier turns out to cover two conferences, both receive new identifiers and the old one
  refers to them.
- **Aliases:** acronyms such as `eswc2016`, the IRIs of lod.springer.com and lod.confref.org (2018) and the pages of
  portal.confref.org lead to the confref identifier.
- **Links to other identifiers:** the DataCite DOIs of ConfIDent, dblp, Wikidata and the GND; DOIs and ISBNs of the
  proceedings; ROR for organisers.

## Maintenance

- **Kept by a program:** the identifiers are assigned and kept by the generator of the dataset ids alone. Each new
  version is made from the current versions of the sources and keeps every identifier of the previous version;
  merges, splits and retirements are recorded with their dates. No identifier is assigned or changed by hand, so
  keeping them takes little effort.
- **Independent of this site:** every version of [ids](../datasets/ids/) holds the full information of the
  identifiers: the records of the sources behind each identifier, its history, its facts and the conflicts between
  the sources. Should confref become unavailable, the latest version of ids (CC0) is all that is needed to resolve
  the identifiers or to continue them.

## IRI scheme

All IRIs that confref coins are below `https://id.confref.org/`. The first path segment says what an IRI stands for;
these segments are reserved:

| Path | What |
|---|---|
| `series/<id>` | a conference, workshop or symposium series; resolves to its landing page or its data |
| `event/<id>` | one event: a conference, workshop, symposium, joint or federated event |
| `event/<id>/edition/<series id>` | the edition number of an event in one of its series, when it belongs to several |
| `datasets/<slug>`, `datasets/<slug>/<version>` | a dataset (one named graph) and its versions |
| `dumps/<slug>/<version>/<file>` | a file of a version |
| `data/<namespace>/…` | a record that confref coins for a source without IRIs of its own |
| `ontology/` | the [confref ontology](../ontology/) (prefix `cr:`) |

Records of the sources keep the IRIs of the sources (dblp, Wikidata, GND, DOIs, lod.springer.com). A dataset has no
path of its own at the top level: its IRI, its files and its records are found under `datasets/`, `dumps/` and
`data/`.

## Series and events

- **A series** is a sequence of recurring events under one name. A workshop series is a series of its own.
- **An event** belongs to one or more series: a joint conference that is branded and run as one event belongs to the
  series of each partner.
- **An event can be held at a larger event:** a workshop at its main conference, the partner conferences of a joint
  conference that presents as a collection of conferences, a conference at a federated event. The series of an event
  is independent of the series of its host.
- **Separate events can be joint or co-located:** held together with joint organisation or programme, or at the same
  place and time with programmes of their own.
- **The way of the source is kept.** The same joint conference can appear in one source as one event in two series
  and in another as two joint events; the links show how they are connected.
- **Proceedings** are not events; they are linked to the events whose contributions they publish.

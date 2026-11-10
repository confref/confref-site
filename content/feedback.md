---
title: "Feedback"
eyebrow: "Errors and corrections"
lead: "How to report an error in the confref data, and how to correct it in its source."
---

confref takes its records from several sources and links them: records of the same series or event are joined under
one identifier. An error can lie in this linking or in a record of a source.

## Issues on confref

Feedback of any kind goes to the public issue tracker of confref-data on GitHub:
[new issue](https://github.com/confref/confref-data/issues/new?template=feedback.yml). It is most useful for errors
of confref itself, in the linking and the grouping of records into series and events:

- records of different conferences joined under one identifier, or one conference under two identifiers;
- an event in the wrong series, or a workshop counted as an edition of its main conference.

Examples help to find the rule behind an error. On the pages of [labs.confref.org](https://labs.confref.org/), the
Feedback button prepares an issue with the page and the selected text. Without a GitHub account, the prepared text can
be copied and sent to the contact in the [legal notice](../legal/).

## Corrections in the sources

An error in a record of a source is best also corrected in that source, so that it is right there as well. confref
takes the correction with its next harvest of the source. Each record on a landing page names its source.

- **ConfIDent:** events and series can be added and updated through
  [ANNOUNCE](https://www.confident-conference.org/index.php/ANNOUNCE); editing needs an
  [account](https://www.confident-conference.org/index.php/Special:RequestAccount); questions in the
  [FAQ](https://www.confident-conference.org/index.php/Help:FAQ).
- **Wikidata:** anyone can edit the items of conferences and series on [wikidata.org](https://www.wikidata.org/);
  each item has a discussion page.
- **dblp:** errors are reported to the dblp team, as described in the FAQ
  [How can I correct errors in dblp?](https://dblp.org/faq/How+can+I+correct+errors+in+dblp.html)
- **GND:** errors in records of the Integrated Authority File are reported to the GND office of the German National
  Library (gnd-info@dnb.de).
- **Springer LOD (2015, 2018), the confref portal (2020):** these sources are no longer kept. Their errors are reported as issues on confref and corrected there.

## New conferences

confref does not create series or events of its own; they come from its sources. A conference that is missing is
added to [ConfIDent](https://www.confident-conference.org/index.php/ANNOUNCE), which also gives it a DOI, and reaches
confref with the next harvest.

## The ontology

Questions about the terms of the [ontology](../ontology/) and proposals for new ones:
[issues of confref-ontology](https://github.com/confref/confref-ontology/issues).

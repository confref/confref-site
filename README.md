# confref-site

The website of confref (https://confref.org): what confref is, its history, the dataset catalogue, news. Hugo, no
theme, no JavaScript, everything served from the site itself (fonts included: Manrope, SIL OFL, `static/fonts/`).

| Path | What |
|---|---|
| `layouts/` | templates: `baseof.html`, `home.html`, `page.html`, `section.html`, `datasets/` (catalogue), `_partials/` |
| `assets/css/main.css` | the one stylesheet, mobile first; colours of the mark as tokens, light and dark |
| `static/img/confref-mark.svg` | the "cr" mark of portal.confref.org (2019), redrawn as SVG without masks |
| `content/` | the pages; `content/datasets/<slug>.md` are copies of the catalogue entries |
| `data/numbers.toml` | the figures of the start page (by hand for now) |
| `data/dataindex.json`, `data/catalogvocabulary.json` | copied from confref-data |

## Working on it

```sh
hugo server                      # preview at http://localhost:1313
hugo --gc --minify               # build into public/
```

The dataset pages are copies of `confref-data/catalog/<slug>.md`: change them there, then
`cd ../confref-data && ./cr sync-site ../confref-site` (with `--add <slug>` for a new entry). Until the dumps locations
exist, `sync-site` gets a test index (`--index`); the dataset pages say that downloads open with the first
publication.

## Notes

- Hugo warns that `kind` in front matter is deprecated (a field of the catalogue format); it still reaches
  the templates as `.Params.kind`. If a future Hugo drops it, `sync-site` has to rename the field for the site.
- Deployed by hand to www.confref.org on bart with `deploy/deploy.sh` (build, rsync); `confref.org` redirects to
  `www.confref.org`; nginx config in `deploy/nginx-confref.conf` (decision 0015 of confref-data). A commit deploys nothing.

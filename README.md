# Jordan Angelov · Insurance Advisor website

Static bilingual landing page hosted on GitHub Pages.

| URL path | Language | File |
|---|---|---|
| `/` | Greek (default) | `index.html` |
| `/en/` | English | `en/index.html` |

## Editing

`index.html` and `en/index.html` are **generated**. Do not edit them directly.

- Design, layout and English text: `_build/source.html`
- Greek text: the `EL` list in `_build/build.py`

Then rebuild:

```
python _build/build.py
```

The build stops with an error if an English sentence in `source.html` changed but its Greek
translation in `build.py` still refers to the old wording. Update both together.

## Local preview

```
python -m http.server 8080
```

Open http://127.0.0.1:8080/. Use the server rather than opening the files directly, because the
language links (`en/` and `../`) need it.

## Going live with a custom domain

1. Set `SITE_URL` at the top of `_build/build.py`, e.g. `SITE_URL = "https://www.example.com"`.
2. Run `python _build/build.py`. This adds `CNAME`, `robots.txt`, `sitemap.xml`, canonical and
   language (hreflang) tags, and social-sharing previews.
3. Commit and push.
4. GitHub → repo **Settings → Pages**: Source "Deploy from a branch", branch `main`, folder `/ (root)`.
   Enter the custom domain, wait for the DNS check, then tick **Enforce HTTPS**.
5. DNS at the domain registrar:
   - `www` → `CNAME` record pointing to `bokisangelov.github.io`
   - apex domain (`example.com`) → `A` records `185.199.108.153`, `185.199.109.153`,
     `185.199.110.153`, `185.199.111.153`
6. Optional: verify the domain under GitHub **Settings → Pages → Verified domains** (account level)
   to stop anyone else using it on GitHub Pages.

Note: GitHub Pages on a **private** repository needs a paid GitHub plan (Pro, Team or Enterprise).
On a free plan the repository must be made public before Pages can be enabled.

## Before launch

- Add licence/registration details and any required regulatory disclosures to the footer
  (currently commented out in `_build/source.html`).

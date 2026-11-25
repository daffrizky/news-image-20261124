# news-image-20261124 — make.fun entry (program form)

Bounty: "Sum up 24 November's world news in one image" ($100, 50 places paid,
ends Thu 26 Nov 2026 07:00 WIB). https://make.fun/bounty/news-image-20261124

The bounty does NOT accept a direct image upload. An entry is a program in a
public GitHub repo (main.py at root, OSI license, one commit) plus the build
transcript bundle plus a wallet signature.

- `main.py` — deterministic, no network: writes the embedded 1024x1024 JPEG
  (262,641 bytes) to /output/entry.png. Same bytes on every run.
- `entry.jpg` — the finished image (v1): THE WORLD IN ONE PICTURE,
  Tuesday 24 November 2026 — Huawei verdict, Hormuz tankers, Cartagena
  hostages, Riyadh tower, Ukraine naval strikes, Senegal AFCON title.
- `LICENSE` — MIT.

STILL MISSING before submit: public GitHub repo under Daffa's own GitHub
account (created after 24 Nov 07:00) + full commit SHA, transcript bundle
(`node cli/makefun.mjs bundle` / makefun-run.json), wallet signature in browser.

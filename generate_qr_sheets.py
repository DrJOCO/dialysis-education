#!/usr/bin/env python3
"""Regenerate printable QR posters for Premier Nephrology patient education."""
from __future__ import annotations

from html import escape
from pathlib import Path

import segno

ROOT = Path(__file__).parent
BASE_URL = "https://drjoco.github.io/dialysis-education/"

POSTERS = [
    {
        "title_en": "Protect Your Kidneys",
        "title_es": "Proteja Sus Riñones",
        "team": "General kidney care",
        "tag": "Kidney number, urine protein, BP, medicines, food, genetic testing · Número del riñón, proteína en orina, presión, medicinas, comida, pruebas genéticas",
        "path": "premier-ckd-basics.html",
    },
    {
        "title_en": "Low Kidney Function: Plan Early",
        "title_es": "Función Baja del Riñón: Planee Temprano",
        "team": "Kidney choices planning",
        "tag": "Transplant, home dialysis, center dialysis, and access planning · Trasplante, diálisis en casa, diálisis en centro, y acceso",
        "path": "premier-advanced-ckd.html",
    },
    {
        "title_en": "Korean Review Draft",
        "title_es": "한국어 신장 교육 검토용",
        "team": "Review before patient use",
        "tag": "Standalone Korean draft · 한국어 검토용 초안",
        "path": "premier-korean-review.html",
        "scan_ko": "휴대폰 카메라로 스캔하세요",
    },
    {
        "title_en": "Premier Nephrology Group",
        "title_es": "Grupo Premier Nephrology",
        "team": "Physicians + Yecenia Cueva, FNP-BC",
        "tag": "Learn how to protect your kidneys · Aprenda a proteger sus riñones",
        "path": "premier-group.html",
    },
    {
        "title_en": "Premier Nephrology Office",
        "title_es": "Oficina de Premier Nephrology",
        "team": "Jonathan Cheng, MD, MPH",
        "tag": "Learn how to protect your kidneys · Aprenda a proteger sus riñones",
        "path": "premier-office.html",
    },
    {
        "title_en": "DaVita Hollywood",
        "title_es": "DaVita Hollywood",
        "team": "Dr. Cheng + Yecenia Cueva, FNP-BC",
        "tag": "Learn about your dialysis, pills, and food · Aprenda sobre su diálisis, sus pastillas y su comida",
        "path": "davita-hollywood.html",
    },
    {
        "title_en": "DaVita Wilshire - Team Yecenia",
        "title_es": "DaVita Wilshire - Equipo Yecenia",
        "team": "Dr. Cheng + Yecenia Cueva, FNP-BC",
        "tag": "Learn about your dialysis, pills, and food · Aprenda sobre su diálisis, sus pastillas y su comida",
        "path": "davita-wilshire-yecenia.html",
    },
    {
        "title_en": "DaVita Wilshire - Team Benjamin",
        "title_es": "DaVita Wilshire - Equipo Benjamin",
        "team": "Dr. Cheng + Benjamin Chow, PA-C",
        "tag": "Learn about your dialysis, pills, and food · Aprenda sobre su diálisis, sus pastillas y su comida",
        "path": "davita-wilshire-benjamin.html",
    },
    {
        "title_en": "DaVita Avalon - Team Sonya",
        "title_es": "DaVita Avalon - Equipo Sonya",
        "team": "Dr. Cheng + Sonya Ambriz, FNP",
        "tag": "Learn about your dialysis, pills, and food · Aprenda sobre su diálisis, sus pastillas y su comida",
        "path": "davita-avalon-sonya.html",
    },
    {
        "title_en": "DaVita Avalon - Team Gloria",
        "title_es": "DaVita Avalon - Equipo Gloria",
        "team": "Dr. Cheng + Gloria Parra, FNP",
        "tag": "Learn about your dialysis, pills, and food · Aprenda sobre su diálisis, sus pastillas y su comida",
        "path": "davita-avalon-gloria.html",
    },
]


STYLE = """<style>
  :root{
    --blue:#166C71;
    --muted:#5d6b7b;
    --line:#d9e2ef;
  }
  *{box-sizing:border-box}
  body{margin:0;font-family:Verdana, Geneva, Tahoma, sans-serif;color:#243142;background:#f5f7fb}
  .no-print{
    max-width:8.5in;margin:0 auto;padding:14px 16px;background:#fff4e5;border:1px solid #e8d4ae;
    border-radius:12px;margin-top:14px;font-size:15px
  }
  .no-print strong{color:var(--blue)}
  .sheet{
    width:8.5in;min-height:10.4in;margin:14px auto;background:#fff;border:1px solid var(--line);
    padding:0.7in 0.8in 0.5in;text-align:center;page-break-after:always;break-after:page;
  }
  .brand{margin:0;font-size:14px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--blue)}
  h1{margin:10px 0 0;font-size:34px;line-height:1.15;color:var(--blue)}
  h2{margin:4px 0 0;font-size:22px;line-height:1.2;font-weight:400;color:var(--muted)}
  .team{margin:6px 0 0;font-size:17px;color:#243142}
  .qr{width:4.6in;height:4.6in;margin:0.28in auto 0}
  .qr svg{width:100%;height:100%;display:block}
  .scan-en{margin:0.22in 0 0;font-size:26px;font-weight:700;color:#243142}
  .scan-es{margin:4px 0 0;font-size:22px;font-weight:700;color:var(--blue)}
  .steps{list-style:none;margin:0.22in auto 0;padding:0;max-width:6.4in;text-align:left}
  .steps li{display:flex;align-items:center;gap:10px;font-size:15px;margin-top:8px}
  .steps li span{
    flex-shrink:0;width:26px;height:26px;border-radius:50%;background:var(--blue);color:#fff;
    display:inline-flex;align-items:center;justify-content:center;font-weight:700;font-size:14px
  }
  .tag{margin:0.2in 0 0;font-size:15px;color:var(--muted)}
  .url{margin:6px 0 0;font-size:12px;color:var(--muted);word-break:break-all}
  @media print{
    body{background:#fff}
    .no-print{display:none}
    .sheet{margin:0 auto;border:none}
  }
  @page{size:letter;margin:0.35in}
</style>"""


def qr_svg(url: str) -> str:
    return segno.make(url, error="m").svg_inline(scale=1)


def render_poster(poster: dict[str, str]) -> str:
    url = BASE_URL + poster["path"]
    scan_ko = ""
    if poster.get("scan_ko"):
        scan_ko = f'\n    <p class="scan-es">{escape(poster["scan_ko"])}</p>'
    return f"""  <section class="sheet">
    <p class="brand">Premier Nephrology Medical Group</p>
    <h1>{escape(poster["title_en"])}</h1>
    <h2>{escape(poster["title_es"])}</h2>
    <p class="team">{escape(poster["team"])}</p>
    <div class="qr">{qr_svg(url)}
</div>
    <p class="scan-en">Scan me with your phone camera</p>
    <p class="scan-es">Escanee con la cámara de su teléfono</p>{scan_ko}
    <ol class="steps">
      <li><span>1</span> Open your phone camera · Abra la cámara de su teléfono</li>
      <li><span>2</span> Point it at this code · Apunte al código</li>
      <li><span>3</span> Tap the link that appears · Toque el enlace que aparece</li>
    </ol>
    <p class="tag">{escape(poster["tag"])}</p>
    <p class="url">{escape(url)}</p>
  </section>"""


def main() -> None:
    posters = "\n".join(render_poster(poster) for poster in POSTERS)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Printable QR Posters | Premier Nephrology Patient Education</title>
{STYLE}
</head>
<body>
<div class="no-print">
  <strong>Staff instructions:</strong> Print this file (File -> Print). It makes {len(POSTERS)} posters, one per page -
  the new QR 1 and QR 2 office pages first, the Korean review draft, then the original office pages and each dialysis unit.
  Post each QR poster at the matching clinic, at chairs, check-in, and the lobby. Patients scan with their phone camera; no app needed.
</div>
{posters}
</body>
</html>
"""
    (ROOT / "qr-sheets.html").write_text(html, encoding="utf-8")
    print(f"wrote qr-sheets.html with {len(POSTERS)} posters")


if __name__ == "__main__":
    main()

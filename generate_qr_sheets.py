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
        "title_ko": "콩팥을 보호하세요",
        "team_en": "For patients learning about kidney disease",
        "team_es": "Para pacientes que están aprendiendo sobre la enfermedad renal",
        "team_ko": "콩팥병에 대해 배우는 환자를 위한 안내",
        "tag": "Kidney number, urine protein, blood pressure, medicines, and food · Número del riñón, proteína en orina, presión, medicinas y comida",
        "tag_ko": "GFR, 소변 단백질, 혈압, 약과 음식",
        "scan_ko": "진료 후 다시 보려면 QR 코드를 스캔하세요",
        "path": "premier-ckd-basics.html",
    },
    {
        "title_en": "Low Kidney Function: Plan Early",
        "title_es": "Función Baja del Riñón: Planee Temprano",
        "title_ko": "콩팥 기능이 낮다면: 미리 준비하세요",
        "team_en": "For patients planning ahead for very low kidney function",
        "team_es": "Para pacientes que necesitan planear por función renal muy baja",
        "team_ko": "콩팥 기능이 많이 낮아 미리 준비하는 환자를 위한 안내",
        "tag": "Transplant, home dialysis, center dialysis, and planning early · Trasplante, diálisis en casa, diálisis en un centro y planificación temprana",
        "tag_ko": "콩팥이식, 재택투석, 센터투석과 미리 준비하기",
        "scan_ko": "진료 후 다시 보려면 QR 코드를 스캔하세요",
        "path": "premier-advanced-ckd.html",
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
    padding:0.5in 0.72in 0.38in;text-align:center;page-break-after:always;break-after:page;
  }
  .brand{margin:0;font-size:14px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--blue)}
  h1{margin:8px 0 0;font-size:32px;line-height:1.15;color:var(--blue)}
  h2{margin:3px 0 0;font-size:20px;line-height:1.2;font-weight:400;color:var(--muted)}
  .title-ko{margin:3px 0 0;font-size:20px;line-height:1.25;color:#243142}
  .team{margin:3px 0 0;font-size:14px;color:#243142}
  .team-ko{margin:2px 0 0;font-size:14px;color:#243142}
  .qr{width:4.15in;height:4.15in;margin:0.18in auto 0}
  .qr svg{width:100%;height:100%;display:block}
  .scan-en{margin:0.14in 0 0;font-size:23px;font-weight:700;color:#243142}
  .scan-es{margin:2px 0 0;font-size:19px;font-weight:700;color:var(--blue)}
  .scan-ko{margin:2px 0 0;font-size:18px;font-weight:700;color:#243142}
  .steps{list-style:none;margin:0.12in auto 0;padding:0;max-width:6.4in;text-align:left}
  .steps li{display:flex;align-items:center;gap:8px;font-size:13px;margin-top:5px}
  .steps li span{
    flex-shrink:0;width:26px;height:26px;border-radius:50%;background:var(--blue);color:#fff;
    display:inline-flex;align-items:center;justify-content:center;font-weight:700;font-size:14px
  }
  .tag{margin:0.1in 0 0;font-size:13px;color:var(--muted)}
  .tag-ko{margin:2px 0 0;font-size:13px;color:var(--muted)}
  .url{margin:4px 0 0;font-size:11px;color:var(--muted);word-break:break-all}
  @media print{
    body{background:#fff}
    .no-print{display:none}
    .sheet{width:7.8in;min-height:10.3in;margin:0 auto;border:none}
    .sheet:last-of-type{page-break-after:auto;break-after:auto}
  }
  @page{size:letter;margin:0.35in}
</style>"""


def qr_svg(url: str) -> str:
    return segno.make(url, error="m").svg_inline(
        svgclass="segno",
        lineclass="qrline",
        omitsize=True,
    )


def render_poster(poster: dict[str, str]) -> str:
    url = BASE_URL + poster["path"]
    scan_ko = f'\n    <p class="scan-ko">{escape(poster["scan_ko"])}</p>'
    return f"""  <section class="sheet">
    <p class="brand">Premier Nephrology Medical Group</p>
    <h1>{escape(poster["title_en"])}</h1>
    <h2>{escape(poster["title_es"])}</h2>
    <h3 class="title-ko">{escape(poster["title_ko"])}</h3>
    <p class="team">{escape(poster["team_en"])} · {escape(poster["team_es"])}</p>
    <p class="team-ko">{escape(poster["team_ko"])}</p>
    <div class="qr">{qr_svg(url)}
</div>
    <p class="scan-en">Scan to review after your visit</p>
    <p class="scan-es">Escanee para repasar después de su cita</p>{scan_ko}
    <ol class="steps">
      <li><span>1</span> Open your phone camera · Abra la cámara de su teléfono</li>
      <li><span>2</span> Point it at this code · Apunte al código</li>
      <li><span>3</span> Tap the link that appears · Toque el enlace que aparece</li>
    </ol>
    <p class="tag">{escape(poster["tag"])}</p>
    <p class="tag-ko">{escape(poster["tag_ko"])}</p>
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
  <strong>End-of-visit instructions:</strong> Print both pages. Give or show the first QR to patients learning about kidney disease.
  Use the second QR for patients with very low kidney function who need to learn about transplant and dialysis planning.
  Patients scan with their phone camera and review the guide at home; no app is needed. Each destination supports English, Spanish, and Korean.
</div>
{posters}
</body>
</html>
"""
    (ROOT / "qr-sheets.html").write_text(html, encoding="utf-8")
    print(f"wrote qr-sheets.html with {len(POSTERS)} posters")


if __name__ == "__main__":
    main()

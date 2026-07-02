#!/usr/bin/env python3
"""Regenerate the 5 DaVita unit pages from templates/dialysis-unit.html.

To change shared content (sections, wording, EN/ES text), edit the template,
then run:  python3 generate_units.py
To change a team, phone number, or address, edit UNITS below and rerun.
"""
from pathlib import Path

ROOT = Path(__file__).parent
TEMPLATE = ROOT / "templates" / "dialysis-unit.html"

PHOTOS = "https://www.premiernephrologyla.com/wp-content/uploads/"

YECENIA = {
    "APP_NAME": "Yecenia Cueva, FNP-BC",
    "APP_PHOTO": PHOTOS + "Yecenia-Cueva.jpg",
    "APP_INITIALS": "YC",
    "APP_ROLE_EN": "Your Nurse Practitioner",
    "APP_ROLE_ES": "Su Enfermera Practicante",
}
BENJAMIN = {
    "APP_NAME": "Benjamin Chow, PA-C",
    "APP_PHOTO": PHOTOS + "Benjamin-Chow.jpg",
    "APP_INITIALS": "BC",
    "APP_ROLE_EN": "Your Physician Assistant",
    "APP_ROLE_ES": "Su Asistente Médico",
}
SONYA = {
    "APP_NAME": "Sonya Ambriz, FNP",
    "APP_PHOTO": PHOTOS + "Sonya-Ambriz-300x300.jpg",
    "APP_INITIALS": "SA",
    "APP_ROLE_EN": "Your Nurse Practitioner",
    "APP_ROLE_ES": "Su Enfermera Practicante",
}
GLORIA = {
    "APP_NAME": "Gloria Parra, FNP",
    "APP_PHOTO": PHOTOS + "gloria-parra-300x300.jpg",
    "APP_INITIALS": "GP",
    "APP_ROLE_EN": "Your Nurse Practitioner",
    "APP_ROLE_ES": "Su Enfermera Practicante",
}

HOLLYWOOD = {
    "UNIT_NAME": "DaVita Hollywood",
    "UNIT_TEL": "+13239134010",
    "UNIT_CONTACT": "5065 Hollywood Blvd, Los Angeles, CA 90027 · (323) 913-4010",
}
WILSHIRE = {
    "UNIT_NAME": "DaVita Wilshire",
    "UNIT_TEL": "+12134825181",
    "UNIT_CONTACT": "1127 Wilshire Blvd Suite 120, Los Angeles, CA 90017 · (213) 482-5181",
}
AVALON = {
    "UNIT_NAME": "DaVita Avalon",
    "UNIT_TEL": "+13232332452",
    "UNIT_CONTACT": "5807 Avalon Blvd, Los Angeles, CA 90011 · (323) 233-2452",
}

UNITS = {
    "davita-hollywood.html": {**HOLLYWOOD, **YECENIA},
    "davita-wilshire-yecenia.html": {**WILSHIRE, **YECENIA},
    "davita-wilshire-benjamin.html": {**WILSHIRE, **BENJAMIN},
    "davita-avalon-sonya.html": {**AVALON, **SONYA},
    "davita-avalon-gloria.html": {**AVALON, **GLORIA},
}


def main():
    template = TEMPLATE.read_text(encoding="utf-8")
    for filename, data in UNITS.items():
        page = template
        for key, value in data.items():
            page = page.replace("{{" + key + "}}", value)
        assert "{{" not in page, f"{filename}: unfilled placeholder"
        (ROOT / filename).write_text(page, encoding="utf-8")
        print(f"wrote {filename}")


if __name__ == "__main__":
    main()

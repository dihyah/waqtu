"""
Adhina is a web app that serves as a personal assistance 
for muslims around the world. At its core function, the app 
allows users to be aware and ahead of their daily prayer times.
Copyright (C) 2020 Dihyah Al Hii

Adhina is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

Adhina is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Adhina.  If not, see <https://www.gnu.org/licenses/>.

Contact Me:
    You may reach me at hiidihyah@gmail.com if you have any inquiries.
"""

import os
import requests
import urllib.parse

from datetime import datetime, date

def lookup(position):
    """Look up prayer times for current location."""

    #contact API
    try:
        response = requests.get("https://api.aladhan.com/timingsByAddress/"+(date.today().strftime('%d-%m-%y%y'))+"?address="+(urllib.parse.quote_plus(position))+"&method=3")
        response.raise_for_status()
    except requests.RequestException:
        return None

    #Parse response
    try:
        quote = response.json()
        return {
                "date": quote["data"]["date"]["readable"],
                "zone": quote["data"]["meta"]["timezone"],
                "fajr": quote["data"]["timings"]["Fajr"],
                "sunrise": quote["data"]["timings"]["Sunrise"],
                "dhuhr": quote["data"]["timings"]["Dhuhr"],
                "asr": quote["data"]["timings"]["Asr"],
                "maghrib": quote["data"]["timings"]["Maghrib"],
                "isha": quote["data"]["timings"]["Isha"],
        }
    except (KeyError, TypeError, ValueError):
        return None



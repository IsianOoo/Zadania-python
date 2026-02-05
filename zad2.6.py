import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def read_float(txt):
    if txt is None:
        return None
    t = txt.strip().replace(",", ".")
    if t in ("", "-", "brak", "None"):
        return None
    try:
        return float(t)
    except:
        return None

if __name__ == "__main__":
    print("2.6 test:")
    url = "https://danepubliczne.imgw.pl/api/data/meteo/format/xml"

    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        root = ET.fromstring(r.text)
    except Exception as e:
        print("ERROR:", e)
        raise SystemExit

    wind_data = []
    temp_data = []

    for s in root.findall("stacja"):
        name = (s.findtext("nazwa_stacji") or "").strip()
        wind = read_float(s.findtext("predkosc_wiatru"))
        temp = read_float(s.findtext("temperatura"))
        if name and wind is not None:
            wind_data.append((name, wind))
        if name and temp is not None:
            temp_data.append((name, temp))

    if wind_data:
        chosen = wind_data[:8]
        names = [x[0] for x in chosen]
        values = [x[1] for x in chosen]
        avg = sum(values) / len(values)

        print("wykres: predkosc_wiatru")
        print("wybrane stacje:", ", ".join(names))
        print("średnia prędkość wiatru:", avg)

        plt.bar(names, values)
        plt.axhline(avg)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
        raise SystemExit

    if temp_data:
        chosen = temp_data[:8]
        names = [x[0] for x in chosen]
        values = [x[1] for x in chosen]
        avg = sum(values) / len(values)

        print("brak wiatru w danych -> wykres: temperatura")
        print("wybrane stacje:", ", ".join(names))
        print("średnia temperatura:", avg)

        plt.bar(names, values)
        plt.axhline(avg)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
        raise SystemExit

    print("Brak danych o wietrze i temperaturze")

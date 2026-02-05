import threading
import requests

def fetch(country, out):
    url = f"http://universities.hipolabs.com/search?country={country}"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()[:20]
        out[country] = [u.get("name", "") for u in data]
    except Exception as e:
        out[country] = f"ERROR: {e}"

if __name__ == "__main__":
    print("2.3 test:")
    countries = ["Poland", "Germany", "France"]
    results = {}
    threads = []

    for c in countries:
        t = threading.Thread(target=fetch, args=(c, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    for c in countries:
        print(f"\n{c}:")
        res = results.get(c)
        if isinstance(res, str):
            print(res)
        else:
            for name in res:
                print(name)

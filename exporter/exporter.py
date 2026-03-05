from flask import Flask, Response
import json

app = Flask(__name__)

def read_results():
    try:
        with open("/data/result.json") as f:
            data = json.load(f)

            fail = 0
            passed = 0

            for item in data.get("Controls", []):
                for test in item.get("tests", []):
                    for result in test.get("results", []):
                        if result.get("status") == "FAIL":
                            fail += 1
                        if result.get("status") == "PASS":
                            passed += 1

            return passed, fail
    except:
        return 0, 0


@app.route("/metrics")
def metrics():
    p, f = read_results()

    metrics = f"""
kube_bench_pass {p}
kube_bench_fail {f}
"""

    return Response(metrics, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

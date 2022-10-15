from flask import Flask
from flask import jsonify, make_response
from flask import request, Response

app = Flask(__name__)

DATA = dict()


@app.route('/hello/')
def hello():
    if request.method == "GET":
        return Response("HSE OneLove!", headers={"Content-Type": "text/plain"}, status=200)
    return Response(status=405)


@app.route('/set/', methods=['POST'])
def set_value():
    if request.method == "POST":
        if request.headers.get("Content-Type", None) != "application/json":
            return Response(status=415)
        dt = request.get_json()
        if "key" not in dt.keys() or "value" not in dt.keys():
            return Response(status=400)
        DATA[dt.get("key", "this key is empty")] = dt.get("value", "this key is empty")
        return Response(status=200)
    return Response(status=405)


@app.route('/get/<key>/', methods=["GET"])
def get(key):
    if request.method == "GET":
        if key not in DATA.keys():
            return Response(status=404)
        if key not in DATA.keys():
            return Response(status=400)
        response = make_response(jsonify({"key": key, "value": DATA[key]}), 200)
        response.headers['Content-Type'] = 'text/plain'
        return response
    return Response(status=405)


@app.route('/devide/', methods=["POST"])
def divide():
    if request.method == "POST":
        if request.headers.get("Content-Type", None) != "application/json":
            return Response(status=415)
        dt = request.get_json()
        try:
            result = str(dt["dividend"] / dt["divider"])
            return Response(result, headers={"Content-Type": "text/plain"}, status=200)
        except Exception:
            return Response(status=400)


@app.route('/<default>/')
def something_else(default):
    return Response(status=405)


@app.route('/')
def index():
    return Response(status=405)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)

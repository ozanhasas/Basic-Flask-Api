from flask import Flask, jsonify, request
name = {"firstname": "Arif Ozan", "lastname": "Hasas"}
temperature = [{"city": "istanbul", "temperature": 8.82}, {"city": "izmir", "temperature": 35.35}]
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config["DEBUG"] = True


@app.route('/')
def api_main():
    return jsonify(name)


@app.route("/temperature", methods=['GET'])
def api_temperature():
    args = request.args
    city = args.get('city')
    for i in temperature:
        if i['city'] == city:
            output = i['temperature']
    return jsonify({'temperature': output})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
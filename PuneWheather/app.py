from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained ML model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    wind_speed = float(request.form["wind_speed"])

    # Send input to ML model
    prediction = model.predict([
        [temperature, humidity, wind_speed]
    ])

    if prediction[0] == 1:
        result = "RAIN"
        emoji = "🌧️"
    else:
        result = "SUNNY"
        emoji = "☀️"

    return render_template(
        "index.html",
        result=result,
        emoji=emoji
    )


if __name__ == "__main__":
    app.run(debug=True)

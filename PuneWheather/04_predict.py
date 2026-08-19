import pickle


# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


print("Pune Rain Prediction")
print("--------------------")


# Get new weather information

temperature = float(
    input("Temperature: ")
)

humidity = float(
    input("Humidity: ")
)

wind_speed = float(
    input("Wind Speed: ")
)


# Create new input
new_weather = [[
    temperature,
    humidity,
    wind_speed
]]


# Predict
prediction = model.predict(new_weather)


# Display result
if prediction[0] == 1:
    print("\n🌧 Prediction: RAIN")
else:
    print("\n☀ Prediction: NO RAIN")

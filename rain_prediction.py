import pandas as pd

# Load dataset
data = pd.read_csv("weather.csv")

# Display first few rows
print("Dataset Preview:")
print(data.head())

# Calculate probability of rain
total_days = len(data)
rain_days = len(data[data['Rain'] == 'Yes'])

probability_of_rain = rain_days / total_days
print("\nProbability of Rain:", probability_of_rain)

# Conditional probability (Humidity > 65)
high_humidity = data[data['Humidity'] > 65]
rain_high_humidity = high_humidity[high_humidity['Rain'] == 'Yes']

if len(high_humidity) > 0:
    conditional_prob = len(rain_high_humidity) / len(high_humidity)
    print("Probability of Rain when Humidity > 65:", conditional_prob)

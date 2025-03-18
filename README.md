# j4f---weather-board
# Weather Dashboard
A simple Python application that fetches real-time weather data for a given city using the OpenWeatherMap API and displays it in a user-friendly graphical interface. Built using Python, Tkinter for the GUI, and the requests library to handle API requests.

# Features
Real-time weather data: Displays temperature, humidity, and weather description of a given city.
User-friendly interface: Easy-to-use GUI built with Tkinter.
City-based search: Users can input any city to view its weather details.
Requirements
Python 3.x
requests library (for API calls)
Tkinter (comes pre-installed with Python)
Setup Instructions

# 1. Install Python
Make sure you have Python 3.x installed. You can download it from python.org.

# 2. Install Required Libraries
To install the requests library, run the following command in your terminal or command prompt:
bash: pip install requests

# 3. Get an API Key from OpenWeatherMap
Go to OpenWeatherMap.
Sign up for an account and generate an API key.
Replace the placeholder YOUR_API_KEY in the code with your actual API key.

# 4. Running the Program
Clone or download this repository to your local machine.
Open the project folder in your terminal or command prompt.
Run the following command to start the program:
bash: python weather_dashboard.py
Enter the name of any city in the input box and click "Search" to view the weather details.

# Example Usage
Enter "London" in the input box.
Click "Search".
The program will display the temperature, humidity, and weather description for London.

# Code Explanation
get_weather(city): This function sends a request to the OpenWeatherMap API, retrieves the weather data, and returns the information in a dictionary format.
show_weather(): This function is triggered when the user clicks the "Search" button. It retrieves the weather data for the city entered by the user and updates the displayed labels.
GUI with Tkinter: The program uses Tkinter to create the graphical interface. It includes an entry widget for inputting the city, labels to display weather information, and a button to trigger the weather search.

# Troubleshooting
Invalid city name: If the city name is not found or invalid, an error message will be displayed.
API key issues: If you see an error related to the API key, make sure you have entered a valid key.

# License
This project is open-source and available under the MIT License.

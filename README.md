
# Smart Weather Info App Using Python
The weather application utilizes the Tkinter library to create a simple graphical user interface (GUI) for users to retrieve weather information for a selected city. 
The algorithm of the program is as follows:

 1.Import necessary modules: The program imports the Tkinter library to create the GUI, requests module to make HTTP requests to the OpenWeatherMap API, and ttk from Tkinter to create a styled combo box.

2.Define data_get function: This function is called when the user clicks the "Get" button. It retrieves the selected city name from the combo box, constructs the API URL with the city name and API key, and makes a GET request to the OpenWeatherMap API. The response is then converted to JSON format, and the relevant weather information such as weather main, description, temperature, and pressure is extracted from the JSON response. This information is then displayed in the GUI

3.Create the main window (win): The main window is created with the title "Weather" and a light blue background. The window size is set to 500x580 pixels.

4.Create GUI elements: -name_label: Label prompting the user to enter the city name. -city_name: StringVar to store the city name entered by the user. -com: Combobox to select the city from the list of predefined cities. -w_label, wb_label, temp_label, per_label: Labels to display weather information such as weather climate, weather description, temperature, and pressure. -w_label1, wb_label1, temp_label1, per_label1: Labels to display the weather data fetched from the API.

5.Define data_get function: -Get the city name entered by the user. -Construct the API URL with the city name and API key. -Make a GET request to the API and retrieve the weather data. -Extract relevant weather information like weather main, description, temperature, and pressure from the JSON response. -Display this information on the GUI. -If the city name is invalid or the data is not available, it displays "Wrong City" in the GUI.

6.Run the application: Start the Tkinter event loop using win.mainloop().

Overall, the program provides a user-friendly interface for users to quickly access weather information for a selected city. It simplifies the process of fetching weather data by utilizing the OpenWeatherMap API and presenting the data in a clear and concise manner on the GUI.
## Installation

Install my-project with npm

```bash
 pip install tkinter
```
    
## Roadmap
1.Import Required Modules:
 - Import the necessary modules (tkinter, ttk, requests).

2.Define the data_get() Function:
- Define the data_get() function to fetch weather data from the OpenWeatherMap API based on the city selected by the user.
- Make an API request to OpenWeatherMap API using the requests.get() method.
- Convert the response to JSON format using the .json() method.
- Extract weather data from the JSON response and update the labels accordingly.
- Handle exceptions in case of incorrect city name or API failure.

3.Create the Main Window:
- Create the main Tk() window and set its properties (title, size, background color).

4.Create Widgets:
 - Create and place the following widgets on the main window:
- Labels:
   - Title label ("Enter The City Name").
   - Labels for displaying weather information ("Weather Climate",       "Weather Description", "Temperature", "Pressure").
- Combobox:
  - A Combobox to select the city.
- Button:
  - A "Get" button to fetch weather data.
## Screenshots




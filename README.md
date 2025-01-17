# Weather

Input and Output Process Explanation
This image illustrates a chatbot's input-output process for fetching and displaying the temperature of a city. Here's how it works:

Input Process
User Initiation:
The user begins with /start, which is a predefined command to initialize the chatbot. This triggers the bot to display its purpose and instructions.
Bot's Response: A greeting and a request for input:
"Send me a city name, and I'll provide the current temperature."
User Input:
The user enters text. The bot processes this input to determine if it's a valid city name:
If the input is not a valid city name (e.g., "hello"), the bot replies:
"Sorry, I could not find that city."
If the input is valid (e.g., "Vijayawada"), the bot proceeds to fetch weather information for the city.
Output Process
Valid Input:
For valid inputs (e.g., "Vijayawada"), the bot fetches the temperature data using an external weather API or database.
The bot then constructs an output message with the city's name and the current temperature, e.g.:
"The current temperature in Vijayawada is 30.97°C."
Process Flow Summary
User Command (/start): Activates the bot's instructions.
User Input: The user provides a city name or other text.
Validation:
If input matches a valid city, the bot fetches temperature data.
Otherwise, it returns an error message.
Data Fetching (for valid input): The bot interacts with a weather API to get the current temperature.
Response Construction: The bot formats the data into a user-friendly message.
Bot Output: The message is displayed in the chat.



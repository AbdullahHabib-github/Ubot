# Ubot

## Project Purpose
Ubot is a chatbot project that utilizes Langchain to create a versatile chatbot. The chatbot can be adapted to work with any dataset provided. In this specific implementation, Ubot is designed to serve as an API for the official website of Ghulam Ishaq Khan Institute. Data is scraped from the website to enable the chatbot to answer queries based on the provided data.

## Installation and Setup
To install and set up the project, follow these steps:
Clone the repository.
create a text file named as `hugging_face_token.txt` and ad your hugging face token
Install the required dependencies by running:
pip install -r requirements.txt
To run the UI-based chatbot, use the following command:
<code>uvicorn app:app --reload</code>
Alternatively, to run the API, use the following command:
<code>uvicorn api:app --reload</code>

Please note that if you intend to run the project on your dataset, you need to run `dataset_extractor.py`. Make sure to replace the URL with the URL of the website from which you want to extract data.

## Usage
Once the project is set up, you can use the chatbot for answering queries based on the provided data. The UI-based chatbot can be accessed through the provided API, and you can interact with it by sending messages through the user interface.

## Main Features
Utilizes Langchain to create a versatile chatbot.
Can be adapted to work with different datasets.
Provides answers to user queries based on the provided data.
Known Issues and Limitations
Currently, Ubot uses the Flan model by Google. While functional, it could be improved by using paid APIs like OpenAI.

## Contributing
Feel free to contribute to the project or use it for your own purposes.

## Changelog
There are no release notes or changelogs available at the moment.

## Support
For any questions or support, you can reach me out at my LinkedIn profile: [ LinkedIn - Abdullah Habib](https://www.linkedin.com/in/mr-abdullahhabib/).

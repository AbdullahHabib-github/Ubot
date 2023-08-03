# Ubot

## Project Purpose
Ubot is a chatbot project that utilizes Langchain to create a versatile chatbot. The chatbot can be adapted to work with any dataset provided. In this specific implementation, Ubot is designed to serve as an API for the official website of Ghulam Ishaq Khan Institute. Data is scraped from the website to enable the chatbot to answer queries based on the provided data.

## Installation and Setup
To install and set up the project, follow these steps:
* Clone the repository.
* Create a Token at [Hugging Face APi Token](https://huggingface.co/settings/tokens).
* Create a text file named as `hugging_face_token.txt` and add (only) your hugging face token.
* Install the required dependencies by running:
   `pip install -r requirements.txt`
   
### To run the UI-based chatbot, use either of the following commands:
for Conversational retrieval chain
<code>uvicorn app:app --reload</code>  

a UI based app that could be accessed by only a single user at  time and it would remember their chat history
<code>uvicorn app:app --reload</code>  

a UI based app the could be accessed by multiple users at  time and it would remember their individual chat histories
<code>uvicorn Multi_user_app:app --reload</code>


### Alternatively, to run the API for Conversational retrieval chain, use the following command:
<code>uvicorn api:app --reload</code>


## If you intend to use your own dataset if not, skip this step
* Please note that if you intend to run the project on your dataset, you need to run `dataset_extractor.py`. Make sure to replace the URL with the URL of the website from which you want to extract data.
* `data_cleaner.py` was designed specifially for my own dataset, you can clean the data the way you want.
* The cleaner your data is, the more accurate your results would be.
* Run the `database_creater.py`
* Hurrah!! now you have a database wit your own dataset.

## LLM
I used "google/flan-t5-small" as the LLM, if you want to change your LLM, just replace the value of `MODEL_ID` in the `Model.py`.
## Usage
Once the project is set up, you can use the chatbot for answering queries based on the provided data. You can interact with it by sending messages either through the user interface or through the api.

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


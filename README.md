# Ubot

## Project Purpose
Ubot is a chatbot project that utilizes Langchain to create a versatile chatbot. The chatbot can be adapted to work with any dataset provided. In this specific implementation, Ubot is designed to serve as an API for the official website of Ghulam Ishaq Khan Institute. Data is scraped from the website to enable the chatbot to answer queries based on the provided data.

## Installation and Setup
To install and set up the project, follow these steps:
* Clone the repository.
* Create a folder names "Api_keys" in the main directory.
* Create a Token at [Hugging Face APi Token](https://huggingface.co/settings/tokens).
* Create a text file named as `hugging_face_token.txt` and add (only) your hugging face token.
* Move `hugging_face_token.txt` to the "Api
-keys" folder.
* Install the required dependencies by running:
   `pip install -r requirements.txt`
   
### To run the UI-based chatbot, use either of the following commands in cmd:

* A UI based app that could be accessed by only a single user at  time and it would remember the context of the discussion and would use Conversational retrieval chain.
<code>uvicorn single_user_api:app --reload</code>


* a UI based app the could be accessed by multiple users at  time and it would remember their individual chat histories and use Retrival QA chain.
<code>uvicorn Multi_user_api:app --reload</code>


### Alternatively, to run the API for Conversational retrieval chain, use the following steps:
* Open either `Multi_user_api.py` or `single_user_api.py` and follow the comments mentioned in the script.
* Run the above mentioned commands to run the APIs.
* (OPTIONAL) Clone the React front-end provided at [Ubot_React_frontend](https://github.com/AbdullahHabib-github/Ubot_React_frontend) and follow the steps in that reposistory.

## If you intend to use your own dataset if not, skip this step
* Please note that if you intend to run the project on your dataset, you need to run `dataset_extractor.py`. Make sure to replace the URL with the URL of the website from which you want to extract data.
* `data_cleaner.py` was designed specifially for my own dataset, you can clean the data the way you want.
* The cleaner your data is, the more accurate your results would be.
* Run the `database_creater.py`
* Hurrah!! now you have a database wit your own dataset.

## LLM
Currenlty, using this repository you can access LLMs in 3 different ways. For more clear understanding refer to `fetch_llm.py`.
* Hugging_face Models
* Replicate Models
* LLama by Meta.

To use either for these three models just import their respective modules from `fetch_llm.py`.
## Usage
Once the project is set up, you can use the chatbot for answering queries based on the provided data. You can interact with it by sending messages either through the user interface or through the api.

## Main Features
Utilizes Langchain to create a versatile chatbot.
Can be adapted to work with different datasets.
Provides answers to user queries based on the provided data.
Known Issues and Limitations
Personally, I used free trials for Ubot. While functional, it could be improved by using paid APIs like OpenAI.

## Contributing
Feel free to contribute to the project or use it for your own purposes.

## Changelog
There are no release notes or changelogs available at the moment.

## Support
For any questions or support, you can reach me out at my LinkedIn profile: [ LinkedIn - Abdullah Habib](https://www.linkedin.com/in/mr-abdullahhabib/).


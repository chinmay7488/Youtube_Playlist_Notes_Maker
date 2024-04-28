import google.generativeai as genai
from dotenv import load_dotenv
import os

class GeminiHelper:

    __prompt =  """Please continue taking notes in the established format. Remember to:
                1. Create concise, easy-to-understand advanced bullet-point notes.
                2. Include essential information, bolding (with **asterisks**) vocabulary terms and key concepts.
                3. Remove extraneous language, focusing on critical aspects.
                4. Base your notes strictly on the provided passages.
                5. Conclude with [#X] to indicate Start of new topic, where "X" represents the Topic name.
                Your notes will help me better understand the material and prepare for the topic. 
                We will continue with our current topic. 
                For youtube link:"""

    def __init__(self):
        load_dotenv()
        genai.configure(api_key=os.getenv('gemini_api_key'))
        # Set up the model
        self.generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
        }
        self.safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        ]
        self.model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=self.generation_config,
                              safety_settings=self.safety_settings)

    def getNote(self, youtubeLink):
        self.convo = self.model.generate_content("{} {}".format(self.__prompt,youtubeLink))
        print(self.convo.text)


gemini = GeminiHelper()
gemini.getNote('https://www.youtube.com/watch?v=MGu7zKi5azQ')

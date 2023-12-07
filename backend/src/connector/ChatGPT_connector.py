import openai

class ChatGPTConnector:
    def __init__(self):
        self.starting_prompt = {"role": "system", "content": "You are a helpful assistant."}
        self.conversation=[self.starting_prompt]
        openai.api_key_path ="./src/connector/secrets/API.txt"
        pass

    def _call_api(self, conversation):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        response_text = response.choices[0].message.content
        return response_text

    def _mock_api(self, conversation):
        ##add response logic here
        response=""
        return response

    def prompt_conversation(self, text):
        new_message = {"role": "user", "content": text}
        self.conversation.append(new_message)
        response_text = self._call_api(self.conversation)
        self.conversation.append({"role": "assistant", "content": response_text})
        return response_text

    def prompt(self, text):
        new_message = {"role": "user", "content": text}
        self.conversation.append(new_message)
        response_text = self._call_api([new_message])
        self.conversation.append({"role": "assistant", "content": response_text})
        return response_text

#PLEASE RUN THIS TO INSTALL cerebras_cloud_sdk
#  pip install cerebras_cloud_sdk
import requests
import json
from cerebras.cloud.sdk import Cerebras
import re
import urllib.parse


class Cerebras_with_Cookie:
    def __init__(self,cookie_path, model = 'llama3.1-8b'):
        self.client = Cerebras(
              api_key=self.get_demo_api_key(cookie_path),
          )
        self.model = model
    def extract_query(self, text: str) -> str:
        pattern = r"```(.*?)```"
        matches = re.findall(pattern, text, re.DOTALL)
        return matches[0] if matches else text

    def refiner(self, text):
        if text.startswith('"'):
            text = text[1:]
        if text.endswith('"'):
            text = text[:-1]
        return text

    def get_demo_api_key(self,cookie_path):
        cookies = {i['name']: i['value'] for i in json.loads(open(cookie_path,'r').read())}
        headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://inference.cerebras.ai',
                'priority': 'u=1, i',
                'referer': 'https://inference.cerebras.ai/',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
            }
        json_data = {
                'operationName': 'GetMyDemoApiKey',
                'variables': {},
                'query': 'query GetMyDemoApiKey {\n  GetMyDemoApiKey\n}',
            }
        response = requests.post('https://inference.cerebras.ai/api/graphql', cookies=cookies, headers=headers, json=json_data)
        print("Your Demo API Key:",response.json()['data']['GetMyDemoApiKey'])
        try:
            return response.json()['data']['GetMyDemoApiKey']
        except:
            print(response.text)

    def ask(self, question, sys="You Are A Helpful Assistant. Try to Help the User According to the Provided Instructions.", json_response=False):
        if json_response:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        'content': sys,
                        'role': 'system',
                    },
                    {
                        'content': question,
                        'role': 'user',
                    },
                ],
                model=self.model,
                response_format={"type": "json_object"}
            )
            return self.extract_query(chat_completion.choices[0].message.content)
        else:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        'content': sys,
                        'role': 'system',
                    },
                    {
                        'content': question,
                        'role': 'user',
                    },
                ],
                model=self.model,
            )
            return self.extract_query(chat_completion.choices[0].message.content)

# Unofficial Cerebras.ai API

This is an unofficial API for [Cerebras.ai](https://www.cerebras.net/), designed for users currently on the waitlist for an official API key. The limits and quotas are similar to those provided with an official key, ensuring consistency and a seamless transition once access to the official API is granted.

## Prerequisites

1. Install the required SDK by running the following command:

   ```bash
   pip install cerebras_cloud_sdk
   ```

2. Install the **"Cookie-Editor"** extension for either Chrome or Edge:
   - [Chrome Extension](https://chrome.google.com/webstore/detail/cookieeditor/neaplmfkghagebokkhpjpoebhdledlfi).
   - [Edge Extension](https://microsoftedge.microsoft.com/addons/detail/cookieeditor/neaplmfkghagebokkhpjpoebhdledlfi).

   Once installed, follow these steps to export your cookies:
   - Open the website from which you want to extract cookies.
   - Click on the **Cookie-Editor** extension icon.
   - Click the **"Export"** button to save your cookies in JSON format.
   - Create a file in your working directory named `cookies.json`.
   - Paste the data copied from the Cookie-Editor into `cookies.json` and save it.

## Quota and Usage Limits

The following limits apply for different models when using this API:

### Llama 3.1-8B Model (default):
- **Requests:**
  - Per minute: 30
  - Per hour: 900
  - Per day: 14,400
- **Tokens:**
  - Per minute: 60,000
  - Per hour: 1,000,000
  - Per day: 1,000,000

### Llama 3.1-70B Model:
- **Requests:**
  - Per minute: 30
  - Per hour: 900
  - Per day: 14,400
- **Tokens:**
  - Per minute: 60,000
  - Per hour: 1,000,000
  - Per day: 1,000,000

## Example

By default, the API uses the **Llama 3.1-8B** model. You can also switch to other models like **Llama 3.1-70B** if required.

```python
from cerebras_cloud_sdk import Cerebras_with_Cookie

# Using the Llama 3.1-70B model
llm_client = Cerebras_with_Cookie(cookie_path='/your/path/to/cookies.json', model='llama3.1-70b')
response = llm_client.ask("Tell me a story of a boy and a dog")
print(response)
```

In the above example, make sure to replace `'/your/path/to/cookies.json'` with the actual path to your `cookies.json` file. If no model is provided, **Llama 3.1-8B** will be used by default.

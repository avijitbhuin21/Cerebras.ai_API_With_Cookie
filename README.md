# Unofficial Cerebras.ai API

This is an unofficial API for [Cerebras.ai](https://www.cerebras.net/), designed for users currently on the waitlist for an official API key. The limits and quotas are similar to those provided with an official key, ensuring consistency and a seamless transition once access to the official API is granted.

## Prerequisites

Before using the API, ensure you have installed the required SDK. You can install the `cerebras_cloud_sdk` by running the following command:

```bash
pip install cerebras_cloud_sdk
```

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
llm_client = Cerebras_with_Cookie(cookie_path='cookies.json', model='llama3.1-70b')
response = llm_client.ask("Tell me a story of a boy and a dog")
print(response)
```

In the above example, the Llama 3.1-70B model is explicitly specified. If no model is provided, **Llama 3.1-8B** will be used by default.

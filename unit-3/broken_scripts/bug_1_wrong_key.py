import json

# Simulated response from an API
response_data = '{"choices": [{"message": {"role": "assistant", "content": "AI is the future."}}]}'

data = json.loads(response_data)
# BUG: Accessing content directly from choices[0] instead of choices[0]['message']
try:
    content = data['choices'][0]['content']
    print("AI Content:", content)
except KeyError as e:
    print("CRASHED due to wrong key:", e)

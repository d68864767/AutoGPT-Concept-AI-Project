```python
# Import necessary libraries
from flask import Flask, request, jsonify
import json
from model_development import model, tokenizer, TASKS

# AutoGPT Concept AI Project - System Integration

app = Flask(__name__)

# Function to process the input and return the model's output
def process_input(input_text, task):
    # Tokenize the input text
    input_tokens = tokenizer.encode(input_text, return_tensors='pt')

    # Generate the output tokens
    output_tokens = model.generate(input_tokens)

    # Decode the output tokens to text
    output_text = tokenizer.decode(output_tokens[0])

    return output_text

# Define the API endpoint
@app.route('/api/autogpt', methods=['POST'])
def autogpt():
    # Get the input data from the request
    data = request.get_json()

    # Get the input text and task from the data
    input_text = data.get('input_text')
    task = data.get('task')

    # Check if the task is valid
    if task not in TASKS:
        return jsonify({'error': 'Invalid task'}), 400

    # Process the input and get the output
    output_text = process_input(input_text, task)

    # Return the output as a JSON response
    return jsonify({'output_text': output_text})

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

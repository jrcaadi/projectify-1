from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Routes
@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/todo')
def serve_todo():
    return render_template('todo.html')

@app.route('/index')
def serve_index2():
    return render_template('index.html')

@app.route('/problem')
def serve_index3():
    return render_template('problem.html')

# Initialize OpenAI API Key
openai.api_key = "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"

@app.route('/problem_solver_chat', methods=['POST'])
def problem_solver_chat():
    print("Received request at /problem_solver_chat")  # Debugging statement
    data = request.json
    prompt = data.get('message', '')
    user_id = data.get('user_id', 'unknown')
    print(f"User ID: {user_id}, Prompt: {prompt}")  # Debugging statement

    if not prompt:
        return jsonify({'response': 'No prompt provided'}), 400

    response_text = get_response(prompt)
    return jsonify({'response': response_text})


def get_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Make sure this is the correct model
            messages=[
                {"role": "system", "content": "You are a helpful problem-solving assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error in OpenAI request: {e}")  # Debugging statement
        return "Sorry, something went wrong."

if __name__ == "__main__":
    app.run(debug=True)

# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # This block only runs when app.py is executed directly
    # (e.g., python app.py), NOT when imported by pytest.
    # What's inside this block?
    print("--- Flask app script is running inside Jenkins! ---") # <-- This is from your log!
    print("Python version:", sys.version) # <-- This is from your log!
    print("Current working directory in Jenkins:", os.getcwd()) # <-- This is from your log!
    print("requirements.txt found!") # <-- This is from your log!

    # IS THERE AN app.run() here?
    # IS THERE A print() statement that outputs the problematic string?
    # For example:
    # print("This should not be hit by Jenkins build job.")
    # Or app.run() might be commented out or misconfigured.
    
    # You might have something like this, which should NOT be in app.py IF your test is importing it:
    # @app.route('/')
    # def some_other_function():
    #    return 'This should not be hit by Jenkins build job.'

    # Check for any direct `print` statements that might be returning this string.
    # It's most likely in the `if __name__ == '__main__':` block or a custom error handler.

    # Example of what *could* be in your if __name__ == '__main__': block if things are misconfigured:
    # @app.route('/')
    # def bad_route_override():
    #     return 'This should not be hit by Jenkins build job.'
    # app.run(debug=True) # If this is running, it could be overriding the test client.

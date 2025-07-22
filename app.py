from flask import Flask 

app=Flask(__name__)

@app.route('/')
def home():
    return """
    <center><h1> Welcome to My Flask App!</h1><br><br>
    <p><h2>Flask is a micro web framework for Python, used for building web applications. It is classified as a "microframework" because it provides a lightweight core with essential functionalities for web development, such as URL routing and template rendering, but it does not include built-in features like database abstraction layers, form validation, or full-fledged authentication systems. Instead, Flask emphasizes flexibility and allows developers to choose and integrate specific libraries and extensions for these functionalities as needed.</h2></p></center>
    
    """

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def fizzbuzz(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fizzbuzz', methods=['POST'])
def get_fizzbuzz():
    data = request.json
    number = data.get("number")
    
    if number is None or not isinstance(number, int):
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    
    result = fizzbuzz(number)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Home route with calculator form
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        except Exception as e:
            result = f"Error: {e}"

    # Inline HTML template
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Calculator</title>
    </head>
    <body>
        <h2>Simple Calculator</h2>
        <form method="POST">
            <input type="number" step="any" name="num1" placeholder="Enter first number" required>
            <input type="number" step="any" name="num2" placeholder="Enter second number" required>
            <select name="operation">
                <option value="add">Add</option>
                <option value="subtract">Subtract</option>
                <option value="multiply">Multiply</option>
                <option value="divide">Divide</option>
            </select>
            <button type="submit">Calculate</button>
        </form>
        {% if result is not none %}
            <h3>Result: {{ result }}</h3>
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(html, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000))

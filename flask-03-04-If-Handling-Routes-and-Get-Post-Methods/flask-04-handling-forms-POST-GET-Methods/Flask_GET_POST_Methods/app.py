
from flask import Flask, render_template, request

app = Flask(__name__)


def lcm(num1,num2):
    common_multiplications = [] 
    for i in range(max(num1, num2),num1*num2+1):
        if i%num1==0 and i%num2==0:
           common_multiplications.append(i) 
    return min(common_multiplications)



@app.route("/")
def index():
    return render_template("index.html")





@app.route("/calc", methods=["POST"])
def calculate():
    if request.method == "POST":
        print("Start of Request")
        num1 = request.form.get("number1")
        num2 = request.form.get("number2")
        lowest = lcm(int(num1), int(num2))
        return render_template("result.html", result1 = num1, result2 = num2, lcm = lowest, developer_name = 'Amber')
    else:
        return "<h1> Error </h1>"


if __name__== "__main__":
    app.run(port=3000, debug=True)
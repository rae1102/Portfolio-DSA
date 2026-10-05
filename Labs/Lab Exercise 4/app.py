from flask import Flask, render_template, request
from linkedlist import LinkedList


app = Flask(__name__)
linked_list = LinkedList()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works/area/circle', methods=['GET', 'POST'])
def circle():
    result = None
    if request.method == 'POST':
        radius = request.form.get('radius', '')
        result = int(radius)*3.14*int(radius)
    return render_template('circle.html', result=result)

@app.route('/works/area/triangle', methods=['GET', 'POST'])
def triangle():
    result = None
    if request.method == 'POST':
        base = request.form.get('base', '')
        height = request.form.get('height', '')
        result = (int(base) * int(height) / 2)
    return render_template('triangle.html', result=result)

# @app.route('/areaOfcirle', methods=['GET', 'POST'])
# def areaOfcirle():
#     result = None
#     name=request.get('name','')
#     print(name)
#     if request.method == 'POST':
#         input_string = request.form.get('inputradius', '')
#         result = int(input_string) * int(input_string) * 3.14
#     return render_template('areaCircle.html', result=result)

@app.route('/works/linkedlist', methods=["GET", "POST"])
def linkedlist():

    values = linked_list.get_values()
    search_result = None

    if request.method == "POST":

        if 'insert_end' in request.form:
            insert_end = request.form.get('insert_end', '')
            linked_list.insert_at_end(insert_end)

        elif 'insert_beginning' in request.form:
            insert_beginning = request.form.get('insert_beginning', '')
            linked_list.insert_at_beginning(insert_beginning)

        elif 'insert_after_node' in request.form:
            insert_after_node = request.form.get('insert_after_node', '')
            insert_after_value = request.form.get('insert_after_value', '')
            linked_list.insert_after(insert_after_node, insert_after_value)

        elif 'remove_beginning' in request.form:
            linked_list.remove_beginning()

        elif 'remove_end' in request.form:
            linked_list.remove_at_end()

        elif 'remove_value' in request.form:
            remove_value = request.form.get('remove_value', '')
            linked_list.remove_at(remove_value)

        elif 'search_value' in request.form:
            search_value = request.form.get('search_value', '')
            search_result = linked_list.search(search_value)

        values = linked_list.get_values()

    return render_template(
        "linkedlist.html",
        values=values,
        search_result=search_result
    )

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

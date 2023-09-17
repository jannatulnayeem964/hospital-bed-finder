from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for hospitals and bed availability
hospitals = [
    {"name": "Inova Loudoun Hospital", "beds_available": 10},
    {"name": "Inova Fair Oaks Hospital", "beds_available": 10},
    {"name": "Inova Alexandria Hospital", "beds_available": 10},
    {"name": "Inova Fairfax Medical Campus", "beds_available": 10},
    {"name": "Inova Mount Vernon Hospital", "beds_available": 10},
]

@app.route('/')
def index():
    return render_template('index.html', hospitals=hospitals)

@app.route('/transfer', methods=['POST'])
def transfer():
    hospital_name = request.form.get('hospital')
    patient_name = request.form.get('patient')
    beds_needed = int(request.form.get('beds'))

    for hospital in hospitals:
        if hospital['name'] == hospital_name:
            if hospital['beds_available'] >= beds_needed:
                hospital['beds_available'] -= beds_needed
                return redirect(url_for('index'))
            else:
                return "Not enough beds available."

    return "Hospital not found."

if __name__ == '__main__':
    app.run(debug=True)

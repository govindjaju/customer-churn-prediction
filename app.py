from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    # 8 input features from user
    tenure = float(request.form['tenure'])
    MonthlyCharges = float(request.form['MonthlyCharges'])
    TotalCharges = float(request.form['TotalCharges'])
    Contract = int(request.form['Contract'])
    InternetService = int(request.form['InternetService'])
    PaymentMethod = int(request.form['PaymentMethod'])
    TechSupport = int(request.form['TechSupport'])
    OnlineSecurity = int(request.form['OnlineSecurity'])

    # Full 19 features (remaining auto-filled)
    features = [
        tenure, MonthlyCharges, TotalCharges,
        Contract, InternetService, PaymentMethod,
        TechSupport, OnlineSecurity,
        0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1
    ]

    final_input = np.array([features])

    prediction = model.predict(final_input)

    result = "Churn" if prediction[0] == 1 else "No Churn"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
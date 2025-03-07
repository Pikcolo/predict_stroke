from flask import Blueprint, render_template, request
import numpy as np
from predict_stroke.models import load_stroke_model, load_scaler_model

module = Blueprint("site", __name__)

# โหลดโมเดลและ Scaler ภายนอก
model = load_stroke_model()
scaler = load_scaler_model()

# ฟังก์ชันที่รับข้อมูลจากฟอร์มและทำนายผล
def predict_stroke(gender, age, hypertension, heart_disease, avg_glucose_level, bmi, smoking_status):
    # สร้าง array สำหรับข้อมูลที่ผู้ใช้กรอก
    input_data = np.array([[gender, age, hypertension, heart_disease, avg_glucose_level, bmi, smoking_status]])

    # ทำ Standardization ด้วยตัวแปลงที่โหลดมา
    input_data_scaled = scaler.transform(input_data)

    # ทำนายผลจากโมเดลที่โหลด
    prediction = model.predict(input_data_scaled)

    # แปลงการทำนายเป็นเปอร์เซ็นต์
    prediction_percent = prediction * 100
    return prediction_percent[0][0]

# ฟังก์ชัน index ที่คงไว้เหมือนเดิม
@module.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # รับข้อมูลจากฟอร์ม
        gender = int(request.form["gender"])
        age = float(request.form["age"])
        hypertension = int(request.form["hypertension"])
        heart_disease = int(request.form["heart_disease"])
        avg_glucose_level = float(request.form["avg_glucose_level"])
        bmi = float(request.form["bmi"])
        smoking_status = int(request.form["smoking_status"])

        # ทำนายผลจากฟังก์ชัน predict_stroke
        prediction = predict_stroke(gender, age, hypertension, heart_disease, avg_glucose_level, bmi, smoking_status)

        # ส่งผลการทำนายไปที่หน้าเว็บ
        return render_template("site/index.html", prediction=prediction)
    
    return render_template("site/index.html")

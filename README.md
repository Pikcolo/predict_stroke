# Stroke Prediction
เปลี่ยนจากหัวข้อเดิม คือ predict Diagnosis of Diabetic Retinopathy สาเหตุที่เปลี่ยนเนื่องจากมีปัญหาในการเอาโมเดลออกไปใช้ จากข้อผิดพลาดของ GPU

Mini project นี้ใช้โมเดล ANN ในการทำนายโอกาสที่เสี่ยงจะเป็นโรคหลอดเลือดสมอง (Stroke)

# Web Stroke prediction

  ใช้ Dataset จาก [Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data)
  โดยเว็บนี้จะใช้โมเดลในการทำนายโอกาสเสี่ยงที่จะเป็นโรคหลอดเลือดสมองโดยใช้ Feature ดังนี้
    
  - เพศ
  - อายุ
  - ความดันโลหิตสูง
  - การโรคหัวใจ
  - ระดับน้ำตาลเฉลี่ยในเลือด
  - ดัชนีมวลกาย (BMI)
  - การสูบบุหรี่

  เมื่อกรอกข้อมูลเหล่านี้แล้วกดยืนยันโมเดลก็จะทำการทำนายโอกาสเสี่ยงที่จะเป็นโรคหลอดเลือดสมองโดยให้ผลออกมาเป็น percent
  ซึ่งจะใช้ model ANN ในการทำโปรแกรมนี้ และโดยจุดเด่นจะมีการทำ Data Augmentation เองโดยเทียบกับแบบ SMOTE 
  
  Dataset from [Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data)
  This website will use a model to predict the risk of stroke using the following features:

  - Gender
  - Age
  - High blood pressure
  - Heart disease
  - Average blood sugar level
  - Body Mass Index (BMI)
  - Smoking
    
  Once you enter this information and click confirm, the model will predict the risk of stroke and provide the result as a percentage.
  Which will use the ANN model to make this program and the highlight is that it will do Data Augmentation itself by comparing with the SMOTE model.

  ![stroke_webpage](https://github.com/user-attachments/assets/d7e47324-fe76-49c7-a395-44807e936187)

# How to Install & Run Project

1. Clone the repository to your local machine:
   
   ```
   git clone https://github.com/Pikcolo/predict_stroke.git
   ```

2. Install poetry and Install Dependencies using Poetry

   Poetry is used to manage dependencies and virtual environments for this project.
    ```
    pip install poetry
    ```

    After installing Poetry, navigate to the project directory and run:
    ```
    poetry install 
    ```
    
3. Install node.js and npm
   
   **for Windows**
   
   Use wsl and follow the linux steps.
   
   **for Linux**
   
   Open a terminal and run the following command to install Node.js and npm:
   ```
   sudo apt update
   sudo apt install nodejs npm
   ```
   
   **for MacOS**
   
   Use Homebrew to install Node.js and npm:
   ```
   brew install node
   ```
   
   Verify the installation by running:
   ```
   node -v
   npm -v
   ```
   
4. Install Dependencies for Static Files

   Navigate to the `static` folder and install npm packages:
  
   ```
   cd predict_stroke/web/static 
   npm install
   ```

6. Run Web
    ```
    ./scripts/run-web 
    ```



    

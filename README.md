# 🤟 Sign Language Detection with Text-to-Speech

A real-time **Sign Language Detection System** powered by **Computer Vision** and **Deep Learning** that recognizes hand gestures through a webcam, converts them into text, and generates speech using **Text-to-Speech (TTS)** technology. This project aims to improve communication accessibility between sign language users and non-signers.

A major highlight of this project is the creation of a **custom-built sign language dataset**, manually collected, labeled, and preprocessed specifically for training the recognition model.

---

## 📌 Project Overview

This project combines **Computer Vision**, **Machine Learning**, and **Speech Synthesis** to build an end-to-end sign language recognition system.

The application captures hand gestures using a webcam, predicts the corresponding sign using a trained deep learning model, displays the prediction as text, and instantly converts it into speech for seamless communication.

The project demonstrates the complete machine learning workflow—from dataset creation and preprocessing to model training, evaluation, and real-time inference.

---

# ✨ Features

- 🤟 Real-time sign language recognition
- 📷 Live webcam gesture detection
- 🧠 Deep learning-based gesture classification
- 📝 Converts detected gestures into readable text
- 🔊 Text-to-Speech (TTS) output
- 📂 Custom-built and manually labeled dataset
- ⚡ Fast and accurate predictions
- 📊 Complete model training pipeline
- 💻 Simple and intuitive interface
- 🔄 Easily extendable with additional gestures

---

# 🗂️ Custom Dataset

One of the major contributions of this project is the creation of a **custom sign language dataset**.

### Dataset Creation

- Captured gesture images using a webcam
- Collected multiple samples for every gesture
- Included different lighting conditions
- Captured multiple hand orientations and positions
- Manually labeled every image
- Organized images into class-wise folders
- Preprocessed images for consistent model training

> **Note:** The dataset (~3.5 GB) is **not included** in this repository due to GitHub storage limitations.

---

# 🛠️ Technologies Used

- Python
- OpenCV
- TensorFlow / Keras *(or PyTorch if applicable)*
- NumPy
- Pandas
- Matplotlib
- Text-to-Speech (TTS)

---

# 🚀 Project Workflow

```text
Custom Dataset
      ↓
Image Preprocessing
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Real-Time Webcam Detection
      ↓
Gesture Prediction
      ↓
Text Output
      ↓
Speech Output
```

---

# 📂 Project Structure

```text
Sign-Language-Detection/
│── dataset/                 # Ignored from Git
│── models/
│── src/
│── utils/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

# 💻 Installation

## Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Sign-Language-Detection.git
```

## Navigate to the project

```bash
cd Sign-Language-Detection
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
python app.py
```

---

# 🎯 Applications

- Accessibility for deaf and hard-of-hearing individuals
- Educational sign language learning tools
- Human-computer interaction
- AI-based gesture recognition
- Assistive communication systems

---

# 🚀 Future Improvements

- Sentence-level sign language recognition
- Dynamic gesture detection
- Mobile application
- Cloud deployment
- Multi-language speech output
- Transformer-based recognition models
- Improved real-time accuracy

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Patrick**

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

## ⭐ Acknowledgements

This project was developed to explore the applications of **Computer Vision**, **Deep Learning**, and **Text-to-Speech** in improving accessibility. A complete custom dataset was created specifically for this project to demonstrate the end-to-end machine learning workflow.

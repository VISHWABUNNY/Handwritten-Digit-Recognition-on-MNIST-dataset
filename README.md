<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Handwritten Digit Recognition on MNIST Dataset</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h1, h2, h3 {
            margin-top: 40px;
        }
        h2 {
            margin-top: 20px;
        }
        ul {
            margin-top: 10px;
            margin-left: 20px;
        }
        li {
            margin-bottom: 5px;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <h1>Handwritten Digit Recognition on MNIST Dataset</h1>
    
    <h2>Overview</h2>
    <p>This project implements a Convolutional Neural Network (CNN) model for handwritten digit recognition using the MNIST dataset. The model is trained to classify handwritten digits (0-9) based on the pixel values of the images.</p>
    
    <h2>Features</h2>
    <ul>
        <li><strong>Backend (Flask):</strong>
            <ul>
                <li>Predict Endpoint: Exposes a <code>/predict</code> endpoint to receive base64 encoded images of handwritten digits, preprocesses them, and returns the predicted digit.</li>
            </ul>
        </li>
        <li><strong>Frontend (HTML, JavaScript):</strong>
            <ul>
                <li>Canvas Drawing: Allows users to draw handwritten digits on a canvas.</li>
                <li>Prediction: Sends the drawn digit to the backend for prediction and displays the predicted digit on the webpage.</li>
            </ul>
        </li>
    </ul>

    <h2>Dependencies</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Flask</li>
        <li>Keras</li>
        <li>TensorFlow</li>
        <li>Pygame (for drawing interface)</li>
        <li>HTML</li>
        <li>JavaScript</li>
    </ul>

    <h2>Usage</h2>
    <ol>
        <li>Clone the repository.</li>
        <li>Install the dependencies using <code>pip install -r requirements.txt</code>.</li>
        <li>Run <code>app.py</code> to start the Flask backend.</li>
        <li>Run <code>app2.py</code> to start the Pygame drawing interface.</li>
        <li>Open <code>index.html</code> in a web browser to access the frontend.</li>
        <li>Draw a digit on the canvas and click "Predict" to see the predicted digit.</li>
    </ol>

    <h2>Dataset</h2>
    <p>The MNIST dataset is used in this project, containing grayscale images of handwritten digits (0-9) with labels indicating the corresponding digits. Each image is of size 28x28 pixels. The dataset is split into training and testing sets for model training and evaluation.</p>

    <h1>Handwritten Text Recognition using OCR</h1>

    <p><strong>Problem Statement:</strong> Optical Character Recognition (OCR) is a well-established problem in machine learning and artificial intelligence. However, challenges arise when dealing with ambiguous and unregulated handwritten text recognition. This project aims to tackle the challenge of recognizing handwritten text in such scenarios.</p>

    <h2>Tools and Frameworks</h2>
    <ul>
        <li>Jupyter Notebook: For data exploration, model development, and experimentation.</li>
        <li>VS Code: For coding and development tasks.</li>
        <li>OpenCV: For image processing tasks such as preprocessing handwritten text images.</li>
        <li>Python: Programming language for implementing the OCR system.</li>
        <li>Kivy: For building the graphical user interface (GUI) for the OCR system.</li>
        <li>NumPy: For numerical operations and array manipulation.</li>
        <li>Tkinter: For building simple GUI elements or for auxiliary purposes.</li>
    </ul>

    <h2>Proposed Approach</h2>
    <ol>
        <li><strong>Data Collection and Preprocessing:</strong> Collect handwritten text images from various sources and preprocess them to enhance their quality and improve recognition accuracy. This may include tasks such as noise removal, binarization, and resizing.</li>
        <li><strong>Feature Extraction:</strong> Extract relevant features from the preprocessed images to represent the handwritten text effectively. Common feature extraction techniques include histogram of oriented gradients (HOG), scale-invariant feature transform (SIFT), or deep learning-based feature extraction using convolutional neural networks (CNNs).</li>
        <li><strong>Model Development:</strong> Develop and train machine learning or deep learning models for handwritten text recognition. This involves selecting an appropriate model architecture, training it on the extracted features, and fine-tuning hyperparameters to optimize performance.</li>
        <li><strong>Integration with GUI:</strong> Build a user-friendly GUI using Kivy or Tkinter to allow users to interact with the OCR system. The GUI should provide options for uploading handwritten text images, initiating the recognition process, and displaying the recognized text.</li>
        <li><strong>Evaluation and Refinement:</strong> Evaluate the performance of the OCR system using test datasets and real-world handwritten text samples. Refine the system based on feedback and performance metrics, such
    </ol>
</body>
</html>

# Leaf Disease Predictor

This project is a web application that predicts whether a plant leaf is healthy or diseased based on an uploaded image. The application is built using FastAPI for the backend and TensorFlow for the machine learning model.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Description](#file-description)
- [Model Description](#model-description)
- [Example](#example)
- [Contributing](#contributing)

## Requirements

- Python 3.8 or higher
- TensorFlow
- FastAPI
- Uvicorn
- Pillow
- Numpy

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/leaf-disease-predictor.git
    cd leaf-disease-predictor
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `.\venv\Scripts\activate.ps1`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the FastAPI application:**

    ```bash
    uvicorn main:app --reload
    ```

2. **Open your web browser and go to `http://127.0.0.1:8000`.**

3. **Upload an image of a plant leaf to get the prediction.**

## File Description

### `web.py`

This script sets up the FastAPI application and includes the following main components:
- Serving static files from the `static` directory.
- Loading the TensorFlow model for prediction.
- Preprocessing uploaded images.
- Defining routes for the main page and image upload.

### `templates/index.html`

The HTML template for the web application. It includes:
- A form to upload an image.
- CSS for styling.
- Jinja2 templating to display the prediction results.

### `static/image.jpeg`

A placeholder image used as the background for the web application.

### `requirements.txt`

A text file containing all the commands required for installing packages.

## Model Description

The model is a Convolutional Neural Network (CNN) built using TensorFlow and Keras. The model architecture includes:
- Three convolutional layers with max pooling.
- A flatten layer followed by two dense layers.
- The final layer uses softmax activation for binary classification (healthy or diseased).


### Model Architecture

| Layer (type)               | Output Shape           | Param #   |
|----------------------------|------------------------|-----------|
| conv2d (Conv2D)            | (None, 148, 148, 32)   | 896       |
| max_pooling2d (MaxPooling2D)| (None, 74, 74, 32)    | 0         |
| conv2d_1 (Conv2D)          | (None, 72, 72, 64)     | 18,496    |
| max_pooling2d_1 (MaxPooling2D)| (None, 36, 36, 64)  | 0         |
| conv2d_2 (Conv2D)          | (None, 34, 34, 128)    | 73,856    |
| max_pooling2d_2 (MaxPooling2D)| (None, 17, 17, 128) | 0         |
| flatten (Flatten)          | (None, 36,992)         | 0         |
| dense (Dense)              | (None, 512)            | 18,940,416|
| dense_1 (Dense)            | (None, 2)              | 1,026     |

- *Total params*: **19,034,690**
- *Trainable params*: **19,034,690**
- *Non-trainable params*: **0**

## Example

1. **Start the server and open the browser at `http://127.0.0.1:8000`.**
2. **You should see a form to upload an image.**
3. **Upload an image of a plant leaf.**
4. **The application will display whether the plant is healthy or diseased based on the uploaded image.**

## Contributing

Contributions are welcome! Please open an issue or submit a request for any improvements or bug fixes.


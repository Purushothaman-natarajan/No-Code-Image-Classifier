# No-Code Image Classifier

This project provides a no-code interface for developing image classification models using the TensorFlow framework. 
Use the `setup_and_run` script to set up and open the Gradio-based interface, which simplifies the process of developing and testing image classification models.

## Prerequisites

- Python 3.6 or higher

## Getting Started (Demo Video)

<p style="text-align: center;">
  <a href="https://www.youtube.com/watch?v=znRVrnVDgD8" target="_blank">Watch the demo video to see how to use the no-code image classifier interface.</a>
</p>

## Project Structure

- `interface.py`: The Gradio interface script that provides a web interface for data loading, training, testing, and prediction.
- `data_loader.py`: Processes and splits data into training, testing, and validation sets. It also performs data augmentation if enabled by the user.
- `test.py`: Contains functions for evaluating the trained model on test data and generating performance metrics.
- `train.py`: Includes the logic for training the image classification model, including data preprocessing, model training, and saving the trained model.
- `predict.py`: Handles the prediction process, allowing the model to make predictions on new, unseen images.
- `requirements.txt`: Lists all the required Python packages for the project.

### Setup and Run (by code)

1. **Clone the Repository**

   If you haven’t already, clone the repository to your local machine:

   ```sh
   git clone https://github.com/Purushothaman-natarajan/No-Code-Image-Classifier
   cd No-Code-Image-Classifier
   ```
2. **Create a Virtual Environment (Optional but Recommended)**

   It’s a good practice to use a virtual environment to manage your project's dependencies:

   ```sh 
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. **Run the Interface Script**

   Install the dependencies:

   ```sh 
   pip install -r requirements.txt 
   ```
      
   Execute the interface.py script to start the Gradio interface:

   ```sh 
   python interface.py
   ```
   This script will:
   - Check if requirements.txt exists.
   - Install any missing dependencies listed in requirements.txt.
   - Run the interface.py script to start the Gradio interface.

5. **Access the Gradio Interface**

Once the Gradio interface is running, you will see a URL in the terminal. Open this URL in your web browser to access the no-code image classifier interface.

## Using the Gradio Interface
- Data Loader: Upload images and specify settings for data augmentation and splits.
- Training: Configure and start model training with various parameters.
- Testing: Test models with uploaded images or directories of images.
- Prediction: Make predictions on new images using the trained models.

## Troubleshooting
- Dependencies Issues: If you encounter issues with installing dependencies, ensure you have the correct version of Python and try running the run.py script again.
- Script Errors: If you encounter errors while running interface.py, check the script for any missing or misconfigured paths.

## Contributing
- Feel free to fork the repository and submit pull requests. For any issues or feature requests, please open an issue on the GitHub repository.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

# No-Code Image Classifier

This project provides a no-code image classification interface using Gradio, TensorFlow framework for Deep learning. The `run.py` script ensures that all dependencies are installed and then starts the Gradio interface for interacting with the image classification models.

## Project Structure

- `interface.py`: The Gradio interface script that provides a web interface for data loading, training, testing, and prediction.
- `requirements.txt`: Lists all the required Python packages for the project.
- `run.py`: A setup script that installs dependencies from `requirements.txt` and starts the Gradio interface.

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Setup and Run

1. **Clone the Repository**

   If you haven’t already, clone the repository to your local machine:

   ```sh
   git clone (https://github.com/Purushothaman-natarajan/No-Code-Image-Classifier)
   cd No-Code-Image-Classifier
   ```
2. **Create a Virtual Environment (Optional but Recommended)**

   It’s a good practice to use a virtual environment to manage your project's dependencies:

   ```sh 
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. **Run the Setup Script**

   Execute the run.py script to install dependencies and start the Gradio interface:

   ```sh 
   python run.py
   ```


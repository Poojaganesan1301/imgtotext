# imgtotext
![Screenshot 2024-09-27 114638](https://github.com/user-attachments/assets/ad3f0bde-5db9-4678-a673-014cfca977b9)

# Image to Text Annotation using Google Gemini

This is a web application that allows users to upload an image and provide an optional text prompt. The application uses Google's Gemini Generative AI to generate textual annotations based on the input image and user prompt.

## Features

- Upload images in `.jpg`, `.jpeg`, or `.png` formats.
- Provide an optional text prompt to guide the image annotation process.
- Generate text annotations using the **Gemini-1.5-flash** model from Google Generative AI.
- Display the uploaded image and the generated text on the web page.

## Tech Stack

- **Streamlit**: For building the web interface.
- **Google Generative AI (Gemini)**: For generating text annotations based on image input.
- **Pillow (PIL)**: For handling image uploads and displaying them on the page.
- **dotenv**: For managing API keys securely.

## Prerequisites

Before running the project, make sure you have the following:

1. Python 3.x installed on your system.
2. A Google API key with access to the **Gemini Generative AI** service.
3. Environment variables setup for secure API key management.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables:
   - Create a `.env` file in the project directory.
   - Add the following line, replacing `<YOUR-API-KEY>` with your Google API key:
     ```bash
     GOOGLE-API-KEY=<YOUR-API-KEY>
     ```

## How to Run the Project

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. The application will open in your web browser. You can:
   - Upload an image (JPG, JPEG, or PNG).
   - Optionally provide a text prompt.
   - Click the "Submit" button to generate a textual annotation for the image.

## File Structure

- `app.py`: The main Streamlit application file.
- `.env`: Contains environment variables for API keys (not included in version control).
- `requirements.txt`: Lists the dependencies required for the project.

## Dependencies

- `streamlit`: For creating the web app.
- `google-generativeai`: For interacting with Google Gemini's API.
- `Pillow`: For image handling.
- `python-dotenv`: For environment variable management.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Google for providing the Gemini Generative AI service.
- Special thanks to the developers of Streamlit for creating such a powerful and easy-to-use framework.


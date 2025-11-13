#  Wine Quality Prediction MLOps Pipeline

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://prarthana-wine-app.streamlit.app/)
[![CI-Pipeline](https://github.com/PRARTHANA-G/Self_Learning/actions/workflows/ci.yml/badge.svg)](https://github.com/PRARTHANA-G/Self_Learning/actions/workflows/ci.yml)

This project demonstrates a complete, end-to-end Machine Learning Operations (MLOps) pipeline. It takes a machine learning model from an experimental Colab notebook, containerizes it with Docker, sets up automated testing (CI), and deploys it as a live, interactive web application (CD).

##  Live Demo

**[View the live application here](https://prarthana-wine-app.streamlit.app/)**

---

## 🛠️ Tech Stack

* **Model Training:** `scikit-learn`, `pandas`, `Google Colab`
* **Web Application:** `Streamlit`
* **Containerization:** `Docker`
* **CI (Continuous Integration):** `pytest`, `GitHub Actions`
* **CD (Continuous Deployment):** `Streamlit Cloud`

---

##  MLOps Pipeline Architecture

This project is fully automated. The MLOps workflow is as follows:

1.  **Code & Push:** The developer pushes new code (e.g., app fixes, new model) to the `main` branch on GitHub.
2.  **CI (Continuous Integration):** This push automatically triggers a **GitHub Actions** workflow (`.github/workflows/ci.yml`). This workflow:
    * Spins up a clean virtual machine.
    * Installs all project dependencies from `requirements.txt`.
    * Runs automated tests using **`pytest`** to validate the application's code and model loading.
3.  **CD (Continuous Deployment):** If the CI pipeline passes (gets a green check), **Streamlit Cloud** detects the new, verified commit on the `main` branch. It automatically:
    * Pulls the latest code.
    * Builds the application container.
    * Deploys the new version, making it live for all users.
4.  **Monitoring:** The deployed application provides real-time logs via the Streamlit Cloud dashboard for monitoring app usage and errors.

---

##  How to Run Locally

You can run this application on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/PRARTHANA-G/Self_Learning.git](https://github.com/PRARTHANA-G/Self_Learning.git)
cd Self_Learning
```
### 2. Create and Activate Virtual Environment
# For Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4.Run the Streamlit App
```bash
streamlit run app.py
```

##  How to Run with Docker

This application is fully containerized.

### 1. Build the Docker Image
From the root of the project folder (where the `Dockerfile` is):
```bash
docker build -t wine-app
```
### 2. Run the Docker Container
```bash
docker run -p 8501:8501 wine-app
```

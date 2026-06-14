
# 💧 AI Water Tracker

AI Water Tracker is an intelligent hydration monitoring application that helps users track their daily water intake and receive AI-powered hydration insights. The application combines a modern Streamlit dashboard, FastAPI backend, SQLite database, and Large Language Models (LLMs) to provide personalized hydration recommendations.

---

## 🚀 Features

### 💧 Water Intake Tracking

* Log daily water consumption in milliliters (mL)
* Store hydration records in a SQLite database
* Maintain a complete intake history

### 🤖 AI-Powered Hydration Analysis

* Analyze daily water intake using AI
* Estimate hydration goals
* Provide personalized hydration feedback
* Suggest improvements to hydration habits

### 📊 Dashboard

* User-friendly Streamlit interface
* View water intake history
* Monitor hydration progress
* Real-time feedback after logging water intake

### 🌐 REST API

* Built with FastAPI
* Log water intake through API endpoints
* Retrieve user hydration history
* Easily integrate with mobile or web applications

### 🗄️ Database Integration

* SQLite database for lightweight storage
* Automatic table creation
* Persistent hydration records

---

## 🏗️ Project Architecture

```text
AI Water Tracker
│
├── src
│   ├── agent.py
│   ├── api.py
│   ├── database.py
│   ├── logger.py
│   └── __init__.py
│
├── Dashboard.py
├── water_tracker.db
├── .env
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

### Backend

* Python
* FastAPI
* SQLite

### Frontend

* Streamlit

### AI Integration

* LangChain
* OpenRouter
* GPT-4o Mini

### Data Handling

* Pandas

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Water-Tracker.git
cd AI-Water-Tracker
```

### Create Virtual Environment

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
OPENROUTER=your_openrouter_api_key
```

---

## ▶️ Running the Streamlit Dashboard

```bash
streamlit run Dashboard.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## ▶️ Running the FastAPI Server

```bash
uvicorn src.api:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### Home Route

```http
GET /
```

Response:

```json
{
  "message": "Water Tracker API Running 🚰"
}
```

---

### Log Water Intake

```http
POST /log-intake
```

Request:

```json
{
  "user_id": "aditya",
  "intake_ml": 500
}
```

Response:

```json
{
  "message": "Water intake logged successfully",
  "analysis": "AI hydration feedback"
}
```

---

### Get Intake History

```http
GET /history/{user_id}
```

Example:

```http
GET /history/aditya
```

Response:

```json
{
  "user_id": "aditya",
  "history": [
    [1, "aditya", 500, "2025-06-14"]
  ]
}
```

---

## 🤖 AI Hydration Assistant

The AI assistant analyzes user water intake and provides:

* Estimated daily hydration goals
* Current water consumption
* Remaining hydration requirements
* Personalized hydration recommendations
* Healthy hydration habits

Example:

```text
💧 Daily Goal: 3.0 L
✅ Consumed: 1.5 L
🚰 Remaining: 1.5 L

Suggestion:
Drink water regularly throughout the day and keep a bottle nearby.
```

---

## 📈 Future Enhancements

* User authentication
* Daily hydration goals based on weight and activity level
* Weekly and monthly analytics
* Email notifications and reminders
* Mobile application integration
* Cloud database support
* Charts and hydration trends
* Smart hydration alerts

---

## 👨‍💻 Author

**Akshara Badal**

B.Tech Student | Backend Development | AI Enthusiast

---

## 📜 License

This project is open-source and available under the MIT License.


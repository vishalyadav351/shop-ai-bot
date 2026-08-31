# 🛍️ WhatsApp AI Chatbot

An intelligent WhatsApp chatbot powered by Python and AI, seamlessly integrated with Twilio and hosted on Render for 24/7 reliability.

## 🚀 Features
* **Automated Responses**: Instantly replies to user messages on WhatsApp using webhook integration.
* **AI-Powered Logic**: Handles queries intelligently to provide a smooth conversational experience.
* **Cloud Hosted**: Deployed on Render for continuous, uninterrupted uptime.

## 🛠️ Tech Stack
* **Language**: Python
* **Messaging API**: Twilio WhatsApp Sandbox
* **Hosting**: Render
* **Framework / Libraries**: Flask / FastAPI (update as per your project)

---

## ⚙️ Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/vishalyadav351/your-repo-name.git](https://github.com/vishalyadav351/your-repo-name.git)
   cd your-repo-name
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory and add your credentials:

Code snippet
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
Run the application locally:

Bash
python app.py
🌐 Webhook Configuration (Twilio)
To connect your live server to Twilio:

Deploy your app to Render (or use ngrok for local testing).

Go to your Twilio Console > Messaging > Try it out > Send a WhatsApp message > Sandbox settings.

Paste your live webhook URL in the "When a message comes in" field:

Plaintext
[https://your-app-name.onrender.com/webhook](https://your-app-name.onrender.com/webhook)
Set the method to POST and click Save.

👨‍💻 Author
Vishal Yadav



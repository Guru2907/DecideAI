# 🤖 DecideAI: A Conversational AI Admissions Agent (IBM Watson Assistant + Twilio)

**DecideAI** is a smart, WhatsApp-integrated virtual admissions assistant built using **IBM watsonx**. This no-code AI chatbot guides prospective students through academic options and enrollment steps in real-time — all via a simple conversational interface.

* 🚀 **Built and deployed** on IBM Cloud using Watson Assistant
* 💬 **Real-time messaging** on WhatsApp via Twilio API
* 🧠 **No-code conversation flow** with 7 key user-facing actions
* 🦪 **Fully tested** in real-world interaction scenarios

---

## 📌 What This Project Does

* 👋 **Personalized Onboarding** – Greets the user by name for a human-like chat experience
* 📚 **Course Recommendation Engine** – Offers course details (AI, Data Science, Cyber Security)
* 📝 **Enrollment Process Guidance** – Walks users through eligibility checks and info collection
* 🔄 **Multi-turn Dialog Handling** – Manages complex flows and nested user queries
* ❏ **Fallbacks & Error Handling** – Handles unknown questions and can escalate to humans

---

## 🛠️ Built With

* 🧠 **IBM Watson Assistant** – Drag-and-drop Action Skill interface for logic building
* 📲 **Twilio WhatsApp API** – Powers two-way messaging over WhatsApp
* 🐍 **Python** – Twilio integration script for testing and notifications
* 🧾 **JSON** – Core chatbot logic stored in `action-skill.json` for version control

---

## 🔄 Conversational Flow Overview

```plaintext
User Greets → Bot Asks Name → User Requests Courses → Bot Lists Courses →
User Chooses Course → Bot Shares Details → User Chooses to Enroll →
Bot Checks Eligibility → Collects Info → Ends Chat
```

---

## 📁 Project Directory Structure

```plaintext
📁 assets/
├── 🖼️ O1.jpg
├── 🖼️ O2.jpg
├── 🖼️ O3.png
├── 🖼️ O4.jpg

📁 code/
└── 🐍 twilio_integration.py

📁 blueprint/
└── 🧠 action-skill.json

🎥 Demonstration
📜 LICENSE
📜 README.md
```

---

## 🚀 Future Enhancements

* 🔗 CRM Integration
* 🌍 Multi-language Support
* 📊 Analytics Dashboard

---

## 👤 Author

**Gurpreet Singh**
Mini Project | Conversational AI | Watson Assistant | Twilio API | WhatsApp Bots

---

📌 *Built as a cloud-native capstone project using IBM watsonx platform.*

# 🚀 Server Monitoring Dashboard

A real-time server monitoring and basic intrusion detection system built using Flask and psutil.
This project provides live system insights with graphical visualization and alert mechanisms.

---

## 📸 Dashboard Preview

![Dashboard](assets/dashboard.png)

---

## 🔥 Features

* 📊 Real-time CPU & Memory monitoring
* 📈 Live graphs using Chart.js
* 🚨 Alert system for high resource usage
* 🔐 Login authentication system
* ⚡ Fast API-based data updates (no page reload)

---

## 🧠 How It Works

1. System data is collected using `psutil`
2. Flask backend exposes data via `/data` API
3. Frontend fetches data using JavaScript
4. Chart.js renders live graphs

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **System Monitoring:** psutil
* **Frontend:** HTML, CSS, JavaScript
* **Visualization:** Chart.js

---

## ▶️ Installation & Setup

```bash
git clone https://github.com/harshujain1910/server-monitoring-dashboard.git
cd server-monitoring-dashboard
pip install flask psutil
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🔐 Login Credentials

```
Username: admin  
Password: admin  
```

---

## 🚀 Future Enhancements

* 🔍 Suspicious process detection
* 🌐 Network monitoring
* 📁 Log storage & reporting
* 🔔 Email/SMS alerts

---

## 🎯 Learning Outcome

* Built a real-time monitoring system
* Understood client-server architecture
* Worked with REST APIs and live data streaming
* Implemented basic security alerting system

---

## 📌 Author

**Harsh Jain**
GitHub: https://github.com/harshujain1910

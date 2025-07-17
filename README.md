# 📝 Flask Note App with MariaDB on EC2 (RHEL 9) & Mounted Backup Volume

This project is a minimal Flask web application that lets users save and manage notes using a MariaDB backend. It’s designed to run on an AWS EC2 instance with a dedicated EBS volume mounted for MariaDB data backup.

---

## 🔧 Features

- Simple Flask frontend with note submission
- SQLAlchemy integration with MariaDB
- Backup volume `/mariadb` mounted for DB persistence
- Shell script for full environment setup
- Deployed on Amazon EC2 (RHEL 9)

---

## 🗂️ Project Structure

```bash
noteapp/
├── app.py              # Flask app
├── models.py           # SQLAlchemy model
├── templates/
│   └── index.html      # HTML frontend
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

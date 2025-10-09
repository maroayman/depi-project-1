# 📝 Flask Note App with MariaDB on EC2 (Amazon Linux 2023) & Mounted Backup Volume

This project is a minimal Flask web application that lets users save and manage notes using a MariaDB backend. It’s designed to run on an AWS EC2 instance with a dedicated EBS volume mounted for MariaDB data backup.

---

## 🔧 Features

- Simple Flask frontend with note submission
- SQLAlchemy integration with MariaDB
- Backup volume `/mariadb` mounted for DB persistence
- Shell script for full environment setup
- Deployed on Amazon EC2 (Amazon Linux 2023)

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
```

## References

- [Full Guide](https://maroayman.hashnode.dev/deploy-a-flask-mariadb-note-app-on-ec2-amazon-linux-2023-complete-guide)
- [MariaDB-Python](https://mariadb.com/docs/connectors/mariadb-connector-python)
- [Flask Docs](https://flask.palletsprojects.com/en/stable/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/en/20/)

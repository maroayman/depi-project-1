from flask import Flask, request, redirect, render_template
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
from models import db, Note

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY

db.init_app(app)

# ✅ Compatible with Flask 3.x
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        if content:
            new_note = Note(content=content)
            db.session.add(new_note)
            db.session.commit()
        return redirect('/')
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MongoDB and Bcrypt
from models.user_model import mongo, bcrypt
mongo.init_app(app)
bcrypt.init_app(app)

# Import and register Blueprints
from routes.auth_route import auth_bp
from routes.contact_route import contact_bp

app.register_blueprint(auth_bp)
app.register_blueprint(contact_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from blueprints.home.routes import home_bp
from blueprints.about.routes import about_bp
from blueprints.mathematics.routes import mathematics_bp
from blueprints.interests.routes import interests_bp
from blueprints.blog.routes import blog_bp
from blueprints.projects.routes import projects_bp
from blueprints.skills.routes import skills_bp
from blueprints.testimonials.routes import testimonials_bp
from blueprints.contact.routes import contact_bp
from blueprints.hobbies.routes import hobbies_bp
from blueprints.england.routes import england_bp
from blueprints.greece.routes import greece_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(mathematics_bp)
app.register_blueprint(interests_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(skills_bp)
app.register_blueprint(testimonials_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(hobbies_bp)
app.register_blueprint(england_bp)
app.register_blueprint(greece_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

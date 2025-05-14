from flask import Flask, render_template
from web_apps.alexpedia_40k_app.views import bp as alexpedia_bp # from project_2 import bp as project_2_bp  <--- How you would add a second project


app = Flask(__name__, template_folder='templates', static_folder='static')
app.register_blueprint(alexpedia_bp)
# app.register_blueprint(project_2_bp)  <--- How you would add a second project

@app.route('/')
def portfolio():
    return render_template('portfolio.html')

if __name__ == "__main__":
    app.run(debug=True)
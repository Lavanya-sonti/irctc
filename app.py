from flask import Flask ,render_template_string

app =Flask(__name__)

@app.route('/')
def home():
    return render_templates('home.html')

@app.route('/profile')
def myprofile():
    return render_templates(profile.html)

@app.route('/booking')
def Book():
    return render_templates('base,html')

#desbug
if __name__ =='__main__':
    app.run(debug = true)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    return render_template('api.html')


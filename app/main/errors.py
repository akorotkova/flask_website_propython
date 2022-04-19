


@app.errorhandler(404)
def page_not_found(error):
    return render_template('templates/404.html'), 404

@app.errorhandler(403)
def forbidden(error):
    return render_template('templates/403.html'), 403

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('templates/4500.html'), 500




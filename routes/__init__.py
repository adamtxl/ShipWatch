from flask import Blueprint

def register_routes(app):
    from .auth import auth_bp
    from .searches import searches_bp
    from .notifications import notifications_bp
    from .cruises import cruises_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(searches_bp, url_prefix='/searches')
    app.register_blueprint(notifications_bp, url_prefix='/notifications')
    app.register_blueprint(cruises_bp, url_prefix='/cruises')
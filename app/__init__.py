from flask import Flask, g
# from google.cloud import ndb

# ndb_client = ndb.Client()

def create_app():
    app = Flask(__name__)

    from .blueprints.scrap.routes import scrap_bp
    # from .blueprints.events.routes import events_bp
    # from .blueprints.travel_durations.routes import travel_durations_bp

    app.register_blueprint(scrap_bp, url_prefix='/api/scrap')
    # app.register_blueprint(events_bp, url_prefix='/api/events')
    # app.register_blueprint(travel_durations_bp, url_prefix='/api/travel_durations')

    # @app.before_request
    # def before_request():
    #     g.ndb_context = ndb_client.context()
    #     g.ndb_context.__enter__()

    # @app.teardown_request
    # def teardown_request(exception):
    #     g.ndb_context.__exit__(None, None, None)

    return app

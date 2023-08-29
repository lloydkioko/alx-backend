#!/usr/bin/env python3
"""
Instantiates Flask App
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel
from pytz import timezone, utc
import pytz.exceptions
from typing import Dict, Union

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Keeps track of supported languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Returns 7-index.html
    """
    if g.user:
        username = g.user.get('name')
    else:
        username = None
    return render_template('7-index.html', username=username)


@babel.localeselector
def get_locale():
    """
    Matches the language from the Accept-Language header
    """
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    elif g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Returns best matched timezone
    """
    if request.args.get('timezone'):
        query_timezone = request.args.get('timezone')
        try:
            return timezone(query_timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    elif g.user:
        user_timezone = g.user.get('timezone')
        try:
            return timezone(user_timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None

    return utc.zone


def get_user() -> Union[Dict, None]:
    """
    Returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed
    """
    user_id = request.args.get('login_as')

    if user_id:
        return users.get(int(user_id))

    return None


@app.before_request
def before_request():
    """
    Uses get_user to find a user if any, and set it as a global on flask.g.user
    """
    g.user = get_user()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

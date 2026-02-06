from flask import Flask
from routes.profile import profile
from routes.admin import admin
from routes.billing import charge
from oauth.oauth_start import oauth_start
from oauth.oauth_callback import oauth_callback

app = Flask(__name__)

app.add_url_rule("/profile", "profile", profile)
app.add_url_rule("/admin", "admin", admin)
app.add_url_rule("/charge", "charge", charge, methods=["POST"])
app.add_url_rule("/oauth/start", "oauth_start", oauth_start)
app.add_url_rule("/callback", "oauth_callback", oauth_callback)

if __name__ == "__main__":
    app.run(debug=True)
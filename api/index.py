import os
from api import create_app, db

app = create_app()

if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()

    port = int(os.environ.get("PORT", 12345))
    host = os.environ.get("HOST", "0.0.0.0")
    app.run(debug=True, host=host, port=port)


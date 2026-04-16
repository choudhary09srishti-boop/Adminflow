from admin_panel.app import app
import api.routes

if __name__ == "__main__":
    app.run(debug=True, port=8000)
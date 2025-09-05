from flask import Flask, jsonify, request
from app.services import create_booking, get_booking, update_booking, delete_booking
from app.db import init_db
import logging
import os

# Загружаем .env только для локальной разработки
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Инициализация базы данных
    try:
        init_db()
        print(f"Database initialized successfully. URL={os.getenv('DATABASE_URL')}")
    except Exception as e:
        print(f"Error initializing database: {e}")

    @app.route("/ping")
    def ping():
        return jsonify({"status": "ok"}), 200

    @app.route("/booking", methods=["POST"])
    def booking():
        data = request.get_json()
        try:
            result = create_booking(data)
            return jsonify(result), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            logging.exception("Unexpected error in POST /booking")
            return jsonify({"error": "Internal server error"}), 500

    @app.route("/booking/<int:booking_id>", methods=["GET"])
    def get_booking_by_id(booking_id):
        try:
            result = get_booking(booking_id)
            if result:
                return jsonify(result), 200
            return jsonify({"error": "Booking not found"}), 404
        except Exception as e:
            logging.exception("Unexpected error in GET /booking/<id>")
            return jsonify({"error": "Internal server error"}), 500

    @app.route("/booking/<int:booking_id>", methods=["PUT"])
    def update_booking_by_id(booking_id):
        data = request.get_json()
        try:
            updated = update_booking(booking_id, data)
            if updated:
                return jsonify({"booking": updated}), 200
            return jsonify({"error": "Booking not found"}), 404
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            logging.exception("Unexpected error in PUT /booking/<id>")
            return jsonify({"error": "Internal server error"}), 500

    @app.route("/booking/<int:booking_id>", methods=["DELETE"])
    def delete_booking_by_id(booking_id):
        try:
            success = delete_booking(booking_id)
            if success:
                return jsonify({"status": "deleted"}), 200
            return jsonify({"error": "Booking not found"}), 404
        except Exception as e:
            logging.exception("Unexpected error in DELETE /booking/<id>")
            return jsonify({"error": "Internal server error"}), 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
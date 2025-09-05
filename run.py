from app.main import create_app
from app.db import init_db

app = create_app()

if __name__ == "__main__":
    init_db()  # создаст таблицы, если их нет
    app.run(debug=True)
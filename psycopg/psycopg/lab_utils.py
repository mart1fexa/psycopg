"""Вспомогательные функции, добавленные в рамках ЛР1 (вариант 5)."""


def table_exists(conn, name):
    """Проверяет, существует ли таблица name в схеме public."""
    row = conn.execute(
        "SELECT 1 FROM information_schema.tables "
        "WHERE table_schema = 'public' AND table_name = %s",
        (name,),
    ).fetchone()
    return row is not None

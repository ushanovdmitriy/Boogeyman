"""
Рендеринг HTML-отчёта из данных анализа.

Использует Jinja2 для подстановки данных в шаблон templates/report.html.
Сохраняет готовый HTML-файл в папку output/ с именем вида report_YYYY-MM-DD.html.
"""

# TODO: реализовать функцию render_report(analysis_data: dict) -> str
#   - Загружать шаблон templates/report.html через jinja2.Environment + FileSystemLoader
#   - Передавать в шаблон все поля из analysis_data
#   - Возвращать строку с готовым HTML

# TODO: реализовать функцию save_report(html: str) -> str
#   - Создавать папку output/ если не существует
#   - Сохранять файл output/report_YYYY-MM-DD_HH-MM.html
#   - Возвращать абсолютный путь к сохранённому файлу

# TODO: реализовать функцию generate_and_save(analysis_data: dict) -> str
#   - Объединить render_report + save_report
#   - Вернуть путь к файлу

FROM jlesage/firefox

# Используем переменные окружения для пароля и порта
ENV VNC_PASSWORD=${VNC_PASSWORD:-123}  # Пароль по умолчанию — 123
ENV LISTENING_PORT=${PORT:-5800}       # Порт по умолчанию — 5800

# Указываем Railway, что контейнер слушает заданный порт
EXPOSE ${PORT}

# Запускаем приложение
CMD ["/init"]


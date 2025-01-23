FROM jlesage/firefox

# Устанавливаем переменные окружения
ENV VNC_PASSWORD=123
ENV LISTENING_PORT=80

# Перенаправляем стандартный порт VNC на 80 для HTTP доступа
EXPOSE 80

# Указываем точку входа
CMD ["/init"]

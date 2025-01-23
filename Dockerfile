FROM kasmweb/desktop:1.13.0

# Устанавливаем дополнительные утилиты, если нужно
RUN apt-get update && apt-get install -y curl

# Открываем порты для VNC и веб-доступа
EXPOSE 6901
EXPOSE 8080

# Запускаем Kasm Desktop
CMD ["/usr/bin/supervisord"]

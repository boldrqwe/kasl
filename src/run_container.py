import docker

def run_docker_container():
    # Инициализация Docker клиента
    client = docker.from_env()

    # Параметры контейнера
    image = "jlesage/firefox"
    container_name = "firefox_container"
    vnc_password = "123"
    ports = {
        '5800/tcp': 5800,
        '5900/tcp': 5900,
    }

    try:
        # Проверка на существующий контейнер
        existing_container = client.containers.list(
            all=True, filters={"name": container_name}
        )
        if existing_container:
            print(f"Контейнер с именем '{container_name}' уже существует. Удаляю...")
            existing_container[0].remove(force=True)

        # Запуск нового контейнера
        print("Запускаем контейнер...")
        container = client.containers.run(
            image,
            detach=True,
            name=container_name,
            ports=ports,
            environment={"VNC_PASSWORD": vnc_password},
        )
        print(f"Контейнер успешно запущен! ID контейнера: {container.id}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    run_docker_container()

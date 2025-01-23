import subprocess

def run_docker_container():
    # Настройки контейнера
    image = "jlesage/firefox"
    container_name = "firefox_container"
    vnc_password = "123"
    ports = {
        "5800": "5800",
        "5900": "5900"
    }

    # Формируем команду docker run
    docker_run_command = [
        "docker", "run", "-d",
        "--name", container_name,
        "-p", f"{ports['5800']}:5800",
        "-p", f"{ports['5900']}:5900",
        "--env", f"VNC_PASSWORD={vnc_password}",
        image
    ]

    try:
        # Запуск команды
        result = subprocess.run(docker_run_command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Контейнер успешно запущен! ID контейнера: {result.stdout.strip()}")
        else:
            print(f"Ошибка запуска контейнера: {result.stderr.strip()}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    run_docker_container()

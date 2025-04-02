import logging
from subprocess import run as subprocess_run
import threading
from plyer import notification

# set up logging
logger: logging.Logger = logging.getLogger("util logger")
logger.setLevel("warn".upper())
logger.addHandler(logging.StreamHandler())


class RestWindowManager:
    rest_window_thread: threading.Thread = threading.Thread()

    def launch_rest_window(self) -> bool:
        "Return: whether the new thread could start or not."
        is_alive: bool = self.rest_window_thread.is_alive()
        if not is_alive:
            logger.debug("before start new thread.")
            self.rest_window_thread = threading.Thread(
                target=self.run_rest_window_process
            )
            self.rest_window_thread.start()
            logger.debug("after start new thread.")
            return True
        else:
            self.notify_rest_time(minutes=30)
            return False

    @staticmethod
    def run_rest_window_process() -> None:
        "Run this func on another thread because it **blocks** until user quit the window!."
        subprocess_run("rest_window.exe")
        logger.debug("The process has been called.")

    @staticmethod
    def notify_rest_time(minutes: int = 30) -> None:
        notification.notify(
            title="目を休める時間やで！",
            message="{minutes}分たった！はよ目を休めんかい！".format(minutes=minutes),
            app_name="Screen Time Logger",
        )  # type: ignore

    @staticmethod
    def notify_snooze(minutes: int) -> None:
        notification.notify(
            title="はよせい",
            message="もう{minutes}分たった！観念せんかい！".format(minutes=minutes),
            app_name="Screen Time Logger",
        )  # type: ignore

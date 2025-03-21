import logging
from subprocess import run as subprocess_run
import tkinter as tk
from typing import Final
from rest_window_manager import RestWindowManager

# set up logging
logger: logging.Logger = logging.getLogger("rest_window logger")
logger.setLevel("info".upper())
logger.addHandler(logging.StreamHandler())

MSEC_IN_A_SEC: Final[int] = 1000

running_count_down_id: str | None = None


def count_down_rest_time(count_label: tk.Label, rest_seconds: int) -> None:
    global running_count_down_id

    # Cancel current counting down
    if running_count_down_id is not None:
        count_label.after_cancel(running_count_down_id)

    count_label["text"] = str(rest_seconds)
    count_label.update()

    if rest_seconds > 0:
        rest_seconds -= 1
        running_count_down_id = count_label.after(
            MSEC_IN_A_SEC, count_down_rest_time, count_label, rest_seconds
        )
    else:
        running_count_down_id = None


def open_rest_link() -> None:
    subprocess_run(
        "rest.url",
        shell=True,
    )


def main() -> None:
    # init
    font_size: int = 500
    rest_seconds: int = 30

    rest_master: tk.Tk = tk.Tk("Rest Window")
    count_label: tk.Label = tk.Label(rest_master, text="0", font=("normal", font_size))
    count_button: tk.Button = tk.Button(
        rest_master,
        text="Count seconds",
        command=lambda: count_down_rest_time(count_label, rest_seconds),
    )
    open_link_button: tk.Button = tk.Button(
        rest_master, text="Open link", command=open_rest_link
    )

    count_label.grid(row=0, column=0, columnspan=2)
    count_button.grid(row=1, column=0)
    open_link_button.grid(row=1, column=1)

    RestWindowManager.notify_rest_time(minutes=30)

    # start tk loop
    rest_master.mainloop()


if __name__ == "__main__":
    logger.info("rest_window.py start running.")
    main()

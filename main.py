import logging
from subprocess import run as subprocess_run
import tkinter as tk
from typing import Final
from rest_window_manager import RestWindowManager

# set up logging
logger: logging.Logger = logging.getLogger("main logger")
logger.setLevel("warn".upper())
logger.addHandler(logging.StreamHandler())

MSEC_IN_A_MIN: Final[int] = 60 * 1000
MIN_IN_A_HOUR: Final[int] = 60

do_count: bool = True
rest_window_manager: RestWindowManager = RestWindowManager()

# for debug
make_fast_to_debug: bool = False


def call_work_in_tk(
    count_label: tk.Label,
    format_displaying_time: str,
    counting_minutes: int,
    minutes_by_rest: int,
) -> None:
    "Helper function. Make label to call after with parameters."

    # for debug
    wait_ms: int = 1000 if make_fast_to_debug else MSEC_IN_A_MIN

    count_label.after(
        wait_ms,
        work_in_tk,
        count_label,
        format_displaying_time,
        counting_minutes,
        minutes_by_rest,
    )


def count_up_and_updata_label(
    count_label: tk.Label, format_displaying_time: str, counting_minutes: int
) -> int:
    "Count up time, and updata time label in tk."
    # count up
    counting_minutes += 1

    # updata text
    count_label["text"] = format_displaying_time.format(
        counting_minutes // MIN_IN_A_HOUR, counting_minutes % MIN_IN_A_HOUR
    )  # hours:minutes

    return counting_minutes


def display_directory_having_link() -> None:
    "Current directory must be this directory."
    subprocess_run(
        "start .",
        shell=True,
    )


def main() -> None:
    # init
    ## values
    format_displaying_time: str = "{}:{}"
    font_size: int = 60
    minutes_by_rest: int = 30

    ## tk
    main_root: tk.Tk = tk.Tk()
    main_root.title("Screen Time Logger")
    count_label: tk.Label = tk.Label(
        main_root, text=format_displaying_time.format(0, 0), font=("normal", font_size)
    )
    pause_button: tk.Button = tk.Button(
        main_root,
        text="Pause",
        command=lambda: switch_pause_and_restart_count(pause_button),
    )
    change_link_button: tk.Button = tk.Button(
        main_root, text="Change link", command=display_directory_having_link
    )

    pause_button.grid(row=0, column=1)
    count_label.grid(row=0, rowspan=2, column=0)
    change_link_button.grid(row=1, column=1)

    # set trigger
    call_work_in_tk(
        count_label,
        format_displaying_time,
        0,
        minutes_by_rest,
    )

    # run
    main_root.mainloop()
    logger.info("Done!")


def switch_pause_and_restart_count(button: tk.Button) -> None:
    global do_count
    do_count = not do_count

    # switch text
    if do_count:
        button["text"] = "Pause"
    else:
        button["text"] = "Restart"


def work_in_tk(
    count_label: tk.Label,
    format_displaying_time: str,
    counting_minutes: int,
    minutes_by_rest: int,
) -> None:
    "Do every things in tk."
    # count up
    if do_count:  # pause
        counting_minutes = count_up_and_updata_label(
            count_label, format_displaying_time, counting_minutes
        )

    # It's time to rest!
    if counting_minutes % minutes_by_rest == 0:
        rest_window_manager.launch_rest_window()

    # loop with calling next.
    call_work_in_tk(
        count_label,
        format_displaying_time,
        counting_minutes,
        minutes_by_rest,
    )


if __name__ == "__main__":
    logger.info("Runnning starts!")
    main()

from plyer import notification


def put_notification() -> None:
    # This error hint is no ploblem.
    notification.notify(
        title="目を休める時間やで！",
        message="30分たった！はよ目を休めんかい！",
        app_name="Screen Time Logger",
    )


if __name__ == "__main__":
    put_notification()

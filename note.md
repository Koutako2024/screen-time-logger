# TODO
* use threading not to freeze the main window.
* change to, "Pause" to .after_cancel() and "Restart" to .after() again.
* add a property file.

# To convert to Exe
* When you use the notification in plyer, you must add `--hidden-import plyer.platforms.win.notification` parameter. (https://stackoverflow.com/questions/64965160/modulenotfounderror-no-module-named-plyer-platforms-when-exe-created-by-pyins)
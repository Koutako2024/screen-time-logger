# TODO
* pystray
* make func to notify after a minute from launching the rest window. (Snooze)
* add a property file. (in [TOML](https://qiita.com/Magnolia/items/76703179248f17e6b519)?)
  * notification
    * title
    * message
  * rest
    * link
      * launch command
    * time
      * until rest
      * while rest
  * dev
    * log level
    * count up speed
* notify the end of resting.

# To convert to Exe
* When you use the notification in plyer, you must add `--hidden-import plyer.platforms.win.notification` parameter. (https://stackoverflow.com/questions/64965160/modulenotfounderror-no-module-named-plyer-platforms-when-exe-created-by-pyins)

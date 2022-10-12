# Overview

This script allows you automate bonus gathering in android application [Мой life:)](https://play.google.com/store/apps/details?id=by.com.life.lifego&hl=en_US&gl=US).

## Requirements
1. You must be a customer of a belarussian mobile operator [Life](https://life.com.by/).
2. Linux as OS.
3. [Appium Server](https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4).
4. [Android Studio](https://developer.android.com/studio).

    Instead of last 2 requirements you may simply launch [Android Emulator in Docker](https://github.com/budtmo/docker-android/).

### `Config` editting
1. credentials\
`login` and `password` shoud contained your phone number and password you use to login in android application [Мой life:)](https://play.google.com/store/apps/details?id=by.com.life.lifego&hl=en_US&gl=US).
2. appium_server\
`host` and `port` should contained host and port from Appium Server.\
3. telnet_token \
To get token you need to connect to running android emulator manually ([instructions](https://developer.android.com/studio/run/emulator-console)).\
4. emulator \
`host` by default is `localhost` or `127.0.0.1`. To get `port` you should enter the follow with running emulator:
    ```
    adb devices
    ```
    The output will be like `emulator-5554`. The numbers define `port`. In this example `port` is `5554`. \
5.  apk_path \
If you're using [docker-android](https://github.com/budtmo/docker-android/) provide the url of apk file ([example](https://trashbox.ru/files20/1705225_f5c2a6/by.com.life.lifego_1.0.93_171.apk)) or push apk to docker's container and provide this path.\
In case you don't use docker just leave this parameter empty.

### Configuring Appium Server
Note: in docker's case you should note configure Appium.
To configure Appium Server just follow the [instruction](https://medium.com/@iqra.bibi/appium-installation-on-linux-ccb102ebdc1).

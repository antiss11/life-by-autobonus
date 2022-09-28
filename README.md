# Overview

This script allows you automate bonus gathering in android application [Мой life:)](https://play.google.com/store/apps/details?id=by.com.life.lifego&hl=en_US&gl=US).

## Requirements
1. You must be a customer of a mobile operator [Life](https://life.com.by/).
2. `Linux` as OS.
3. [Appium Server](https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4)(#appium_server).
4. [Android Studio](https://developer.android.com/studio).

### Configuring `Appium Server`
To configure `Appium Server` follow the [instructions](https://medium.com/@iqra.bibi/appium-installation-on-linux-ccb102ebdc1).

### `Config` editting
1.`credentials`\
`login` and `password` shoud contained your phone number and password you use to login in android application [Мой life:)](https://play.google.com/store/apps/details?id=by.com.life.lifego&hl=en_US&gl=US). \
2. `appium_server`\
`host` and `port` should contained host and port from `Appium Server`.\
3. `telnet_token` \
To get token you need to connect to running android emulator manually ([instructions](https://developer.android.com/studio/run/emulator-console)).\
4. `android_vdi` \
`host` by default is `localhost` or `127.0.0.1`. To get `port` you should enter the follow with running emulator:
``` bash
adb devices
```
The output will be like `emulator-5554`. The numbers define `port`. In this example `port` is `5554`.

### Headless mode
Script also works with android in headless mode! To make your android emulator headless follow [this](https://gist.github.com/nhtua/2d294f276dc1e110a7ac14d69c37904f). 

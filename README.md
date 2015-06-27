Pushbullet ⥦ IRC Gateway
========================

pbirc is a pair of scripts that, together, allow you to read all of your
notifications, and push links to your devices, directly from IRC.

Currently, the module ``messenger.py`` is able to maintain an IRC connection,
and will repeat anything stated on its ``stdin``. ``pushbullet.py`` is the
Pushbullet end of the app, and will print out a specially formatted line every
time a notification is sent over Pushbullet:

    appname | notification title: body body body...

Currently, it does not support replying with links, nor does it actually support
talking between messenger and pushbullet.

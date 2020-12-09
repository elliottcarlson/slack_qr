# slack_qr
Generate a QR code using Slack emoji

# Instructions
```
$ pip install -r requirements.txt
$ ./slack_qr.py text here
```

# Parameters

| Parameter                        | Description                                                        |
| -------------------------------- | ------------------------------------------------------------------ |
| -l [emoji], --light [emoji]      | Specify the light colored emoji to use, defaults to :white_square: |
| -d [emoji], --bark [emoji]       | Specify the dark colored emoji to use, defaults to :black_square:  |
| -b, --border                     | Enable a border around the QR code, default is off                 |

# Examples

```
$ ./slack_qr.py -l lolstone -d eggplant https://youtu.be/dQw4w9WgXcQ
:lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone:
:lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone:
:lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone:
:lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::lolstone::lolstone::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone:
:lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone:
:lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone:
:lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::lolstone::lolstone::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone:
:lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone:
:lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone:
:lolstone::eggplant::lolstone::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone:
:lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::eggplant::eggplant::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone:
:lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::eggplant::lolstone::eggplant::lolstone::lolstone::lolstone:
:lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::eggplant::lolstone:
:lolstone::lolstone::eggplant::lolstone::lolstone::lolstone::eggplant::eggplant::lolstone::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone:
:lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone:
:lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone:
:lolstone::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::eggplant::lolstone::lolstone::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone:
:lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::lolstone::lolstone::lolstone:
:lolstone::eggplant::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::eggplant::lolstone::lolstone::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone:
:lolstone::eggplant::eggplant::lolstone::lolstone::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone:
:lolstone::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::lolstone::lolstone::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone:
:lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::lolstone::lolstone::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::lolstone:
:lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::eggplant::lolstone::lolstone::eggplant::lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::lolstone::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::lolstone:
:lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::lolstone:
:lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::eggplant::lolstone::lolstone::lolstone::eggplant::lolstone:
:lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::lolstone::lolstone::lolstone:
:lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::eggplant::eggplant::lolstone::lolstone::lolstone::eggplant::lolstone::lolstone::lolstone::eggplant::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::lolstone:
:lolstone::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::eggplant::eggplant::lolstone::eggplant::lolstone::lolstone::eggplant::eggplant::lolstone::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone:
:lolstone::eggplant::lolstone::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::lolstone:
:lolstone::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::eggplant::lolstone::eggplant::eggplant::eggplant::lolstone::lolstone::lolstone::lolstone::eggplant::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::lolstone::eggplant::lolstone::eggplant::lolstone::lolstone::lolstone::lolstone:
:lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone::lolstone:
```

# Limitations
Slack has a limit of 12,000 characters in a message - if the emoji names you are using too long, and the text content of
the QR code is too long, then the generated emoji will be too large to send. To work around this, you can create an
alias of the emoji name you are using at https://slack.com/customize/emoji

For a QR code to scan properly you need to make sure you have well contrasting emoji or it might not scan properly.

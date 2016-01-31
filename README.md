# Github notifications via Free Mobile SMS
SMS notifications with python, github-api and free mobile.

## Make it work for you
* Clone the repo
* `[editor] config.cfg` (See below)
* `pip install -r requirements.txt`
* `python main.py`

You must create `config.cfg` with your credentials.
```
[Github]
username: foo
token: *****

[Free]
user: bar
pass: *****
```
You need a personal access tokens for github with `repo` and ` notifications` scopes.
You can find the free mobile pass in the options tab of your account on [mobile.free.fr](http://mobile.free.fr/)

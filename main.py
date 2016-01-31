import sys,requests,configparser

github_username = ''
github_token = ''
free_user = ''
free_pass = ''
def loadConfig():
    config = configparser.ConfigParser()
    config.read('config.cfg')
    
    global github_username,github_token,free_user,free_pass
    try:
        github_username = config['Github']['username']
        github_token = config['Github']['token']
        free_user = config['Free']['user']
        free_pass = config['Free']['pass']
    except:
        print('Missing information in config.cfg, see README.md')
        sys.exit(1)

def githubAPI(action):
	r = requests.get('https://api.github.com' + action, auth=(github_username, github_token))
	return r.json()

def sendSMS(msg):
	return requests.post('https://smsapi.free-mobile.fr/sendmsg', params={'user' : free_user, 'pass' : free_pass, 'msg' : msg}).status_code

if __name__ == '__main__':
    loadConfig()

    notifs = githubAPI('/notifications')
    unread = []
    for notif in notifs:
        if notif['unread']:
            unread.append(notif)

    msg = '[Github] Unread notifications :\n'
    for n in unread:
        msg += "    [" + n['subject']['type'] + "] " + n['subject']['title'] + " in " + n['repository']['full_name'] + "\n"

    sendSMS(msg)

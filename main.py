### Importing Packages ###
import requests;

## Cookies File ##
cookiesFile = open('cookies.txt', 'r');
cookies = cookiesFile.read().split('\n');

## User ID Input ##
user_ID = input('Roblox\'s user ID?\nType the user ID... ');

#################### GET PROXIES ####################
## Proxies File ##
proxiesFile = open('proxies.txt', 'r');
proxies = proxiesFile.read().split('\n');

#################### MATH STUFF ####################
if proxies[0] == '':
  print('\x1b[33mNo proxies detected. The code will error.\x1b[0m');

if cookies[0] == '':
  print('\x1b[33mThis feature will not work without cookies.\x1b[0m');

#################### MAIN FOLLOW BOTTER ####################
for cookie in cookies:
  for proxy in proxies:
    proxyObj = {
      'https': 'https://{proxyThing}'.format(proxyThing=proxy),
    };
    print('\x1b[32mSending {amount} follower(s) to {user}\x1b[0m'.format(amount=len(cookies), user=user_ID));
    csrfHeaders = {
      'Cookie': '.ROBLOSECURITY=' + cookie,
    };
    ## CSRF Request ##
    try:
      csrfRequest = requests.post('https://auth.roblox.com/v2/logout', headers=csrfHeaders, proxies=proxyObj);
      ## If Statement For CSRF ##
      if csrfRequest.status_code == 403:
        csrfToken = csrfRequest.headers['x-csrf-token'];
        ## Headers ##
        headers = {
          'X-CSRF-TOKEN': csrfToken,
          'Cookie': '.ROBLOSECURITY=' + cookie,
        };
        ## Follow Request ##
        r = requests.post('https://friends.roblox.com/v1/users/{user}/follow'.format(user=user_ID), headers=headers);
        ## If Statement For Follow Botter ##
        if r.status_code == 200:
          print('\x1b[32mSuccessfully followed! Status code: 200\x1b[0m');
        ## Else Statement For Follow Botter ##
        elif r.status_code == 401:
          print('\x1b[31mInvalid cookie. Status code: 401\x1b[0m'); 
      ## Else Statement For CSRF ##
      else:
        print('\x1b[31mGetting the CSRF Token will not work with invalid cookies.\x1b[0m');
        break;
    except OSError as e:
      print('\x1b[31mAn error has occured! ' + e + '\x1b[0m')

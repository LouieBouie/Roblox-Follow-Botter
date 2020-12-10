#Important #1
import requests;

# Important #2
cookiesFile = open('cookies.txt', 'r');
cookies = cookiesFile.read().split('\n');

# User ID input.
user_ID = input('Roblox\'s user ID?\nType the user ID... ');

# Main follow botter.
for cookie in cookies:
  print('\x1b[32mSending {amount} follower(s) to {user}\x1b[0m'.format(amount=len(cookies), user=user_ID));
  csrfHeaders = {
    'Cookie': '.ROBLOSECURITY=' + cookie,
  };
  # CSRF request.
  csrfRequest = requests.post('https://auth.roblox.com/v2/logout', headers=csrfHeaders);
  # If statement for CSRF.
  if csrfRequest.status_code == 403:
    csrfToken = csrfRequest.headers['x-csrf-token'];
    # Headers
    headers = {
      'X-CSRF-TOKEN': csrfToken,
      'Cookie': '.ROBLOSECURITY=' + cookie,
    };
    # Follow request.
    r = requests.post('https://friends.roblox.com/v1/users/{user}/follow'.format(user=user_ID), headers=headers);
    # If statement for follow botter.
    if r.status_code == 200:
      print('\x1b[32mSuccessfully followed! Status code: 200\x1b[0m');
    # Else statement for follow botter.
    elif r.status_code == 401:
      print('\x1b[31mInvalid cookie. Status code: 401\x1b[0m'); 
  # Else statement for CSRF.
  else:
    print('\x1b[31mGetting the CSRF Token will not work with invalid cookies.\x1b[0m');
    break;

import api
import time
try:
    resp,c = api.phone_login()
except api.requests.exceptions.ConnectionError:
    api.start_server()
    time.sleep(2)
    resp,c = api.phone_login()

print(api.get_user_playlist(1854260783,c))

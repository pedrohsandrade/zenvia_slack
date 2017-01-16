#zenvia_bot_slack
#Por pedrohsandrade

import time , requests
from slackclient import SlackClient

slack_client = SlackClient ('xoxb-118898388294-T7XTQJlgS6dF1dqZtzzfuuQk')
http = 'https://api-rest.zenvia360.com.br/services'
i = True

print ("zenvia_slack inicializado")
while True:
       try:
           r = requests.get (http) 
       except:              
              if i:
                     slack_client.api_call("chat.postMessage", channel='#general',text="O Zenvia SMS não está em funcionamento", as_user=True)
                     i = False              
       else:
              if not i:
                     slack_client.api_call("chat.postMessage", channel='#general',text="O Zenvia SMS retornou a normalidade", as_user=True)
                     i = True
       finally:
              time.sleep (60)

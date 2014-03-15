import twitter
from stratum import settings

import stratum.logger
log = stratum.logger.get_logger('Notify_Tweet')

class NOTIFY_TWITTER():

#   def notify_start(self):
#        if len(settings.TWITTER_CONSUMER_KEY) != '':
#            self.send_tweet('Test')

   def notify_found_block(self,worker_name):
        if len(settings.TWITTER_CONSUMER_KEY) != '':
            text = 'Woot, %s found a block! %s' % (worker_name,settings.TWITTER_HASHTAGS)
            self.send_tweet(text)

   def send_tweet(self,message):
   	try:
        	api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY,consumer_secret=settings.TWITTER_CONSUMER_SECRET, access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY, access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET);
                api.PostUpdate(message);                
        except Exception as e:
            log.error('Error sending TWEET: %s' % e[0])


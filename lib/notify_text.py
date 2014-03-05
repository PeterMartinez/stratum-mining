from twilio.rest import TwilioRestClient

from stratum import settings

import stratum.logger
log = stratum.logger.get_logger('Notify_Text')

class NOTIFY_TEXT():

    def notify_start(self):
        if len(settings.NOTIFY_TEXT_TO) != 0:
            self.send_texts(settings.NOTIFY_TEXT_TO,'Stratum Server Started','Stratum server has started!')

    def notify_found_block(self,worker_name):
        if len(settings.NOTIFY_TEXT_TO) != 0:
            text = '%s on Stratum server found a block!' % worker_name
            self.send_texts(settings.NOTIFY_TEXT_TO,'Stratum Server Found Block',text)

    def send_texts(self,to,subject,message):
        for person in to:
            self.send_text(person,subject,message)

    def send_text(self,text_to,subject,message):
        text_body = subject +"\n"+message

        try:
                client = TwilioRestClient(settings.NOTIFY_TEXT_SID, settings.NOTIFY_TEXT_AUTH_TOKEN)
                message = client.sms.messages.create(
                          body=text_body,
                          to=text_to,    # Replace with your phone number
		          from_=settings.NOTIFY_TEXT_FROM) # Replace with your Twilio number
        except Exception as e:
            log.error('Error sending TEXT: %s' % e[0])


import requests
import json
import pocket_constants
from pocket_retrieve import PocketRetrieve

class PocketModify:

    def __init__(self):
        self.pocketRetriever = PocketRetrieve()

    def preModify(self):
        self.modify([])

    def modify(self,oActions):
        """
        Send request to Pocket with tags to add to articles.  Send as batch to
        avoid hitting rate limiter.
        """
        oPayload = {'access_token':pocket_constants.strToken,'consumer_key':pocket_constants.strConsumerKey,'actions':oActions}

        requests.post(pocket_constants.strModifyURL, data=json.dumps(oPayload), headers=pocket_constants.oHeaders)
        return

    def postModify(self):
        pass

class TwitterAPI:

    def __init__(self, auth):
        self.auth = auth
    
    def get_mentions_timeline(self):
        url = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'
        return self.auth.get(url).json()

    def get_twitter(self, id):
        url = 'https://api.twitter.com/1.1/statuses/show.json?id={}'
        return self.auth.get(url.format(id)).json()
    
    def reply_to(self, status, in_reply_to_status_id):
        params = {
            'status': status,
            'in_reply_to_status_id': in_reply_to_status_id,
            'auto_populate_reply_metadata': 'true'
        }
        url = 'https://api.twitter.com/1.1/statuses/update.json'
        return self.auth.post(url, params=params).json()
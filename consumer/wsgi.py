import falcon

events = []

class Events:
    def on_get(self, req, resp):
        resp.media = {
            'events': events
        }

    def on_post(self, req, resp):
        events.append(req.media)

application = falcon.API()
application.add_route('/events', Events())


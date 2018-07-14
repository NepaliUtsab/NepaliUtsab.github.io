

class ResponseInfo(object):
    def __init__(self, user=None, **args):
        self.response = {
            "status": args.get('status', True),
            "error": args.get('error', 200),
            "data": args.get('data', []),
            "message": args.get('message', 'success')
            }
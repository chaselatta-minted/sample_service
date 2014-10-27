from m_services.handlers.handler import BaseHandler

class Handler(BaseHandler):
  def get(self):
    return self.finalize('x', None)

def register_routes(api):
  api.add_resource(Handler, '/sample_service/blah')
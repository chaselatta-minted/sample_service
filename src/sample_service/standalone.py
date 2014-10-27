
### ALLOWS THIS TO BE RUN ALONE


from m_services.plugin.run import prepare_standalone, run_app
from m_services.handlers.handler import BaseHandler

(app, api) = prepare_standalone()

class Handler(BaseHandler):
  def get(self):
    return self.finalize('x', None)


api.add_resource(Handler, '/')

run_app(app)
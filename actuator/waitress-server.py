from paste.translogger import TransLogger
from waitress import serve
import app
serve(TransLogger(app.app), host='0.0.0.0', port=8080)

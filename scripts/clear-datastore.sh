# remote api
google_appengine/remote_shell_api.py ceg-86

# fix the path
sys.append(os.path.join(os.getcwd(), 'ceg-86')
import models

query =  models.Member.all()
entries = query.fetch(1000)
db.delete(entries)

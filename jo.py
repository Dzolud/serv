from data import db_session
from data.profils import Profile
from data.bookmark import Bookmarks

db_session.global_init("db/users.db")




# prof = Profile()
# prof.chat_id = 1332
# prof.login = 'qwerty'
# prof.set_password("1234")
#
# db_sess = db_session.create_session()
#
# db_sess.add(prof)
# db_sess.commit()

db_sess = db_session.create_session()

bm = Bookmarks()
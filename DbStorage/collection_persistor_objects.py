from DbStorage.raw_email_persistor import RawEmailsPersistor
from DbStorage.users_persistor import UsersPersistor
from DbStorage.leave_dates_by_location_persistor import LeaveDatesPersistor
from DbStorage.requests_persistor import RequestsPersistor

raw_emails_persistor = RawEmailsPersistor()
users_persistor = UsersPersistor()
leave_dates_persistor = LeaveDatesPersistor()
requests_persistor = RequestsPersistor()
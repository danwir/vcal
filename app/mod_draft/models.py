# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app.common.models import DyBase
from flywheel import Field, NUMBER, GlobalIndex

# Define a User model

class PublicHoliday(DyBase):

    __tablename__ = 'public_holiday'

    __metadata__ = {
        'global_indexes': [
            GlobalIndex.all('ts-index', 'holiday_date').throughput(read=10, write=2),
        ],
    }

    # dateField(data_type=STRING, hash_key=True)
    holiday_date    = Field(data_type=NUMBER,  nullable=False)
    # full day or half day
    is_halfday   = Field(data_type=NUMBER, nullable=False)

    # New instance instantiation procedure
    def __init__(self, date, is_halfday):
        super(PublicHoliday, self).__init__()
        self.holiday_date  = date
        self.is_halfday    = is_halfday

    def __repr__(self):
        return '<Date %r>' % (str(self.holiday_date))

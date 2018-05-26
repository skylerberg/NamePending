from enum import Enum


class SubmissionStatus(Enum):
    IN_REVIEW = 'In Review'
    REVIEWED = 'Reviewed'


class EventTypes(Enum):
    COMMENTED = 'Commented'
    STATUS_CHANGED = 'Status Changed'
    POINTS_EDITED = 'Points Edited'
    SUMBISSION_EDITED = 'Submission Edited'
    SUMBISSION_CREATED = 'Submission Created'

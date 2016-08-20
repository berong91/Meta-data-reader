from __future__ import unicode_literals

from django.db import models



class Source(models.Model):
    """
    Define a source file attribute
    """
    source_name = models.CharField(max_length=255, primary_key=True)  # the file name of a source
    date = models.DateTimeField('date added')  # the detected date
    modified_date = models.DateTimeField('date modified')  # the modified date (replaced)


class Record(models.Model):
    """
    Define rating type and color code for each type
    """
    # Define rating types and value
    CLEAN = "clean"
    LOW = "low-risk"
    MEDIUM = "medium-risk"
    HIGH = "high-risk"
    MALICIOUS = "malicious"
    EVENT_TYPES = (
        (CLEAN, "Alert"),
        (LOW, "Low Risk"),
        (MEDIUM, "Medium Risk"),
        (HIGH, "High Risk"),
        (MALICIOUS, "Malicious"),
    )
    
    # map ratings to colours
    COLOUR = {
        CLEAN: "66ff33",
        LOW: "FF6A00",
        MEDIUM: "FF0000",
        HIGH: "FFE800",
        MALICIOUS: "999966",
    }
    
    """
    Define a record attribute
    """
    source = models.ForeignKey(Source, on_delete=models.CASCADE)  # reference source file
    date = models.DateTimeField('date published', primary_key=True)  # date of a record
    filename = models.CharField(max_length=255, primary_key=True)  # file name of record
    action = models.CharField(max_length=50)  # action, may need to re-define later
    submit_type = models.CharField(max_length=50)  # submit type of a record
    rating = models.CharField(max_length=16, choices=EVENT_TYPES, default=MALICIOUS)  # rating type, defined above
    
    @property
    def colour(self):
        """
        Return the hexadecimal colour of this rating
        """
        self.COLOUR[self.ratingType]

from __future__ import unicode_literals

from django.db import models


class Source(models.Model):
    """
    Define a source file attribute
    """
    source_name = models.CharField(max_length=255, primary_key=True)  # the file name of a source
    date_added = models.DateTimeField('date added')  # the detected date
    date_modified = models.DateTimeField('date modified')  # the modified date (replaced)
    
    def __unicode__(self):
        return u'Source: {0}, added {1}, last modified {2}'.format(
            self.source_name,
            self.date_added,
            self.date_modified
        )


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
        CLEAN: "active",
        LOW: "info",
        MEDIUM: "warning",
        HIGH: "danger",
        MALICIOUS: "success",
    }
    
    """
    Define a record attribute
    """
    source = models.ForeignKey(  # reference source file
        Source,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField('date published')  # date of a record
    filename = models.CharField(max_length=255)  # file name of record
    action = models.CharField(max_length=50)  # action, may need to re-define later
    rating = models.CharField(max_length=16, choices=EVENT_TYPES, default=MALICIOUS)  # rating type, defined above
    submit_type = models.CharField(max_length=50)  # submit type of a record
    
    @property
    def colour(self):
        return self.COLOUR[self.rating]
    
    def __unicode__(self):
        return u'{0} - Threat level {1}, action {2} (Published at {3} by {4})'.format(
            self.filename,
            self.rating,
            self.action,
            self.date,
            self.submit_type
        )

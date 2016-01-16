from django.db import models
from django.core.validators import RegexValidator
from organizations.models import Organization

# Create your models here.
class Member(models.Model):
    """
    This is a model that represent a member in the club.
    """
    COLLEGES = (
        'McMurtry', 'Martel', 'Brown',
        'Duncan', 'Jones', 'Lovett',
        'Will Rice', 'Hanzen', 'Sid Rich',
        'Baker', 'Wiess'
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(validators=[
        RegexValidator(regex="*@rice.edu", message="Not a valid Rice Email.")
    ])
    phone_number = models.IntegerField(blank=True)
    college = models.CharField(max_length=10, choices=COLLEGES)
    grad_year = models.IntegerField(max_length=4)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE())

    def to_json(self):
        """
        This will take the current member and return the jsonified version of self.
        :return: model_json
        """
        model_json = {'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email,
                      'phone_number': self.phone_number, 'college': self.college, 'grad_year': self.grad_year,
                      'organization': self.organization.name}

        return model_json

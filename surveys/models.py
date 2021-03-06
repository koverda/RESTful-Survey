from django.db import models


RECOMMEND_CHOICES = (
    ('1', '1 - Very Unlikely'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10 - Very Likely'),
)
BOOL_CHOICES = (
    (1, 'Yes'), 
    (0, 'No')
)


class Survey(models.Model):
    # date survey was taken
    created = models.DateTimeField(auto_now_add=True)

    recommend_company = models.CharField('How likely would you be to recommend this company to a friend?', 
                                         max_length = 2, choices = RECOMMEND_CHOICES)

    what_changes = models.CharField('What would you change about the product?',
                                    max_length = 500, default = '')
    
    was_researched = models.CharField('Did you research the product before purchasing it?', 
                                         max_length = 2, choices = BOOL_CHOICES, default = 'Yes')
    # optional field
    feedback = models.CharField('Would you like to provide any other feedback?',
                                max_length = 500, blank = True, default = '')

    owner = models.ForeignKey('auth.User', related_name='surveys')

    class Meta:
        ordering = ('created',)
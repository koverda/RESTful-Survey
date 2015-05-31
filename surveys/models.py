from django.db import models

'''
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
'''

'''
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
'''

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
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class Survey(models.Model):
    # date survey was taken
    created = models.DateTimeField(auto_now_add=True)
    # how likely are you to recommend this company to a friend?
    recommend_company = models.CharField('How likely would you be to recommend this company to a friend?', 
                                         max_length = 2, choices = RECOMMEND_CHOICES)
    # what changes would you make to our product?
    what_changes = models.CharField('What would you change about the product?',
                                    max_length = 500, default = '')
    # did you research the product before purchasing?
    was_researched = models.BooleanField('Did you research the product before purchasing it?', 
                                         choices = BOOL_CHOICES, default = True)
    # optional field
    feedback = models.CharField('Would you like to provide any other feedback?',
                                max_length = 500, blank = True, default = '')
    owner = models.ForeignKey('auth.User', related_name='surveys')

    class Meta:
        ordering = ('created',)
'''
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly',
                             max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets')
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

        # limit the number of instances retained
        snippets = Snippet.objects.all()
        if len(snippets) > 100:
            snippets[0].delete()
'''
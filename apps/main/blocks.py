from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class StudentWork(blocks.StructBlock):
    name = blocks.CharBlock(required=True, max_length=25)
    role = blocks.CharBlock(required=True, max_length=25)
    type = blocks.CharBlock(required=True, max_length=25)
    profile = ImageChooserBlock(required=True)
    work = ImageChooserBlock(required=True)

    def __str__(self):
        return self.name

    class Meta:
        template = 'blocks/student-works.html'
        verbose_name = _('Student Work')
        verbose_name_plural = _('Student Works')


class KeyHighlight(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=25)
    description = blocks.CharBlock(required=True, max_length=255)
    icon = ImageChooserBlock(required=True)

    def __str__(self):
        return self.heading

    class Meta:
        template = 'blocks/key-highlight.html'
        verbose_name = _('Key Highlight')
        verbose_name_plural = _('Key Highlights')


class keyValue(blocks.StructBlock):
    text = blocks.CharBlock(required=True, max_length=25)
    value = blocks.CharBlock(required=True, max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        template = 'blocks/key-value.html'
        verbose_name = _('Key Value')
        verbose_name_plural = _('Key Values')


class Testimonial(blocks.StructBlock):
    profile = ImageChooserBlock(required=True)
    name = blocks.CharBlock(required=True, max_length=25)
    role = blocks.CharBlock(required=True, max_length=255)
    content = blocks.TextBlock(required=True, max_length=2000)
    logo = ImageChooserBlock(required=True)

    def __str__(self):
        return self.name

    class Meta:
        template = 'blocks/testimonial.html'
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')


class EvolutionPoints(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=25)
    description = blocks.TextBlock(required=True, max_length=2000)
    year = blocks.CharBlock(required=True, max_length=25)

    def __str__(self):
        return self.heading

    class Meta:
        template = 'blocks/evolution-points.html'
        verbose_name = _('Evolution Point')
        verbose_name_plural = _('Evolution Points')


class Article(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    url = blocks.URLBlock(required=True)
    image = ImageChooserBlock(required=True)
    publisher = blocks.CharBlock(required=True, max_length=255)
    date = blocks.DateBlock(required=True)

    def __str__(self):
        return self.heading

    class Meta:
        template = 'blocks/article.html'
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')


class FAQ(blocks.StructBlock):
    question = blocks.TextBlock(required=True)
    answer = blocks.TextBlock(required=True)

    def __str__(self):
        return self.question

    class Meta:
        template = 'blocks/faq.html'
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')


class BreakdownPoint(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    description = blocks.TextBlock(required=True, max_length=2000)
    points = blocks.ListBlock(
        blocks.CharBlock(required=True, max_length=255),
        label="List of Points"
    )

    def __str__(self):
        return self.heading

    class Meta:
        template = 'blocks/breakdown-point.html'
        verbose_name = _('Breakdown Point')
        verbose_name_plural = _('Breakdown Points')


class Card(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    description = blocks.TextBlock(required=True, max_length=2000)
    image = ImageChooserBlock(required=True)

    def __str__(self):
        return self.heading

    class Meta:
        template = 'blocks/card.html'
        verbose_name = _('Card')
        verbose_name_plural = _('Cards')


class WhoAreWePoints(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    value = blocks.CharBlock(required=True, max_length=255)
    image = ImageChooserBlock(required=False)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = _('Who Are We')
        verbose_name_plural = _('Who Are We')

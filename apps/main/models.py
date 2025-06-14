from django.db.models import *
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.translation import gettext as _
from wagtail import blocks
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page

from apps.main.blocks import StudentWork, KeyHighlight, keyValue, Testimonial, EvolutionPoints, Article, FAQ, \
    BreakdownPoint, Card, WhoAreWePoints
from utils.toast import Toast


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BasePage(Page):
    heading = RichTextField(_('Heading'), max_length=255)
    description = TextField(_('Description'), max_length=255)
    image = ForeignKey('wagtailimages.Image', on_delete=PROTECT, related_name='+')

    class Meta:
        abstract = True


class Home(BasePage):
    template = "index.html"
    max_count = 1
    parent_page_types = []

    Brand_images = StreamField([('image', ImageChooserBlock())], use_json_field=True, min_num=3)

    who_are_we_heading = RichTextField(_('Heading'), max_length=255)
    who_are_we_description = RichTextField(_('Description'), max_length=255)
    who_are_we_subheading = TextField(_('Subheading'), max_length=255)
    who_are_we_sub_description = TextField(_('Sub Description'), max_length=2000)
    who_are_we_images = StreamField([('image', ImageChooserBlock())], use_json_field=True, min_num=3)
    who_are_we_points = StreamField([('point', WhoAreWePoints())], use_json_field=True, min_num=3)

    commit_heading = RichTextField(_('Heading'), max_length=255)
    commit_cards = StreamField([('card', Card())], use_json_field=True, min_num=3)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('description'),
                FieldPanel('image'),
                FieldPanel('Brand_images'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('who_are_we_heading'),
                FieldPanel('who_are_we_description'),
                FieldPanel('who_are_we_subheading'),
                FieldPanel('who_are_we_sub_description'),
                FieldPanel('who_are_we_images'),
                FieldPanel('who_are_we_points'),
            ],
            heading="Who Are We Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('commit_heading'),
                FieldPanel('commit_cards'),
            ],
            heading="Commit Section",
            classname="collapsed",
        ),
    ]

    def get_context(self, request, *args, **kwargs):
        today = timezone.now().date()
        context = super().get_context(request, args, kwargs)
        context['courses'] = CourseDetails.objects.filter(
            course_stating_date__gte=today
        ).order_by('course_stating_date')[:2]
        context['works'] = Alumni.objects.first()
        context['workshops_listing'] = workshopListing.objects.first()
        context['workshops'] = WorkshopDetail.objects.filter(
            course_stating_date__gte=today
        ).order_by('course_stating_date')[:3]
        return context

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"


class Alumni(BasePage):
    student_works = StreamField([('work', StudentWork())], use_json_field=True, min_num=4)

    template = "alumni.html"
    subpage_types = []
    parent_page_types = ["Home"]
    max_count = 1

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('description'),
                FieldPanel('image'),
                FieldPanel('student_works'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
    ]

    class Meta:
        verbose_name = "Alumni"
        verbose_name_plural = "Alumni"


class WorkshopDetail(BasePage):
    template = "workshop-details-page.html"
    subpage_types = []
    parent_page_types = ["workshopListing"]

    course_mentor = CharField(_('Mentor Name'), max_length=255)
    course_mentor_profile = ForeignKey('wagtailimages.Image', on_delete=PROTECT, related_name='+')

    course_url = URLField(_('Course URL'), max_length=255)
    course_stating_date = DateField(_('Course Stating Date'))
    course_type = CharField(_('Course Type'), max_length=255)
    course_rating = CharField(_('Course Rating'), max_length=255)
    course_level = CharField(_('Course Level'), max_length=255)
    course_duration = CharField(_('Course Duration'), max_length=255)

    info_heading = RichTextField(_('Heading'), max_length=255)
    info_description = TextField(_('Description'), max_length=2000)
    info_main_image = ForeignKey('wagtailimages.Image', on_delete=PROTECT, related_name='+')
    info_sub_image = ForeignKey('wagtailimages.Image', on_delete=PROTECT, related_name='+')
    info_sub_value = StreamField([('value', keyValue())], use_json_field=True, min_num=2)

    from_heading = RichTextField(_('Heading'), max_length=255)
    key_highlight = StreamField([('work', KeyHighlight())], use_json_field=True, min_num=4)

    galley_heading = RichTextField(_('Heading'), max_length=255)
    galley_images = StreamField([('image', ImageChooserBlock())], use_json_field=True, min_num=6, max_num=6)

    reviews_heading = RichTextField(_('Heading'), max_length=255)
    testimonials = StreamField([('testimonial', Testimonial())], use_json_field=True, null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('description'),
                FieldPanel('image'),
                FieldPanel('course_url'),
                FieldPanel('course_mentor'),
                FieldPanel('course_mentor_profile'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('course_stating_date'),
                FieldPanel('course_type'),
                FieldPanel('course_rating'),
                FieldPanel('course_level'),
                FieldPanel('course_duration'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('info_heading'),
                FieldPanel('info_description'),
                FieldPanel('info_main_image'),
                FieldPanel('info_sub_image'),
                FieldPanel('info_sub_value'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('from_heading'),
                FieldPanel('key_highlight'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('galley_heading'),
                FieldPanel('galley_images'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('reviews_heading'),
                FieldPanel('testimonials'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(WorkshopDetail, self).get_context(request, *args, **kwargs)
        context['home_page'] = Home.objects.first()
        context['listing_page'] = workshopListing.objects.first()
        return context

    class Meta:
        verbose_name = "Workshop Detail"
        verbose_name_plural = "Workshop Details"


class workshopListing(BasePage):
    template = "workshop-listing.html"

    subpage_types = ['WorkshopDetail']
    parent_page_types = ["Home"]
    max_count = 1

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('description'),
                FieldPanel('image'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(workshopListing, self).get_context(request, *args, **kwargs)
        context['detail'] = WorkshopDetail.objects.live().order_by('-course_stating_date')
        return context

    class Meta:
        verbose_name = "Workshop Listing"
        verbose_name_plural = "Workshop Listing"


class About(BasePage):
    template = "about.html"
    max_count = 1
    subpage_types = []
    parent_page_types = ["Home"]

    mission_heading = RichTextField(_('Heading'), max_length=255)
    mission_description = TextField(_('Description'), max_length=2000)
    since_experience = PositiveSmallIntegerField(_('Since Experience'), default=0)

    evolution_heading = RichTextField(_('Heading'), max_length=255)
    evolution_image = ForeignKey('wagtailimages.Image', on_delete=PROTECT, related_name='+')
    evolution_points = StreamField([('point', EvolutionPoints())], use_json_field=True, min_num=3)

    founders_heading = RichTextField(_('Heading'), max_length=255)
    founders_sub_heading = RichTextField(_('Heading'), max_length=255)
    founders_description = TextField(_('Description'), max_length=2000)
    founder_image = ForeignKey('wagtailimages.Image', on_delete=PROTECT, related_name='+')

    brand_heading = RichTextField(_('Heading'), max_length=255)
    brand_description = TextField(_('Description'), max_length=2000)
    brand_image = StreamField([('image', ImageChooserBlock())], use_json_field=True, min_num=3)

    article_heading = RichTextField(_('Heading'), max_length=255)
    article_description = TextField(_('Description'), max_length=2000)
    articles = StreamField([('article', Article())], use_json_field=True, null=True, blank=True)

    who_are_we_heading = RichTextField(_('Heading'), max_length=255)
    who_are_we_images = StreamField([('image', ImageChooserBlock())], use_json_field=True, min_num=3)
    who_are_we_points = StreamField([('point', WhoAreWePoints())], use_json_field=True, min_num=3)

    galley_heading = RichTextField(_('Heading'), max_length=255)
    galley_images = StreamField([('image', ImageChooserBlock())], use_json_field=True, min_num=6, max_num=6)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('description'),
                FieldPanel('image'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('mission_heading'),
                FieldPanel('mission_description'),
                FieldPanel('since_experience'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('evolution_heading'),
                FieldPanel('evolution_image'),
                FieldPanel('evolution_points'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('founders_heading'),
                FieldPanel('founders_sub_heading'),
                FieldPanel('founders_description'),
                FieldPanel('founder_image'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('brand_heading'),
                FieldPanel('brand_description'),
                FieldPanel('brand_image'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('article_heading'),
                FieldPanel('article_description'),
                FieldPanel('articles'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('who_are_we_heading'),
                # FieldPanel('who_are_we_images'),
                FieldPanel('who_are_we_points'),
            ],
            heading="Who Are We Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('galley_heading'),
                FieldPanel('galley_images'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
    ]

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"


class CourseListing(BasePage):
    template = "course-listing.html"
    subpage_types = ['CourseDetails']
    parent_page_types = ["Home"]
    max_count = 1

    galley_heading = RichTextField(_('Heading'), max_length=255)
    galley_images = StreamField([('image', ImageChooserBlock())], use_json_field=True, min_num=6, max_num=6)


    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('description'),
                FieldPanel('image'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('galley_heading'),
                FieldPanel('galley_images'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(CourseListing, self).get_context(request, *args, **kwargs)
        context['cards'] = CourseDetails.objects.live().order_by('-course_stating_date')
        return context

    class Meta:
        verbose_name = "Course Listing"
        verbose_name_plural = "Course Listing"


class CourseDetails(BasePage):
    template = "course-details.html"
    subpage_types = []
    parent_page_types = ["CourseListing"]

    course_url = URLField(_('Course URL'), max_length=255)
    course_stating_date = DateField(_('Course Stating Date'))
    course_type = CharField(_('Course Type'), max_length=255)
    course_rating = CharField(_('Course Rating'), max_length=255)
    course_level = CharField(_('Course Level'), max_length=255)
    course_duration = CharField(_('Course Duration'), max_length=255)

    points = StreamField([('point', blocks.TextBlock())], use_json_field=True, min_num=3)
    key_image = ForeignKey('wagtailimages.Image', on_delete=PROTECT, related_name='+')

    brand_images = StreamField([('image', ImageChooserBlock())], use_json_field=True, min_num=3)

    from_heading = RichTextField(_('Heading'), max_length=255)
    key_highlight = StreamField([('work', KeyHighlight())], use_json_field=True, min_num=4)

    certificate_heading = RichTextField(_('Heading'), max_length=255)
    certificate_description = TextField(_('Description'), max_length=2000)
    certificate_image = ForeignKey('wagtailimages.Image', on_delete=PROTECT, related_name='+')
    certificate_icons = StreamField([('icon', ImageChooserBlock())], use_json_field=True, min_num=3)

    mentor_name = CharField(_('Mentor'), max_length=255)
    mentor_description = TextField(_('Description'), max_length=2000)
    mentor_image = ForeignKey('wagtailimages.Image', on_delete=PROTECT, related_name='+')
    mentor_instagram = URLField(_('Instagram URL'), max_length=255, blank=True, null=True)
    mentor_linkedin = URLField(_('Linkedin URL'), max_length=255, blank=True, null=True)

    breakdown_heading = RichTextField(_('Heading'), max_length=255)
    breakdown_description = TextField(_('Description'), max_length=2000)
    breakdown_images = StreamField([('image', ImageChooserBlock())], use_json_field=True, min_num=3)
    breakdown_points = StreamField([('point', BreakdownPoint())], use_json_field=True, min_num=3)

    testimonial_heading = RichTextField(_('Heading'), max_length=255)
    testimonials = StreamField([('testimonial', Testimonial())], use_json_field=True, min_num=3)

    faqs = StreamField([('faq', FAQ())], use_json_field=True, min_num=3)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('description'),
                FieldPanel('image'),
                FieldPanel('course_url'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('course_stating_date'),
                FieldPanel('course_type'),
                FieldPanel('course_rating'),
                FieldPanel('course_level'),
                FieldPanel('course_duration'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('points'),
                FieldPanel('key_image'),
                FieldPanel('brand_images'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('from_heading'),
                FieldPanel('key_highlight'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('certificate_heading'),
                FieldPanel('certificate_description'),
                FieldPanel('certificate_image'),
                FieldPanel('certificate_icons'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('mentor_name'),
                FieldPanel('mentor_description'),
                FieldPanel('mentor_image'),
                FieldPanel('mentor_instagram'),
                FieldPanel('mentor_linkedin'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('breakdown_heading'),
                FieldPanel('breakdown_description'),
                FieldPanel('breakdown_images'),
                FieldPanel('breakdown_points'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('testimonial_heading'),
                FieldPanel('testimonials'),
                FieldPanel('faqs'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(CourseDetails, self).get_context(request, *args, **kwargs)
        context['home_page'] = Home.objects.first()
        context['listing_page'] = CourseListing.objects.first()
        return context

    class Meta:
        verbose_name = "Course Details"
        verbose_name_plural = "Course Details"


class Contact(BaseModel):
    name = CharField(_('First Name'), max_length=255)
    email = EmailField(_('Email'))
    phone = CharField(_('Phone Number'), max_length=255)
    msg = TextField(_('Message'), max_length=5000)

    def __str__(self):
        return f'{self.name}'


class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(
            *args, **kwargs,
        )

        for field in self.errors:
            if not field == '__all__':
                self.fields[field].widget.attrs['class'] = self.fields[field].widget.attrs.get('class',
                                                                                               '') + ' is-invalid'

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'msg']

        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone Number',
            'msg': 'Message',
        }

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Your Name', "data-py": "m", "data-px": "l", "class": "input"}),
            'email': EmailInput(
                attrs={'placeholder': 'Email Address', "data-py": "m", "data-px": "l", "class": "input"}),
            'phone': TextInput(attrs={'placeholder': 'Phone Number', "data-py": "m", "data-px": "l", "class": "input"}),
            'msg': Textarea(attrs={'placeholder': 'Anything you’d like to tell us?', "data-px": "l", "data-py": "m",
                                   "class": "input"}),
        }


class ContactUs(Page):
    max_count = 1
    subpage_types = []
    parent_page_types = ["Home"]
    template = "contact-us.html"
    email = EmailField(_('Email Address'), max_length=255)
    phone_number = CharField(_('Phone Number'), max_length=255)
    location = CharField(_('Location'), max_length=255)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('email'),
                FieldPanel('phone_number'),
                FieldPanel('location'),
            ],
            heading="Main Section",
            classname="collapsed",
        ),
    ]

    def serve(self, request, *args, **kwargs):
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                message_data = dict(
                    message=f'We\'ve received your response and we will get back to you soon.',
                    title="Thank You!"
                )
                Toast.success(request, message_data)
                return redirect(self.url)
            message_data = dict(
                message=f'something went wrong.',
                title="error"
            )
            Toast.error(request, message_data)
        return super().serve(request, *args, **kwargs)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        if request.method == "POST":
            context["form"] = ContactForm(request.POST)
        else:
            context["form"] = ContactForm()
        return context

from modeltranslation.translator import register, TranslationOptions
from .models import AboutUs, PortFolio, VideoModel


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(PortFolio)
class PortFolioTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(VideoModel)
class VideoModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

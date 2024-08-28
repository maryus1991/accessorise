from django.contrib import admin

from .models import Contact_us, SiteSetting, Footer_Link_my_account, Footer_Link_info, InstaFeed, FooterFeatures, \
    About_us, About_Team, About_Features, FAQS

# Register your models here.
admin.site.register(Contact_us)
admin.site.register(SiteSetting)
admin.site.register(Footer_Link_my_account)
admin.site.register(Footer_Link_info)
admin.site.register(InstaFeed)
admin.site.register(FooterFeatures)
admin.site.register(About_us)
admin.site.register(About_Team)
admin.site.register(About_Features)
admin.site.register(FAQS)

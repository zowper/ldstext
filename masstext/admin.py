from django.contrib import admin
from masstext.models import Stake
from masstext.models import Ward
from masstext.models import Calling
from masstext.models import Member
from masstext.models import Group
from masstext.models import Thread
from masstext.models import OutboundMessage
from masstext.models import InboundMessage

admin.site.register(Stake)
admin.site.register(Ward)
admin.site.register(Calling)
admin.site.register(Member)
admin.site.register(Group)
admin.site.register(Thread)
admin.site.register(OutboundMessage)
admin.site.register(InboundMessage)
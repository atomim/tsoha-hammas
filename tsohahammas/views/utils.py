
class TitleMixin(object):
	def get_context_data(self, **kwargs):
		context = super(TitleMixin, self).get_context_data(**kwargs)
		context.update({'title': self.title})
		return context
class ExtraContextMixin(object):
	def get_context_data(self, **kwargs):
		context = super(TitleMixin, self).get_context_data(**kwargs)
		context.update(self.extra_context)
		return context

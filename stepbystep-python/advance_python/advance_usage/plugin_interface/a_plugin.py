from advance_python.advance_usage.plugin_interface.macro_sample import Macro

__author__ = 'patrick'


@Macro.register('RecentChanges')
class RecentChangeMacro(Macro):
    def render(self):
        return 'render all changes'
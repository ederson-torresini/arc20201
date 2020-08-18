from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class HelloSkill(Skill):
    @match_regex(r'hi', case_sensitive=False)
    async def hello(self, message):
        await message.respond('Hello, ' + message.user)

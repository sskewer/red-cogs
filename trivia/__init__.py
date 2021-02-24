from redbot.core.bot import Red

from .trivia import trivia

async def setup(bot: Red):
    quiz = trivia(bot)
    bot.add_cog(quiz)
    await quiz.checker()

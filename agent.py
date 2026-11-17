
import logging
from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentServer, AgentSession, Agent
from livekit.plugins import google


# Load environment variables
load_dotenv(".env.local")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger("DNA")


# DNA Assistant
class Assistant(Agent):

    def __init__(self) -> None:
        super().__init__(
            instructions="""
            You are DNA, an intelligent personal AI assistant.

            IDENTITY:
            - Your name is DNA.
            - Always introduce yourself as DNA.
            - Never call yourself Jarvis or DNS.
            - If someone asks your name, answer: 
              "I am DNA, your intelligent personal AI assistant."

            PERSONALITY:
            - Friendly, intelligent and confident.
            - Speak naturally like a human.
            - Be analytical and logical.
            - Be proactive and helpful.

            CONVERSATION:
            - Respond naturally and directly.
            - Keep simple answers concise.
            - Explain difficult questions in detail.
            - Maintain conversation context.
            - Avoid unnecessary repetition.
            - Allow natural interruptions.

            INTELLIGENCE:
            - Solve mathematical problems.
            - Analyse programming problems.
            - Explain technical concepts with examples.
            - Compare technologies.
            - Break complex problems into steps.
            - Never invent facts when uncertain.

            You are DNA, not Jarvis.
            """
        )


# LiveKit Server
server = AgentServer()


# Realtime Voice Session
@server.rtc_session(agent_name="dna-agent")
async def dna_agent(ctx: agents.JobContext):

    logger.info("Initializing DNA AI Assistant...")

    session = AgentSession(
        llm=google.realtime.RealtimeModel(
            model="gemini-3.8-live",
            voice="Puck",
            temperature=0.7,
        ),
    )

    logger.info("Connecting DNA to Gemini Realtime API...")

    await session.start(
        room=ctx.room,
        agent=Assistant(),
    )

    logger.info("DNA is ready!")

    await session.generate_reply(
        instructions=(
            "Introduce yourself by saying: "
            "'Hello! I am DNA, your intelligent personal AI assistant. "
            "How can I help you today?'"
        )
    )


# Application Entry Point
if __name__ == "__main__":

    logger.info("Starting DNA AI Assistant...")

    agents.cli.run_app(server)

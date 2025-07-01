from core.agent_core import AIAgent

if __name__ == "__main__":
    agent = AIAgent()
    agent.boot()
    while agent.active:
        agent.run_cycle()
from . import python_agent, agent

agent.AgentFactory.register_agent('run_python', python_agent.run_python)
agent.AgentFactory.register_agent('merge_code', python_agent.merge_code)

import os

from . import agent, python_agent, shell_agent

# python agent
agent.AgentFactory.register_agent('run_python', python_agent.run_python)
agent.AgentFactory.register_agent('merge_code', python_agent.merge_code)
agent.AgentFactory.register_agent('create_dir', python_agent.create_dir)
agent.AgentFactory.register_agent('write_file', python_agent.write_file)
agent.AgentFactory.register_agent('append_file', python_agent.append_file)

# shell agent
if os.system() == 'windows':
    agent.AgentFactory.register_agent('windows_shell_agent', shell_agent.windows_shell_agent)
elif os.system() == 'linux':
    agent.AgentFactory.register_agent('shell_shell_agent', shell_agent.windows_shell_agent)

# web_search


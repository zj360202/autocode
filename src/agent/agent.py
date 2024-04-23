# """
# 执行plan，并将plan中的tools提取处理，调用对应的tools
# """
# import importlib
# import inspect
# from typing import Any
#
# from logs.logger import logger
#
#
# # Unique identifier for auto-gpt commands
# AUTO_GPT_COMMAND_IDENTIFIER = "auto_gpt_command"
#
#
# class ToolRegistry:
#     """
#     The ToolRegistry class is a manager for a collection of Tool objects.
#     It allows the registration, modification, and retrieval of Tool objects,
#     as well as the scanning and loading of tool plugins from a specified
#     directory.
#     """
#
#     tools: dict[str, Tool]
#     tools_aliases: dict[str, Tool]
#
#     def __init__(self):
#         self.tools = {}
#         self.tools_aliases = {}
#
#     def __contains__(self, tool_name: str):
#         return tool_name in self.tools or tool_name in self.tools_aliases
#
#     def _import_module(self, module_name: str) -> Any:
#         return importlib.import_module(module_name)
#
#     def _reload_module(self, module: Any) -> Any:
#         return importlib.reload(module)
#
#     def register(self, tool: Tool) -> None:
#         if tool.name in self.tools:
#             logger.warn(
#                 f"Tool '{tool.name}' already registered and will be overwritten!"
#             )
#         self.tools[tool.name] = tool
#
#         if tool.name in self.tools_aliases:
#             logger.warn(
#                 f"Tool '{tool.name}' will overwrite alias with the same name of "
#                 f"'{self.tools_aliases[tool.name]}'!"
#             )
#         for alias in tool.aliases:
#             self.tools_aliases[alias] = tool
#
#     def unregister(self, tool: Tool) -> None:
#         if tool.name in self.tools:
#             del self.tools[tool.name]
#             for alias in tool.aliases:
#                 del self.tools_aliases[alias]
#         else:
#             raise KeyError(f"Tool '{tool.name}' not found in registry.")
#
#     def reload_tools(self) -> None:
#         """Reloads all loaded tool plugins."""
#         for tool_name in self.tools:
#             tool = self.tools[tool_name]
#             module = self._import_module(tool.__module__)
#             reloaded_module = self._reload_module(module)
#             if hasattr(reloaded_module, "register"):
#                 reloaded_module.register(self)
#
#     def get_tool(self, name: str) -> Tool | None:
#         if name in self.tools:
#             return self.tools[name]
#
#         if name in self.tools_aliases:
#             return self.tools_aliases[name]
#
#     def call(self, tool_name: str, **kwargs) -> Any:
#         if tool := self.get_tool(tool_name):
#             return tool(**kwargs)
#         raise KeyError(f"Tool '{tool_name}' not found in registry")
#
#     def tool_prompt(self) -> str:
#         """
#         Returns a string representation of all registered `Tool` objects for use in a prompt
#         """
#         tools_list = [
#             f"{idx + 1}. {str(tool)}" for idx, tool in enumerate(self.tools.values())
#         ]
#         return "\n".join(tools_list)
#
#     def import_tools(self, module_name: str) -> None:
#         """
#         Imports the specified Python module containing tool plugins.
#
#         This method imports the associated module and registers any functions or
#         classes that are decorated with the `AUTO_GPT_TOOL_IDENTIFIER` attribute
#         as `Tool` objects. The registered `Tool` objects are then added to the
#         `tools` dictionary of the `ToolRegistry` object.
#
#         Args:
#             module_name (str): The name of the module to import for tool plugins.
#         """
#
#         module = importlib.import_module(module_name)
#
#         for attr_name in dir(module):
#             attr = getattr(module, attr_name)
#             # Register decorated functions
#             if hasattr(attr, AUTO_GPT_COMMAND_IDENTIFIER) and getattr(
#                 attr, AUTO_GPT_COMMAND_IDENTIFIER
#             ):
#                 self.register(attr.tool)
#             # Register tool classes
#             elif (
#                 inspect.isclass(attr) and issubclass(attr, Tool) and attr != Tool
#             ):
#                 tool_instance = attr()
#                 self.register(tool_instance)
#
#
# class Agent:
#
#     def extract_tool(self):
#         pass
#
#     def execute_tool(
#             self,
#             tool_name: str,
#             arguments: dict[str, str]):
#         pass
#
#     def run(self):
#         """
#         判定使用哪个模型
#         调用对应模型(包含api_key有效性判定，读取配置，参数封装，请求返回)
#         已经返回结果，调用对应的应用(多个应用执行列表)
#         以此执行完成应用
#         通过应用结果，判定流程是否结束
#         如果结束，判定结果是否理想(判定结果是否可以再次调用model，通过模型打分，判定结果是否合格)
#         如果不合理，将结果和问题，补充优化prompt(问模型提供改善意见)，再次循环
#         上述情况一，是模型可以一次性给出全流程解决方案
#         情况二，是当前问题的每一个都依赖于上一步的结果，具体判定标准(是否是依赖问题)待定
#         """
#         # 判定使用哪个模型
#
#         # 调用对应模型(包含api_key有效性判定，读取配置，参数封装，请求返回)
#
#         # 已经返回结果，调用对应的应用(多个应用执行列表)
#
#         # 以此执行完成应用
#
#         # 通过应用结果，判定流程是否结束
#
#         # 如果结束，判定结果是否理想(判定结果是否可以再次调用model，通过模型打分，判定结果是否合格)
#
#         # 如果不合理，将结果和问题，补充优化prompt(问模型提供改善意见)，再次循环
#
#         # 上述情况一，是模型可以一次性给出全流程解决方案
#
#         # 情况二，是当前问题的每一个都依赖于上一步的结果，具体判定标准(是否是依赖问题)待定
#
#

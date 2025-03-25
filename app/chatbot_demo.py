import asyncio
import uuid
from typing import List, Dict, Any
from laowu_npc001 import laowu_npc, npc001, Runner, NPCContext, Target
from agents import Agent, MessageOutputItem, ToolCallItem, ToolCallOutputItem, ItemHelpers


class ChatHistory:
    def __init__(self):
        self.messages: List[Dict[str, Any]] = []

    def add_message(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})

    def to_input_list(self) -> List[Dict[str, Any]]:
        return self.messages.copy()


input_context = {}


async def chat_with_laowu():
    print("欢迎来到与老五的对话！输入 'quit' 退出对话。")
    print("老五: 您好！我是老五，京奉铁路的茶房。有什么我可以帮您的吗？")

    # Initialize conversation tracking
    conversation_id = uuid.uuid4().hex[:16]
    chat_history = ChatHistory()
    input_context['default'] = chat_history
    current_agent: Agent[NPCContext] = laowu_npc

    def get_new_chathistory(input: str):
        _1, _2 = input.split('[system: change target]')
        # reset chat history update the npc001,
        if str(_2).strip() not in input_context:
            npc001.target = Target(_2, [])
            if str(_2).strip() == '张三':
                npc001.target.appearance = ["军大衣", "军帽"]
            elif str(_2).strip() == '李四':
                npc001.target.appearance = ["军大衣", "军帽", "警棍"]
            else:
                npc001.target.appearance = ["衬衫", "工装裤"]
        return input_context.get(str(_2).strip(), ChatHistory())

    while True:
        user_input = input("\n您: ").strip()

        if user_input.lower() == 'quit':
            print("\n老五: 谢谢您的光临，下次再见！")
            break

        if '[system: change target]' in user_input:
            chat_history = get_new_chathistory(user_input)
            continue

        # Add user message to history
        chat_history.add_message("user", user_input)

        # Process the user input and get NPC's response
        result = await Runner.run(
            current_agent,
            chat_history.to_input_list(),
            context=npc001,
        )

        # Handle different types of output items
        for new_item in result.new_items:
            if isinstance(new_item, MessageOutputItem):
                print(f"\n{current_agent.name}: {ItemHelpers.text_message_output(new_item)}")
            elif isinstance(new_item, ToolCallItem):
                print(f"\n老五: [正在处理您的请求...]")
            elif isinstance(new_item, ToolCallOutputItem):
                print(f"\n老五: [处理结果: {new_item.output}]")

        for item in result.to_input_list():
            if item.get('type', 'model') == 'function_call':
                continue
            elif item.get('type', 'model') == 'function_call_output':
                chat_history.add_message('assistant', f"({current_agent.name}内心的想法：" + f"{item['output']})")
            else:
                chat_history.add_message(item["role"], item["content"])
        current_agent = result.last_agent


def main():
    asyncio.run(chat_with_laowu())


if __name__ == "__main__":
    main()

# [system: change target] 张三
# [game event type: stranger; threaten: false]
# 你知道我是谁吗？
# 你来描述一下我穿的衣服
# [system: change target] 李四
# [game event type: stranger; threaten: true]
# [system: change target] 王五
# 我叫什么名字？
# 我现在穿的什么衣服？

# TODO: chat with multiple people
# TODO: chat history length
# TODO: lao wu workflow

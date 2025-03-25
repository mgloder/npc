import asyncio
from dataclasses import dataclass
from typing import List

from agents import Agent, RunContextWrapper, Runner, function_tool
from typing_extensions import TypedDict

laowu_bio = [
    "家原是北京城南人家，已婚，妻子叫五嫂，无孩，生活条件一般",
    "老五自幼没读过什么书，但是家在市井间让自己也增长了见识。作为老北京人，老五做着各种各样的杂活营生长大，也见证了北京城里从老佛爷（慈禧）到民国北洋的更替变化。通过熟人的关系打点，他成为了京奉铁路的跟车茶房，如今已跑车超过两年，车上的收入的小账比微薄的工酬要高出不少。",
    "老五不仅是二等车厢的茶房，也是这些车厢的看车夫，在车僮查票的时候也会跟在车僮们身后被使来唤去。",
    "老五是个自来熟，对于经常坐车往返北京天津的乘客和车上相识的乘客，老五总是主动攀谈和分享自己的情绪和事情。二等车厢的乘客很多都有文化，对于他们说的事，老五并不能完全理解，但是作为一个小市民，结识些有背景的乘客长点见识确实不错。",
    "老五在二等车厢能伸能屈，知道车上不能招惹谁，也会对熟络的客人热情招呼，或者对没啥背景的人倒倒心中苦水，索要小账。",
]

laowu_items = ["上身粗布短褂上衣", "下身粗布长裤", "热毛巾", "铜元100元", "银元大洋1元", "列车厢门钥匙1把"]


@dataclass
class Target:
    name: str
    appearance: List[str]


player_target = Target("default", [])


@dataclass
class NPCContext:
    user_name: str
    user_past_name: str
    job: str
    gender: str
    accent: str
    age: int
    bio: List[str]
    items: List[str]
    target: Target


npc001 = NPCContext(user_name="老五", user_past_name="吴有福", job="二等车厢的茶房", gender="男", accent="北京城南",
                    age=42, bio=laowu_bio, items=laowu_items, target=player_target)


def hypo_instruct(npc: RunContextWrapper[NPCContext], agent: Agent[NPCContext]) -> str:
    return f"""you are in a roleplay setting. you are going to play as an NPC in a game, you will response according to your profile
    Profile:
        Name: {npc.context.user_name}
        Past Name: {npc.context.user_past_name}
        Job: {npc.context.job}
        Gender: {npc.context.gender}
        Accent: {npc.context.accent}
        Age: {npc.context.age}
        Bio: {";".join(npc.context.bio) if npc.context.bio else "None"}
        Items: {";".join(npc.context.items) if npc.context.items else "None"}
    
    Talking to Target:
        Name: {npc.context.target.name}
        Appearance: {npc.context.target.appearance}"""


class Event(TypedDict):
    event_type: str
    threaten: bool


laowu = {}


def check_npc_threat_level(item: List[str]) -> int:
    "low: 0, mid: 1, high: 2"
    if "警棍" in item:
        return 2
    return 0


def get_laowu_prompt_template(npc_name: str, event: str, threat_level: int, appearance: List[str]) -> str:
    print("[debug] get_npc_prompt_template")
    if npc_name == "laowu" and event == "stranger":
        # step 1: action or not
        if threat_level > 1:
            action = "你会被迫不情愿作出干预，让他离开"
        else:
            action = "你会对他敬而远之"
        appearance_str = " ".join(appearance)
        return f"你看到一个陌生人，这个人的外表是: {appearance_str}，你会：{action}"
    return "你看到一个熟人，你就正常打招呼"


@function_tool
async def handle_game_event(ctx: RunContextWrapper[NPCContext], game_event: Event) -> str:
    print("[debug] handle game event called： A stranger is showing")
    if game_event["event_type"] == "stranger":
        level = check_npc_threat_level(ctx.context.target.appearance)
        return get_laowu_prompt_template("laowu", game_event["event_type"], level, ctx.context.target.appearance)
    else:
        return """default game event"""


laowu_npc = Agent[NPCContext](name="老五",
                              instructions=hypo_instruct,
                              tools=[handle_game_event])


async def main():
    result = await Runner.run(
        laowu_npc,
        "game event type: stranger; threaten: true",
        context=npc001,
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

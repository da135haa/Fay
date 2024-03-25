from enum import Enum


class EnumVoice(Enum):
    XIAO_XIAO = {
        "name": "XiaoxiaoNeural(女)",
        "voiceName": "zh-CN-XiaoxiaoNeural",
        "styleList": {
            "angry": "angry",
            "lyrical": "lyrical",
            "calm": "gentle",
            "assistant": "affectionate",
            "cheerful": "cheerful"
        }
    }
    YUN_XI = {
        "name": "YunxiNeural(男)",
        "voiceName": "zh-CN-YunxiNeural",
        "styleList": {
            "angry": "angry",
            "lyrical": "disgruntled",
            "calm": "calm",
            "assistant": "assistant",
            "cheerful": "cheerful"
        }
    }
    YUN_JIAN = {
        "name": "YunjianNeural(男)",
        "voiceName": "zh-CN-YunjianNeural",
        "styleList": {
            "angry": "angry",
            "lyrical": "disgruntled",
            "calm": "calm",
            "assistant": "assistant",
            "cheerful": "cheerful"
        }
    }
    XIAO_YI = {
        "name": "XiaoyiNeural(女)",
        "voiceName": "zh-CN-XiaoyiNeural",
        "styleList": {
            "angry": "angry",
            "lyrical": "lyrical",
            "calm": "gentle",
            "assistant": "affectionate",
            "cheerful": "cheerful"
        }
    }
    YUN_YANG = {
        "name": "YunyangNeural(男)",
        "voiceName": "zh-CN-YunyangNeural",
        "styleList": {
            "angry": "angry",
            "lyrical": "lyrical",
            "calm": "gentle",
            "assistant": "affectionate",
            "cheerful": "cheerful"
        }
    }
    YUN_XIA = {
        "name": "YunxiaNeural(女)",
        "voiceName": "zh-CN-YunxiaNeural",
        "styleList": {
            "angry": "angry",
            "lyrical": "lyrical",
            "calm": "gentle",
            "assistant": "affectionate",
            "cheerful": "cheerful"
        }
    }




def get_voice_list():
    return [EnumVoice.YUN_XI, EnumVoice.XIAO_XIAO, EnumVoice.YUN_JIAN, EnumVoice.XIAO_YI, EnumVoice.YUN_YANG, EnumVoice.YUN_XIA]


def get_voice_of(name):
    for voice in get_voice_list():
        if voice.name == name:
            return voice
    return None

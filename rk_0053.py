
from typing import Dict, List


FSCHAT_MODEL_WORKERS = {
    # 所有模型共用的默认配置，可在模型专项配置中进行覆盖。
    "default": {
        "host": '127.0.0.1',
        "port": 20002,
        "device": 'auto',
        # False,'vllm',使用的推理加速框架,使用vllm如果出现HuggingFace通信问题，参见doc/FAQ
        # vllm对一些模型支持还不成熟，暂时默认关闭
        "infer_turbo": False,

    },
    "chatglm3-6b": {
        "device": "cuda",
    },
    "Qwen1.5-0.5B-Chat": {
        "device": "cuda",
    },
    # 以下配置可以不用修改，在model_config中设置启动的模型
    "zhipu-api": {
        "port": 21001,
    },
    "minimax-api": {
        "port": 21002,
    }
}

MODEL_PATH = {
    "embed_model": {
        "ernie-tiny": "nghuyong/ernie-3.0-nano-zh",
        "ernie-base": "nghuyong/ernie-3.0-base-zh",
        "text2vec-base": "shibing624/text2vec-base-chinese",
        "text2vec": "GanymedeNil/text2vec-large-chinese",
        "text2vec-paraphrase": "shibing624/text2vec-base-chinese-paraphrase",

    },

    "llm_model": {
        "chatglm2-6b": "THUDM/chatglm2-6b",
        "chatglm2-6b-32k": "THUDM/chatglm2-6b-32k",
        "chatglm3-6b": "THUDM/chatglm3-6b",
        "chatglm3-6b-32k": "THUDM/chatglm3-6b-32k",

        "Orion-14B-Chat": "OrionStarAI/Orion-14B-Chat",
        "Orion-14B-Chat-Plugin": "OrionStarAI/Orion-14B-Chat-Plugin",
        "Orion-14B-LongChat": "OrionStarAI/Orion-14B-LongChat",

    },

    "reranker": {
        "bge-reranker-large": "BAAI/bge-reranker-large",
        "bge-reranker-base": "BAAI/bge-reranker-base",
    }
}

ONLINE_LLM_MODEL = {
    "openai-api": {
        "model_name": "gpt-4",
        "api_base_url": "https://api.openai.com/v1",
        "api_key": "",
        "openai_proxy": "",
    },

    # 智谱AI API,具体注册及api key获取请前往 http://open.bigmodel.cn
    "zhipu-api": {
        "api_key": "",
        "version": "glm-4",
        "provider": "ChatGLMWorker",
    },

    # 火山方舟 API，文档参考 https://www.volcengine.com/docs/82379
    "fangzhou-api": {
        "version": "", # 对应火山方舟的 endpoint_id
        "version_url": "",
        "api_key": "",
        "secret_key": "",
        "provider": "FangZhouWorker",
    },

    # 阿里云通义千问 API，文档参考 https://help.aliyun.com/zh/dashscope/developer-reference/api-details
    "qwen-api": {
        "version": "qwen-max",
        "api_key": "",
        "provider": "QwenWorker",
        "embed_model": "text-embedding-v1"  # embedding 模型名称
    },

    # 百川 API，申请方式请参考 https://www.baichuan-ai.com/home#api-enter
    "baichuan-api": {
        "version": "Baichuan2-53B",
        "api_key": "",
        "secret_key": "",
        "provider": "BaiChuanWorker",
    },

}

def list_config_llm_models() -> Dict[str, Dict]:
    '''
    get configured llm models with different types.
    return {config_type: {model_name: config}, ...}
    '''
    workers = FSCHAT_MODEL_WORKERS.copy()
    workers.pop("default", None)

    return {
        "local": MODEL_PATH["llm_model"].copy(),
        "online": ONLINE_LLM_MODEL.copy(),
        "worker": workers,
    }



list_config_llm_models = list_config_llm_models()
print(list_config_llm_models)




# def list_online_embed_models() -> List[str]:
#     from other.server import model_workers

#     ret = []
#     for k, v in list_config_llm_models()["online"].items():
#         if provider := v.get("provider"):
#             worker_class = getattr(model_workers, provider, None)
#             print(worker_class)
#             if worker_class is not None and worker_class.can_embedding():
#                 ret.append(k)
#     return ret


# ret = list_online_embed_models()
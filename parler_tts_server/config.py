import enum

from pydantic_settings import BaseSettings

SPEED = 1.0


# NOTE: commented out response formats don't work
class ResponseFormat(enum.StrEnum):
    MP3 = "mp3"
    # OPUS = "opus"
    # AAC = "aac"
    FLAC = "flac"
    WAV = "wav"
    # PCM = "pcm"


class Config(BaseSettings):
    log_level: str = "info"  # env: LOG_LEVEL
    torch_dtype: str = "torch.bfloat16" # env: TORCH_DTYPE
    model: str = "parler-tts/parler-tts-mini-expresso"  # env: MODEL
    compile_mode: str = "reduce-overhead" # env: COMPILE_MODE
    attn_implementation: str = "sdpa" # env: ATTN_IMPLEMENTATION
    max_stream_sec: int = 30 # env: MAX_STREAM_SEC
     

    max_models: int = 1  # env: MAX_MODELS
    lazy_load_model: bool = False  # env: LAZY_LOAD_MODEL
    voice: str = (
        "Thomas speaks moderately slowly in a sad tone with emphasis and high quality audio."  # env: VOICE
    )
    response_format: ResponseFormat = ResponseFormat.MP3  # env: RESPONSE_FORMAT


config = Config()

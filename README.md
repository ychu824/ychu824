### Yucheng Hu

Engineer working on **AI infrastructure**. I contribute to inference serving engines for omni-modal models (speech, audio and text), mostly scheduling, batching and GPU-side latency in **[SGLang-Omni](https://github.com/sgl-project/sglang-omni)** and **[vLLM-Omni](https://github.com/vllm-project/vllm-omni)**.

`inference serving` · `request scheduling & batching` · `GPU latency` · `distributed systems`

![Profile views](https://komarev.com/ghpvc/?username=ychu824&color=555&style=flat-square&label=profile+views)

---

### SGLang-Omni & vLLM-Omni

<sub>merged PRs: 11 · synced daily</sub>

<!-- PRS:START -->
**Performance**

- [Classify the flow DiT attention mask once per forward on FLASH_ATTN](https://github.com/vllm-project/vllm-omni/pull/9942) <sub>vLLM-Omni · CosyVoice3</sub>
- [Release the prefill-coalesce hold during decode under a draft](https://github.com/sgl-project/sglang-omni/pull/3938) <sub>SGLang-Omni · Qwen3-ASR</sub>
- [Evaluate the Qwen3 decoder's prefill one layer at a time](https://github.com/sgl-project/sglang-omni/pull/3414) <sub>SGLang-Omni</sub>
- [Read decode token ids through the pinned buffer and event](https://github.com/sgl-project/sglang-omni/pull/2625) <sub>SGLang-Omni · CosyVoice3</sub>

**Serving & realtime**

- [Preserve error codes for session admission and runtime failures](https://github.com/sgl-project/sglang-omni/pull/3231) <sub>SGLang-Omni</sub>
- [Close connections that never send session.update](https://github.com/sgl-project/sglang-omni/pull/2674) <sub>SGLang-Omni</sub>

**Correctness**

- [Coalesce concurrent CosyVoice3 reference conditioning](https://github.com/vllm-project/vllm-omni/pull/9632) <sub>vLLM-Omni</sub>

**Benchmarks & CI**

- [Retain failing TTS audio in weekly TTS steps](https://github.com/vllm-project/vllm-omni/pull/9786) <sub>vLLM-Omni</sub>
- [Retry in-session admission rejections in the duplex recorder (C2)](https://github.com/sgl-project/sglang-omni/pull/3038) <sub>SGLang-Omni</sub>
- [Stop overriding the model's generation-length contract](https://github.com/sgl-project/sglang-omni/pull/2299) <sub>SGLang-Omni · Fun-CosyVoice3</sub>

**Models & sampling**

- [Repetition-aware sampling on the CUDA path](https://github.com/sgl-project/sglang-omni/pull/2626) <sub>SGLang-Omni · Fun-CosyVoice3</sub>
<!-- PRS:END -->

---

### Projects

| Project | What it is |
|---|---|
| **[TokenTide](https://github.com/ychu824/TokenTide)** | A floating macOS meter for Claude plan limits and Claude Code token usage. Signed, notarized and self-updating. ![downloads](https://img.shields.io/github/downloads/ychu824/TokenTide/total?color=555&label=downloads&style=flat-square) |

### Background

- M.S., Carnegie Mellon University
- *Object Detection Based Handwriting Localization*, ICDAR 2021 Workshops

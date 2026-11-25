### Yucheng Hu

Distributed-systems engineer working toward **AI infrastructure**. At Microsoft I build multitenant job scheduling and orchestration for Azure Storage. Outside work I contribute to inference serving engines for omni-modal models, mostly scheduling, batching and GPU-side latency in **[SGLang-Omni](https://github.com/sgl-project/sglang-omni)** and **[vLLM-Omni](https://github.com/vllm-project/vllm-omni)**.

`inference serving` · `request scheduling & batching` · `GPU latency` · `multitenant systems`

---

### Selected contributions

| Project | Change | Area |
|---|---|---|
| **SGLang-Omni** | [Release the prefill-coalesce hold during decode under a draft (Qwen3-ASR)](https://github.com/sgl-project/sglang-omni/pull/3938) | scheduling |
| **SGLang-Omni** | [Evaluate the Qwen3 decoder's prefill one layer at a time](https://github.com/sgl-project/sglang-omni/pull/3414) | memory / perf |
| **SGLang-Omni** | [Read CosyVoice3 decode token ids through a pinned buffer and event](https://github.com/sgl-project/sglang-omni/pull/2625) | GPU latency |
| **vLLM-Omni** | [Classify the flow DiT attention mask once per forward on FLASH_ATTN (CosyVoice3)](https://github.com/vllm-project/vllm-omni/pull/9942) | GPU latency |
| **vLLM-Omni** | [Coalesce concurrent CosyVoice3 reference conditioning](https://github.com/vllm-project/vllm-omni/pull/9632) | batching |
| **SGLang-Omni** | [Preserve error codes for realtime session admission and runtime failures](https://github.com/sgl-project/sglang-omni/pull/3231) | serving / realtime |

<!-- MERGED:START -->
<details>
<summary>All merged upstream PRs (12)</summary>

| Repo | PR | Merged |
|---|---|---|
| `vllm-project/vllm-omni` | [\[CI/Build\] Retain failing TTS audio in weekly TTS steps](https://github.com/vllm-project/vllm-omni/pull/9786) | 2026-11-25 |
| `vllm-project/vllm-omni` | [\[Perf\]\[CosyVoice3\] Classify the flow DiT attention mask once per forward on FLASH_ATTN](https://github.com/vllm-project/vllm-omni/pull/9942) | 2026-11-20 |
| `sgl-project/sglang-omni` | [\[Perf\]\[Qwen3-ASR\] Release the prefill-coalesce hold during decode under a draft](https://github.com/sgl-project/sglang-omni/pull/3938) | 2026-11-14 |
| `sgl-project/sglang-omni` | [\[Benchmark\] Retry in-session admission rejections in the duplex recorder (C2)](https://github.com/sgl-project/sglang-omni/pull/3038) | 2026-11-08 |
| `sgl-project/sglang-omni` | [\[Perf\] Evaluate the Qwen3 decoder's prefill one layer at a time](https://github.com/sgl-project/sglang-omni/pull/3414) | 2026-11-04 |
| `vllm-project/vllm-omni` | [\[Bugfix\] Coalesce concurrent CosyVoice3 reference conditioning](https://github.com/vllm-project/vllm-omni/pull/9632) | 2026-11-01 |
| `sgl-project/sglang-omni` | [\[Realtime\] Preserve error codes for session admission and runtime failures](https://github.com/sgl-project/sglang-omni/pull/3231) | 2026-10-28 |
| `sgl-project/sglang-omni` | [\[Fun-CosyVoice3\] Repetition-aware sampling on the CUDA path](https://github.com/sgl-project/sglang-omni/pull/2626) | 2026-10-12 |
| `sgl-project/sglang-omni` | [\[Perf\]\[CosyVoice3\] Read decode token ids through the pinned buffer and event](https://github.com/sgl-project/sglang-omni/pull/2625) | 2026-10-12 |
| `sgl-project/sglang-omni` | [\[Realtime\] Close connections that never send session.update](https://github.com/sgl-project/sglang-omni/pull/2674) | 2026-10-12 |
| `sgl-project/sglang-omni` | [\[Benchmark\]\[Fun-CosyVoice3\] Stop overriding the model's generation-length contract](https://github.com/sgl-project/sglang-omni/pull/2299) | 2026-10-03 |
| `sgl-project/sglang-omni` | [\[Fix\] OmniTyper: withdraw the unkept copy promise, show preparation progress in Settings, point at where verbatim is set, stop Unload ASR orphaning the speech server](https://github.com/sgl-project/sglang-omni/pull/2261) | 2026-09-21 |

</details>
<!-- MERGED:END -->

<!-- OPEN:START -->
<details>
<summary>Open PRs · in review and work in progress (3)</summary>

| Repo | PR | Status |
|---|---|---|
| `sgl-project/sglang-omni` | [\[FireRedTTS3\] Encode concurrent reference clips in one batch on Base](https://github.com/sgl-project/sglang-omni/pull/4458) | draft |
| `vllm-project/vllm-omni` | [\[Bugfix\] Bound CosyVoice3 shared reference-conditioning waits](https://github.com/vllm-project/vllm-omni/pull/9783) | in review |
| `sgl-project/sglang-omni` | [\[Perf\] Evaluate the native Qwen3-ASR encoder in groups on long audio](https://github.com/sgl-project/sglang-omni/pull/3456) | in review |

</details>
<!-- OPEN:END -->

---

### Projects

| | |
|---|---|
| **[TokenTide](https://github.com/ychu824/TokenTide)** | A floating macOS meter for Claude plan limits and Claude Code token usage. Signed, notarized and self-updating. ![downloads](https://img.shields.io/github/downloads/ychu824/TokenTide/total?color=555&label=downloads&style=flat-square) |

### Background

- M.S., Carnegie Mellon University
- *Object Detection Based Handwriting Localization*, ICDAR 2021 Workshops

---

<sub>PR lists are synced daily by [a workflow](.github/workflows/sync-prs.yml).</sub>

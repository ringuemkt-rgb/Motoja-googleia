# Arquitetura

USER → API/CLI/UI → ROUTER → KB / DIAGNOSTIC / PRODUCT AUDIT → EVIDENCE PACK → DETERMINISTIC CORE + OPTIONAL LLM → RED TEAM → RESPONSE.

## Camadas

1. Canonical Knowledge: JSON/CSV/SQLite com status explícito.
2. Deterministic Core: relação, fitment, busca OEM, roteamento e diagnóstico funcionam sem IA.
3. LLM Adapter: recebe context packet e não pode sobrescrever baseline por memória.
4. Multimodal: Qwen3-VL, Grounding DINO, SAM2.1, PaddleOCR/Docling, OpenCV/ArUco e embeddings/Qdrant como adaptadores opcionais.
5. Digital Twin: medições, serviços, componentes instalados, observações, falhas e resultados.

Novo dado = CONFIRMED / PROVISIONAL / SUPERSEDED / UNKNOWN. Conflito nunca faz overwrite silencioso.

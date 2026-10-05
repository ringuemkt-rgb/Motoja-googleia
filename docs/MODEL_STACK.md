# Model & Tool Stack

O agente é capability-based, não preso a fornecedor.

- reasoning multimodal: Qwen3-VL-8B-Instruct ou VLM equivalente;
- grounding: IDEA-Research/GroundingDINO;
- segmentation: SAM2.1;
- OCR/document: PaddleOCR + Docling;
- geometry: OpenCV + ArUco/AprilTag; depth/3D apenas como apoio;
- retrieval: embeddings + Qdrant;
- orchestration: state machine determinística; PydanticAI/LangGraph opcionais;
- API: FastAPI.

## Perfil leve
Core determinístico local + RAG pequeno + VLM remoto quando autorizado.

## Perfil oficina
Celular envia foto; servidor devolve componentes, achados, confidence, fotos adicionais, medições e sequência de testes.

## Treinamento futuro
Só depois de dataset rotulado suficiente. Antes disso usar modelos fundacionais, grounding, segmentação e retrieval.

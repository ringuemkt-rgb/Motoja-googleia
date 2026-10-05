# Deployment

## 1. Local/offline
O core determinístico funciona sem LLM:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
xtz-agent search carburador
uvicorn xtz_agent.api:app --reload
```

## 2. LLM compatível
Configure:
```env
XTZ_LLM_BASE_URL=https://seu-endpoint
XTZ_LLM_API_KEY=...
XTZ_LLM_MODEL=...
```

O endpoint deve expor interface de chat-completions compatível. As regras OEM e os cálculos críticos continuam fora do LLM.

## 3. Docker
```bash
docker build -t xtz125k-agent .
docker run --rm -p 8000:8000 --env-file .env xtz125k-agent
```

## 4. RAG
Indexe knowledge/ mantendo os metadados de status.
Nunca achate CANONICAL, PROVISIONAL e SUPERSEDED na mesma verdade.
Qdrant é opcional; uma busca determinística local continua sendo fallback.

## 5. Vision
Adaptadores recomendados:
- VLM para raciocínio visual;
- GroundingDINO para grounding;
- SAM2.1 para segmentação;
- PaddleOCR/Docling para documentos;
- OpenCV + ArUco/AprilTag para medição assistida.

Medição visual não substitui paquímetro em encaixes críticos.

## 6. MOTOJÁ
O frontend existente deve chamar esta API no servidor. Nunca expor chave real de LLM no bundle web.

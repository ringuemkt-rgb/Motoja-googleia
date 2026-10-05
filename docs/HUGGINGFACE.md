# Hugging Face Integration

A arquitetura suporta Hub models e futuros Spaces/Jobs sem transformar Hugging Face em dependência obrigatória.

## Referências
- Qwen/Qwen3-VL-8B-Instruct — reasoning multimodal.
- facebook/sam2.1-hiera-small — segmentação / mask generation.

## Supply chain
Preferir safetensors, fixar revision/hash em produção, revisar model card/licença/arquivos, evitar remote code arbitrário e tratar pickle como artefato de maior risco.

HF Jobs pode futuramente executar batch inference, QA de dataset e fine-tuning; não é requisito para o agente funcionar.

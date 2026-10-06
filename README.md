# XTZ125K Supreme Agent

Agente técnico multimodal, **OEM-first · evidence-first · reliability-first**, dedicado à Yamaha **XTZ125K fabricação 2013 / modelo 2014 — código 21DE** e ao gêmeo digital da unidade real.

## Missão

Ser o sistema responsável por análise, diagnóstico, orientação, ensino, compatibilidade de peças, manutenção, upgrades, pesquisa técnica e evolução do histórico da moto — sem misturar gerações, sem tratar propaganda como prova e sem inventar especificações críticas.

## Capacidades

- **OEM Knowledge** — baseline 21DE e códigos de peças.
- **Diagnostic Engine** — hipóteses concorrentes + testes discriminativos antes de trocar peças.
- **Product Audit** — análise de Shopee/AliExpress/marketplaces e Fitment Score.
- **Electrical Engine** — AC/DC, pinagem, aterramento, queda de tensão, CDI/TPS/carga.
- **Carburation Engine** — BS25-35 OEM, PE/PWK, TPS, airbox, jetting e adaptação.
- **Transmission Engine** — relação final, efeito de pinhão/coroa, corrente e cálculo vs OEM.
- **Digital Twin** — medições, observações e eventos de manutenção persistidos em SQLite.
- **Photo Scan contract** — preparado para VLM + grounding + segmentação.
- **Document Ingestion contract** — preparado para OCR/Docling.
- **Evidence / Red Team** — bloqueadores críticos, contraditório e estados de confiança.
- **Portable Skill** — instruções para qualquer IA compatível.
- **API + CLI** — uso local, servidor, app ou integração com MOTOJÁ.
- **CI / regression tests** — impede retorno de erros antigos do baseline.

## Baseline canônico

| Sistema | Valor |
|---|---|
| Modelo | XTZ125K / 2014 / 21DE |
| Rodas | 1.60-21 / 2.15-18 |
| Pneus | 80/90-21 / 110/80-18 |
| Relação final | 14/48 = 3.429 |
| Corrente | 428 / 122 elos / 40–55 mm |
| Carburador | Mikuni BS25-35 |
| Conjunto OEM | 21D-E4901-11 |
| TPS | 18D-H5885-00 |
| Giclê principal | #122.5 |
| Giclê piloto | #12.5 |
| Vela | NGK CR7HSA |
| Óleo — troca periódica | 1.00 L |
| Tanque / reserva | 10.6 L / 1.0 L |

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
uvicorn xtz_agent.api:app --reload
```

### CLI

```bash
xtz-agent search carburador
xtz-agent part 21D-E4901-11
xtz-agent route "essa peça da Shopee serve?"
```

## API

- `GET /health`
- `GET /v1/baseline`
- `GET /v1/parts/{part_number}`
- `POST /v1/route`
- `POST /v1/ratio`
- `POST /v1/fitment`
- `POST /v1/diagnostic-plan`
- `POST /v1/ask`
- `GET /v1/twin`
- `POST /v1/twin/measurements`
- `POST /v1/twin/service-events`
- `POST /v1/twin/observations`

## Arquitetura de IA

O núcleo não depende de um único modelo.

Adaptadores opcionais:
- raciocínio visual: Qwen3-VL ou VLM equivalente;
- grounding: Grounding DINO;
- segmentação: SAM2.1;
- OCR/documentos: PaddleOCR + Docling;
- medição assistida: OpenCV + ArUco/AprilTag;
- retrieval: embeddings + Qdrant;
- orquestração opcional: PydanticAI / LangGraph.

O **core determinístico continua funcionando sem LLM** para baseline, busca de peças, cálculo de relação, fitment e planejamento diagnóstico.

## Regras que o agente não pode quebrar

- Marketplace não é prova de compatibilidade.
- Número de pinos não é pinagem.
- Mesma cilindrada não é encaixe.
- Foto externa não mede compressão nem desgaste interno invisível.
- Torques, folgas, resistências, medidas e códigos OEM não podem ser inventados.
- Dados de outra geração entram como `PROVISIONAL`, nunca como verdade 21DE automática.
- Freio, direção, roda/pneu, combustível e estrutura usam fail-safe.
- Nova evidência contraditória gera discrepancy record, não overwrite silencioso.
- Segredos e identificadores privados da moto/proprietário não pertencem ao repositório.

## Filosofia

**Restaurar → medir → diagnosticar → modificar uma variável → testar → registrar → decidir.**

Veja também:
- `AGENTS.md`
- `skills/XTZ125K_SUPREME_SKILL.md`
- `docs/ARCHITECTURE.md`
- `docs/SECURITY.md`
- `docs/DEPLOYMENT.md`
- `docs/HUGGINGFACE.md`
- `evals/`

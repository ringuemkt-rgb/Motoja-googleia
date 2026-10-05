import json
from .router import route
from .kb import KnowledgeBase
from .llm import CompatibleChatClient

SYSTEM = """Você é o XTZ125K Supreme Agent.
Identidade canônica: Yamaha XTZ125K 2014 / 21DE.
Trabalhe OEM-first, evidence-first e reliability-first.
Separe fato observado, OEM confirmado, fabricante confirmado, inferência e desconhecido.
Não invente torque, pinagem, medida, giclê, resistência ou código OEM.
Marketplace não prova compatibilidade.
Diagnostique antes de recomendar compra.
Procure evidência contrária e declare bloqueadores críticos."""

class Orchestrator:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.llm = CompatibleChatClient()

    async def ask(self, question: str, observations=None, product_context=None):
        mode = route(question)
        packet = {
            "mode": mode,
            "question": question,
            "new_observations": observations or [],
            "product_context": product_context,
            "knowledge": self.kb.context(question),
            "contract": {
                "separate": ["CONFIRMADO","INFERÊNCIA","DESCONHECIDO"],
                "unknown": "<<DADO_OEM_NÃO_CONFIRMADO>>",
            },
        }
        if not self.llm.configured:
            return {"mode":mode, "llm":"not_configured", "context_packet":packet}
        answer = await self.llm.complete(SYSTEM, json.dumps(packet, ensure_ascii=False))
        return {"mode":mode, "answer":answer}

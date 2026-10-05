from .domain import DiagnosticPlanRequest, DiagnosticTest

GENERIC = [
    DiagnosticTest(
        name="Inspeção visual dirigida",
        why="Encontrar falhas óbvias sem desmontagem.",
        safety=10, cost=10, invasiveness=10, discrimination=6,
    ),
    DiagnosticTest(
        name="Conexões, aterramentos e fixações",
        why="Muitas falhas intermitentes são de interface.",
        safety=10, cost=9, invasiveness=9, discrimination=7,
    ),
]

RULES = [
    (("não pega","partida","difícil pegar"),[
        DiagnosticTest(name="Tensão da bateria em repouso e durante partida",why="Separa alimentação fraca de ignição/combustível.",safety=9,cost=9,invasiveness=10,discrimination=8),
        DiagnosticTest(name="Presença e qualidade de centelha",why="Separa ignição de combustível/compressão.",safety=7,cost=8,invasiveness=8,discrimination=9),
        DiagnosticTest(name="Combustível chegando à cuba",why="Confirma alimentação antes de desmontar carburador.",safety=8,cost=10,invasiveness=9,discrimination=8),
    ]),
    (("falha","engasga","sem força","acelera"),[
        DiagnosticTest(name="Teste de entrada falsa de ar",why="Vedação ruim invalida acerto de giclê.",safety=8,cost=9,invasiveness=9,discrimination=9),
        DiagnosticTest(name="Filtro/airbox e respiros",why="Restrição ou vazamento altera mistura.",safety=10,cost=10,invasiveness=9,discrimination=7),
    ]),
    (("descarrega","bateria","carga"),[
        DiagnosticTest(name="Tensão em repouso e sob carga",why="Avalia alimentação básica.",safety=9,cost=9,invasiveness=10,discrimination=7),
        DiagnosticTest(name="Tensão de carga em rotações definidas",why="Separa bateria de geração/regulação.",safety=8,cost=9,invasiveness=9,discrimination=9),
        DiagnosticTest(name="Queda de tensão em terra e positivo",why="Detecta cabo/conector ruim.",safety=9,cost=9,invasiveness=9,discrimination=9),
    ]),
]

def _rank(test: DiagnosticTest) -> float:
    return test.safety*.30 + test.cost*.20 + test.invasiveness*.20 + test.discrimination*.30

def build_plan(req: DiagnosticPlanRequest) -> list[DiagnosticTest]:
    text = (req.symptom + " " + " ".join(req.observations)).lower()
    tests = list(GENERIC)
    for keys, items in RULES:
        if any(key in text for key in keys):
            tests.extend(items)
    unique = {test.name: test for test in tests}
    return sorted(unique.values(), key=_rank, reverse=True)

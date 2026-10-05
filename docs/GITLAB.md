# GitLab role

GitLab é tratado como mirror/CI/backup secundário do agente.

Estratégia:
1. GitHub = origem principal de engenharia.
2. GitLab = mirror de recuperação, CI alternativo e comparação de pipelines.
3. Hugging Face = modelos/datasets/Spaces e compute, não source-of-truth do baseline OEM.

Nunca permitir que uma cópia stale no mirror sobrescreva o branch canônico sem comparação de commit/revisão.

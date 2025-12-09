# Análise de Workloads: CPU e Memória

Este projeto tem como objetivo processar e analisar logs de uso de recursos (CPU e Memória) extraídos do Grafana. O fluxo inclui uma etapa de anonimização de dados sensíveis e o cálculo estatístico de métricas de performance dos Pods.

## Estrutura de Pastas

A organização do projeto segue a estrutura abaixo:

```text
.
├── README.md
├── anomizacao.py
├── calculoCPUMemoriaWorkloads.xlsx
├── data
│   ├── CPU Usage-data-original.csv
│   ├── CPU_anon.csv
│   ├── MEM_anon.csv
│   ├── Memory Usage-data-original.csv
│   └── mapping_pods.csv
├── tabela_final.csv
└── uso_memoria.ipynb
```

## Bibliotecas Necessárias

O projeto foi desenvolvido em Python e requer as seguintes bibliotecas para manipulação e cálculo de dados:

  * **pandas** (Manipulação de DataFrames)
  * **numpy** (Cálculos matemáticos)
  * *typing* (Tipagem padrão do Python)

Você pode instalar as dependências externas via pip:

```bash
pip install pandas numpy openpyxl
```

*(Nota: `openpyxl` é necessário para ler/escrever arquivos Excel como o .xlsx presente na raiz)*

### Imports utilizados nos scripts:

```python
import pandas as pd
from typing import Optional
import numpy as np
```

## Como Executar

O fluxo de execução é dividido em duas etapas: preparação (anonimização) e análise.

### 1\. Anonimização dos Dados (Opcional)

Por questões de confidencialidade e segurança, os nomes reais dos pods podem ser mascarados antes da análise.

  * **Script:** `anomizacao.py`
  * **Função:** Lê os arquivos originais na pasta `data/`, gera nomes genéricos para os serviços e salva os arquivos anonimizados (`*_anon.csv`) e um arquivo de mapeamento (`mapping_pods.csv`).
  * **Execução:**
    ```bash
    python anomizacao.py
    ```

### 2\. Análise de Recursos

A análise estatística e geração dos relatórios finais é feita através do Jupyter Notebook.

  * **Arquivo:** `uso_memoria.ipynb`
  * **Entrada:** Lê os arquivos CSV localizados na pasta `data/`.
  * **Como rodar:** Abra o notebook em seu ambiente Jupyter ou VS Code e execute as células sequencialmente.

## Resultados e Tabela de Saída

Ao final da execução do notebook, será gerada uma tabela consolidada (`tabela_final.csv` ou visualização no notebook) contendo as métricas calculadas.

As colunas são renomeadas para facilitar a interpretação, conforme o mapeamento abaixo:

| Coluna Original (Estatística) | Coluna na Tabela Final | Descrição |
| :--- | :--- | :--- |
| `count` | **Registros** | Quantidade de amostras coletadas |
| `min` | **CPUMin** | Mínimo de CPU registrado |
| `max` | **CPUMax** | Pico máximo de CPU registrado |
| `mean` | **CPUMédia** | Média de consumo de CPU |
| `mode` | **CPUModa** | Valor de CPU mais frequente |
| `p95` | **CPUP95** | Percentil 95 (95% dos dados estão abaixo deste valor) |
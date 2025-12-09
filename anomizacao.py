import pandas as pd
import csv

# ====== Caminhos fixos solicitados ======
cpu_path = "data/CPU Usage-data-original.csv"
mem_path = "data/Memory Usage-data-original.csv"

cpu_out = "data/CPU_anon.csv"
mem_out = "data/MEM_anon.csv"

mapping_out = "data/mapping_pods.csv"
# ========================================


def is_preserve(col):
    return col.strip().lower() in ("time", "max capacity")


print("Lendo arquivos...")
df_cpu = pd.read_csv(cpu_path)
df_mem = pd.read_csv(mem_path)

# Coletar todos os headers que devem ser anonimizados (exceto os preservados)
all_headers = []

for df in (df_cpu, df_mem):
    for col in df.columns:
        if not is_preserve(col) and col not in all_headers:
            all_headers.append(col)

# Criar mapa simples: header original → pod_n
mapping = {h: f"pod_{i+1}" for i, h in enumerate(all_headers)}

print("Salvando mapping...")
with open(mapping_out, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["original", "anon"])
    for orig, anon in mapping.items():
        writer.writerow([orig, anon])

# Aplicar mapeamento aos arquivos
def apply_mapping(df):
    new_cols = [mapping[c] if c in mapping else c for c in df.columns]
    df.columns = new_cols
    return df

print("Anonimizando CPU...")
df_cpu_anon = apply_mapping(df_cpu)
df_cpu_anon.to_csv(cpu_out, index=False)

print("Anonimizando MEM...")
df_mem_anon = apply_mapping(df_mem)
df_mem_anon.to_csv(mem_out, index=False)

print("Concluído!")
print(f"Arquivos gerados:\n - {cpu_out}\n - {mem_out}\n - {mapping_out}")

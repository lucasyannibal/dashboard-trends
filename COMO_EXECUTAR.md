# 🚀 Como Executar o Samsung Trends Dashboard

Este guia contém o passo a passo completo para executar o dashboard na sua máquina.

## 📋 Pré-requisitos

### 1. Python
- Você precisa ter o **Python 3.8 ou superior** instalado
- Para verificar se você tem Python instalado, abra o terminal/prompt de comando e digite:
  ```bash
  python --version
  ```
- Se não tiver Python instalado, baixe em: https://www.python.org/downloads/
  - **IMPORTANTE**: Durante a instalação, marque a opção "Add Python to PATH"

### 2. Arquivos Necessários
Certifique-se de que a pasta contém os seguintes arquivos:
- ✅ `app.py` - Código principal do dashboard
- ✅ `requirements.txt` - Lista de dependências
- ✅ `Samsung_base_reclassificada_COM_descricao.xlsx` - Base de dados
- ✅ `samsung-logo-png_seeklogo-122019.png` - Logo da Samsung

---

## 🔧 Passo a Passo para Instalação

### **Passo 1: Abrir o Terminal na Pasta do Projeto**

#### No Windows:
1. Abra o **Explorador de Arquivos**
2. Navegue até a pasta `Social Listener Samsung`
3. Na barra de endereços no topo, digite `cmd` e pressione **Enter**
4. O Prompt de Comando abrirá diretamente na pasta

#### No Mac/Linux:
1. Abra o **Terminal**
2. Use o comando `cd` para navegar até a pasta:
   ```bash
   cd "caminho/para/Social Listener Samsung"
   ```

---

### **Passo 2: Criar Ambiente Virtual (Recomendado)**

Um ambiente virtual isola as dependências deste projeto de outros projetos Python.

**No Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**No Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

✅ Você saberá que o ambiente virtual está ativo quando aparecer `(venv)` antes do cursor no terminal.

---

### **Passo 3: Instalar Dependências**

Com o ambiente virtual ativo, instale todas as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

Este comando instalará:
- `streamlit` - Framework do dashboard
- `pandas` - Manipulação de dados
- `plotly` - Gráficos interativos
- `openpyxl` - Leitura de arquivos Excel

**Aguarde a instalação concluir.** Pode levar alguns minutos dependendo da sua conexão.

---

## ▶️ Como Executar o Dashboard

### **Comando para Iniciar:**

```bash
streamlit run app.py
```

### **O que vai acontecer:**
1. O terminal exibirá mensagens de inicialização
2. Após alguns segundos, uma nova aba do navegador abrirá automaticamente
3. O dashboard estará rodando em: `http://localhost:8501`

### **Se o navegador não abrir automaticamente:**
- Copie o link que aparecer no terminal (geralmente `http://localhost:8501`)
- Cole no seu navegador preferido (Chrome, Firefox, Edge, etc.)

---

## 🎯 Navegando no Dashboard

O dashboard possui **2 páginas**:

### **Página 1: Macro & Micro Trends**
- Treemap com distribuição de MacroTrends
- Cards descritivos das tendências
- Gráfico de barras com Top MicroTrends
- **Filtros na sidebar**: MacroTrend e MicroTrend com descrições

### **Página 2: Microtrends & Influencers**
- KPIs (Vídeos, Views, Followers, etc.)
- Gráfico de frequência de MicroTrends
- Gráfico de bolhas Social vs Media Power
- Ranking de Top 10 Influenciadores
- **Filtros na sidebar**: Canal, MacroTrend, MicroTrend e Influenciador

---

## 🛑 Como Parar o Dashboard

Para parar a execução do dashboard:
1. Volte ao terminal onde o dashboard está rodando
2. Pressione **Ctrl + C** (Windows/Linux) ou **Cmd + C** (Mac)
3. O servidor será encerrado

---

## ⚠️ Problemas Comuns e Soluções

### **Erro: "Python não é reconhecido como comando"**
**Solução**: Python não está no PATH do sistema
- Reinstale o Python e marque "Add Python to PATH" durante a instalação
- Ou adicione manualmente o Python às variáveis de ambiente

### **Erro: "ModuleNotFoundError"**
**Solução**: Dependências não foram instaladas corretamente
```bash
pip install -r requirements.txt --upgrade
```

### **Erro: "FileNotFoundError: Samsung_base_reclassificada_COM_descricao.xlsx"**
**Solução**: O arquivo Excel não está na mesma pasta que `app.py`
- Certifique-se de que o arquivo Excel está na pasta `Social Listener Samsung`

### **Erro: "Logo não aparece na sidebar"**
**Solução**: Arquivo de imagem não encontrado
- Verifique se `samsung-logo-png_seeklogo-122019.png` está na pasta

### **Dashboard não atualiza após alterações**
**Solução**: 
- Pressione **R** no dashboard para recarregar
- Ou clique em "Always rerun" no canto superior direito

### **Porta 8501 já está em uso**
**Solução**: Outra instância do Streamlit está rodando
- Feche outras instâncias do dashboard
- Ou use uma porta diferente:
  ```bash
  streamlit run app.py --server.port 8502
  ```

---

## 🔄 Atualizando os Dados

Para atualizar os dados do dashboard:
1. Substitua o arquivo `Samsung_base_reclassificada_COM_descricao.xlsx` pelo novo
2. **IMPORTANTE**: Mantenha o mesmo nome de arquivo
3. Recarregue o dashboard (pressione **R**)

---

## 💡 Dicas Úteis

### **Melhor Performance:**
- Use navegadores modernos (Chrome, Edge, Firefox)
- Feche abas desnecessárias durante a análise
- Se o dashboard ficar lento, reduza a quantidade de filtros selecionados

### **Exportar Visualizações:**
- Passe o mouse sobre qualquer gráfico
- Clique no ícone de câmera 📷 no canto superior direito do gráfico
- A imagem será baixada automaticamente

### **Modo Tela Cheia:**
- Clique nos 3 pontinhos (⋮) no canto superior direito
- Selecione "Settings"
- Ative "Wide mode" para melhor visualização

---

## 📞 Suporte

Se você encontrar problemas não listados aqui:
1. Verifique se todos os arquivos necessários estão na pasta
2. Confirme que o Python 3.8+ está instalado
3. Tente reinstalar as dependências
4. Entre em contato com a equipe de desenvolvimento

---

## 📦 Estrutura da Pasta

Sua pasta deve estar organizada assim:
```
Social Listener Samsung/
│
├── app.py                                          # Código principal
├── requirements.txt                                # Dependências
├── Samsung_base_reclassificada_COM_descricao.xlsx # Base de dados
├── samsung-logo-png_seeklogo-122019.png           # Logo Samsung
├── COMO_EXECUTAR.md                               # Este arquivo
└── venv/                                          # Ambiente virtual (criado no passo 2)
```

---

**✅ Pronto! Você está preparado para executar o Samsung Trends Dashboard.**

**Criado em:** Fevereiro 2026  
**Versão do Dashboard:** 2.0  
**Compatível com:** Python 3.8+, Windows/Mac/Linux

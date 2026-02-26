# 🌐 Como Publicar o Dashboard Online

Este guia mostra como publicar o Samsung Trends Dashboard na internet para que qualquer pessoa possa acessar sem precisar rodar localmente.

## 🎯 Melhor Opção: Streamlit Community Cloud

**Vantagens:**
- ✅ **100% GRATUITO**
- ✅ Deploy em menos de 5 minutos
- ✅ Atualização automática quando você atualizar o código
- ✅ URL pública para compartilhar
- ✅ Sem necessidade de servidor próprio
- ✅ Suporta até 1GB de dados

---

## 📋 Pré-requisitos

1. **Conta no GitHub** (gratuita) - https://github.com
2. **Conta no Streamlit Community Cloud** (gratuita) - https://streamlit.io/cloud
3. Seu projeto já funciona localmente

---

## 🚀 Passo a Passo Completo

### **ETAPA 1: Preparar o Projeto**

#### 1.1. Criar arquivo `.gitignore`

Crie um arquivo chamado `.gitignore` na pasta do projeto com o seguinte conteúdo:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Streamlit
.streamlit/secrets.toml

# OS
.DS_Store
Thumbs.db

# IDEs
.vscode/
.idea/
*.swp
*.swo
```

Este arquivo evita que arquivos desnecessários sejam enviados ao GitHub.

#### 1.2. Verificar arquivos necessários

Certifique-se de que sua pasta tem:
- ✅ `app.py`
- ✅ `requirements.txt`
- ✅ `Samsung_base_reclassificada_COM_descricao.xlsx`
- ✅ `samsung-logo-png_seeklogo-122019.png`
- ✅ `.gitignore` (recém-criado)

---

### **ETAPA 2: Subir o Projeto para o GitHub**

#### 2.1. Criar repositório no GitHub

1. Acesse https://github.com
2. Faça login ou crie uma conta
3. Clique no botão **"+"** no canto superior direito
4. Selecione **"New repository"**
5. Configure o repositório:
   - **Repository name**: `samsung-trends-dashboard`
   - **Description**: `Dashboard executivo de análise de tendências Samsung`
   - **Visibilidade**: 
     - **Private** (apenas você e pessoas autorizadas veem)
     - **Public** (qualquer pessoa vê - não recomendado para dados sensíveis)
   - **NÃO** marque "Initialize with README"
6. Clique em **"Create repository"**

#### 2.2. Enviar arquivos para o GitHub

**Opção A: Interface Web do GitHub (Mais Fácil)**

1. No repositório criado, clique em **"uploading an existing file"**
2. Arraste TODOS os arquivos do projeto para a área de upload:
   - `app.py`
   - `requirements.txt`
   - `Samsung_base_reclassificada_COM_descricao.xlsx`
   - `samsung-logo-png_seeklogo-122019.png`
   - `.gitignore`
   - `COMO_EXECUTAR.md`
   - `COMO_PUBLICAR.md`
3. Adicione uma mensagem: "Initial commit - Samsung Dashboard"
4. Clique em **"Commit changes"**

**Opção B: Via Git (Terminal)**

```bash
# Abra o terminal na pasta do projeto

# Inicializar Git
git init

# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Initial commit - Samsung Dashboard"

# Conectar com o repositório remoto (substitua SEU-USUARIO)
git remote add origin https://github.com/SEU-USUARIO/samsung-trends-dashboard.git

# Enviar para o GitHub
git branch -M main
git push -u origin main
```

⚠️ **IMPORTANTE**: Se os arquivos forem grandes (>100MB), você precisará usar Git LFS ou reduzir o tamanho do arquivo Excel.

---

### **ETAPA 3: Deploy no Streamlit Community Cloud**

#### 3.1. Criar conta no Streamlit Cloud

1. Acesse https://share.streamlit.io/
2. Clique em **"Sign up"**
3. Escolha **"Continue with GitHub"**
4. Autorize o Streamlit a acessar sua conta GitHub

#### 3.2. Fazer Deploy

1. No painel do Streamlit Cloud, clique em **"New app"**
2. Preencha as informações:
   - **Repository**: `seu-usuario/samsung-trends-dashboard`
   - **Branch**: `main`
   - **Main file path**: `app.py`
3. Clique em **"Advanced settings"** (opcional):
   - Você pode definir variáveis de ambiente aqui se necessário
4. Clique em **"Deploy!"**

#### 3.3. Aguardar Deploy

- O Streamlit Cloud começará a instalar as dependências
- Isso pode levar 2-5 minutos
- Você verá logs em tempo real do processo
- Quando aparecer **"Your app is live!"**, está pronto! 🎉

---

## 🔗 Compartilhar o Dashboard

Após o deploy, você receberá uma URL como:
```
https://seu-usuario-samsung-trends-dashboard-app-xyz123.streamlit.app
```

**Como compartilhar:**
- Copie esta URL
- Envie para qualquer pessoa que precise acessar
- Elas poderão usar o dashboard direto no navegador, sem instalar nada!

---

## 🔄 Atualizar o Dashboard

Quando você quiser atualizar o dashboard:

### **Opção A: Via Interface Web do GitHub**

1. Acesse seu repositório no GitHub
2. Clique no arquivo que quer editar (ex: `app.py`)
3. Clique no ícone de lápis ✏️ para editar
4. Faça as alterações
5. Clique em **"Commit changes"**
6. O Streamlit Cloud detectará a mudança e **atualizará automaticamente** em 1-2 minutos!

### **Opção B: Via Git Local**

```bash
# Fazer alterações nos arquivos localmente

# Adicionar alterações
git add .

# Fazer commit
git commit -m "Atualização do dashboard"

# Enviar para GitHub
git push origin main
```

---

## 📊 Atualizar os Dados (Excel)

Para atualizar o arquivo Excel com novos dados:

### **Método 1: Upload via GitHub Web**

1. Acesse seu repositório no GitHub
2. Clique no arquivo `Samsung_base_reclassificada_COM_descricao.xlsx`
3. Clique em **"Delete file"** (lixeira)
4. Faça commit da exclusão
5. Volte à página principal do repositório
6. Clique em **"Add file" > "Upload files"**
7. Faça upload do novo arquivo Excel (MESMO NOME!)
8. Faça commit
9. O dashboard será atualizado automaticamente!

### **Método 2: Via Git**

```bash
# Substitua o arquivo Excel localmente pelo novo

# Adicionar e commitar
git add Samsung_base_reclassificada_COM_descricao.xlsx
git commit -m "Atualização dos dados"
git push origin main
```

---

## ⚙️ Configurações Avançadas

### **Limitar Acesso ao Dashboard**

Se você não quer que qualquer pessoa acesse:

1. No Streamlit Cloud, vá em **"Settings"** do seu app
2. Em **"Sharing"**, adicione os e-mails autorizados
3. Apenas essas pessoas conseguirão acessar

### **Aumentar Recursos (Pago)**

Se o dashboard ficar lento ou precisar de mais recursos:
- Streamlit oferece planos pagos com mais memória e CPU
- Preços a partir de $20/mês

---

## ⚠️ Limitações do Plano Gratuito

**Streamlit Community Cloud (Grátis):**
- ✅ 1GB de memória
- ✅ 1 CPU core
- ✅ 1GB de armazenamento
- ✅ Tempo de inatividade: app "dorme" após 7 dias sem uso (acorda em segundos quando alguém acessa)
- ❌ Sem domínio customizado (você terá uma URL .streamlit.app)

**Para 99% dos casos, o plano gratuito é suficiente!**

---

## 🔒 Segurança e Dados Sensíveis

### **Se seus dados são confidenciais:**

1. **Repositório Privado**: Use repositório privado no GitHub
2. **Controle de Acesso**: Configure e-mails autorizados no Streamlit Cloud
3. **Remover Dados Sensíveis**: Se possível, anonimize dados antes do upload
4. **Variáveis de Ambiente**: Use secrets do Streamlit para senhas/tokens

#### Como usar Secrets:

1. No Streamlit Cloud, vá em **"Settings" > "Secrets"**
2. Adicione suas variáveis no formato:
   ```toml
   DB_PASSWORD = "sua-senha-aqui"
   API_KEY = "sua-chave-api"
   ```
3. No código, acesse com:
   ```python
   import streamlit as st
   senha = st.secrets["DB_PASSWORD"]
   ```

---

## 🐛 Problemas Comuns

### **Erro: "Requirements.txt not found"**
**Solução**: Certifique-se de que `requirements.txt` está na raiz do repositório

### **Erro: "Module not found"**
**Solução**: Verifique se todas as bibliotecas estão listadas em `requirements.txt`

### **Erro: "File not found: Samsung_base..."**
**Solução**: O arquivo Excel deve estar na mesma pasta que `app.py`

### **Dashboard muito lento**
**Solução**:
- Reduza o tamanho do arquivo Excel (filtre apenas dados necessários)
- Use cache (`@st.cache_data`) - já implementado!
- Considere plano pago se necessário

### **Arquivo Excel muito grande (>100MB)**
**Solução**:
- Use Git LFS (Large File Storage)
- Ou armazene dados em Google Sheets/Database e conecte via API
- Ou reduza o tamanho dos dados

---

## 🌍 Alternativas ao Streamlit Cloud

Se você precisar de algo diferente:

### **1. Heroku** (Pago após período gratuito)
- Mais flexível
- Suporta bancos de dados
- Mais complexo de configurar

### **2. AWS/Azure/GCP** (Pago)
- Máximo controle
- Escalabilidade ilimitada
- Requer conhecimento técnico

### **3. PythonAnywhere** (Tem plano gratuito)
- Boa alternativa
- Menos específico para Streamlit

### **4. Servidor Próprio**
- Total controle
- Requer infraestrutura

---

## ✅ Checklist Final

Antes de fazer deploy, verifique:

- [ ] Dashboard funciona 100% localmente
- [ ] `requirements.txt` está completo e correto
- [ ] Todos os arquivos necessários estão na pasta
- [ ] `.gitignore` está configurado
- [ ] Conta GitHub criada
- [ ] Repositório GitHub criado
- [ ] Arquivos enviados para GitHub
- [ ] Conta Streamlit Cloud criada
- [ ] Deploy feito com sucesso
- [ ] URL funcionando
- [ ] Dashboard testado online

---

## 📞 Suporte

**Documentação Oficial:**
- Streamlit Cloud: https://docs.streamlit.io/streamlit-community-cloud
- GitHub: https://docs.github.com

**Comunidade:**
- Streamlit Forum: https://discuss.streamlit.io
- Stack Overflow: Tag `streamlit`

---

## 🎉 Resumo Rápido

1. ✅ Crie repositório no GitHub
2. ✅ Faça upload dos arquivos do projeto
3. ✅ Acesse https://share.streamlit.io
4. ✅ Conecte com GitHub e faça deploy
5. ✅ Compartilhe a URL gerada
6. ✅ Pronto! Dashboard online e gratuito!

**Tempo estimado: 10-15 minutos**

---

**Criado em:** Fevereiro 2026  
**Última atualização:** Fevereiro 2026  
**Método recomendado:** Streamlit Community Cloud

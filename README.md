Este projeto é um laboratório prático de autenticação avançada desenvolvido para consolidar os aprendizados sobre o protocolo **OAuth2.0**. Ele vai muito além do básico, implementando fluxos de segurança completos com uma interface moderna e responsiva estilo "Startup Software".

---

## 🚀 Funcionalidades Principais

### 🔑 Autenticação Social (OAuth2.0)
*   **Integração com GitHub**: Login rápido e seguro utilizando o protocolo Oauth2.0 via `django-allauth`.
*   **Sign-up Social**: Automação de criação de perfil a partir de dados externos.

### 📧 Fluxo de Recuperação de Senha (SMTP)
*   **Recuperação Robusta**: Fluxo completo de esqueci a senha com envio de e-mails via **Mailtrap** (SMTP).
*   **E-mails Premium**: Templates de e-mail customizados em HTML com design responsivo.

### 🎨 Experiência do Usuário (UI/UX)
*   **Layout Sidebar**: Menu lateral fixo para melhor navegação.
*   **Dark Mode Automático**: Detecção automática da preferência do sistema do usuário.
*   **Design Glassmorphism**: Cards e botões com transparência e micro-animações.

---

## 🛠️ Tecnologias Utilizadas

*   **Python 3.13**
*   **Django 6.0**
*   **Django Allauth** (Social Auth & Account Management)
*   **Bootstrap 5** (Customizado via CSS puro)
*   **Mailtrap** (Ambiente de testes SMTP)

---

## 📸 Screenshots

| Login Premium | Feed Estilo Rede Social | E-mail de Recuperação |
| :---: | :---: | :---: |
| ![Login](https://raw.githubusercontent.com/DouglasScarello/django-auth-lab-oauth2/main/screenshots/login.png) | ![Home](https://raw.githubusercontent.com/DouglasScarello/django-auth-lab-oauth2/main/screenshots/home.png) | ![Email](https://raw.githubusercontent.com/DouglasScarello/django-auth-lab-oauth2/main/screenshots/email.png) |

---

## ⚙️ Como Rodar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/DouglasScarello/django-auth-lab-oauth2.git
   cd django-auth-lab-oauth2
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as Variáveis de Ambiente:**
   Crie um arquivo `.env` (baseado no `.env.example`) com suas credenciais do GitHub OAuth e Mailtrap.

5. **Rode as migrações e o servidor:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

## 🎓 Sobre este projeto
Desenvolvido após concluir a formação de **OAuth2.0 da Alura**, com o objetivo de demonstrar habilidades técnicas em segurança de aplicações web e front-end moderno.

---
Desenvolvido por **[Douglas Scarello](https://github.com/DouglasScarello)** 🚀

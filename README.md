# 🛡️ PyShield Stealth Scanner

Fala, time! 👋 Este projeto é uma implementação de um **Network Scanner Profissional** focado em reconhecimento furtivo (Stealth Recon). Desenvolvi essa ferramenta para demonstrar como unir a performance do Python assíncrono com o poder da manipulação de pacotes em baixo nível.

---

### 🚀 O que essa ferramenta faz?
Basicamente, o PyShield mapeia portas abertas em um alvo sem "fazer barulho". Diferente de conexões comuns, ele usa a técnica **TCP SYN Scan (Half-Open)**. 

**A lógica é a seguinte:**
1. O scanner envia um sinal "Oi" (SYN).
2. O alvo responde "Oi, tudo bem?" (SYN-ACK) se a porta estiver aberta.
3. O scanner, em vez de continuar o papo, desliga na cara (RST).
*Resultado:* Sabemos que a porta está aberta, mas o servidor alvo dificilmente registra que houve uma conexão real. 



---

### ⚙️ Pré-requisitos
Como estamos lidando com manipulação de pacotes na camada 3 (IP), você vai precisar de:
* **Python 3.8+** instalado.
* **Permissões de Administrador (Sudo/Admin):** Essencial para criar pacotes brutos.
* **Scapy:** A biblioteca que faz o trabalho sujo na rede.

---

### 🛠️ Como Instalar e Rodar

1. **Clone o repositório:**
```bash
git clone [https://github.com/jcss191/pyshield-scanner.git](https://github.com/jcss191/pyshield-scanner.git)
cd pyshield-scanner

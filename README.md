# 🛡️ PyShield Stealth Scanner

Fala, time! 👋 

Este projeto não é apenas um "scriptzinho" de rede. É uma ferramenta de **reconhecimento ofensivo** que eu desenvolvi em Python para ser rápida e silenciosa. O objetivo aqui foi unir a performance do **AsyncIO** com o poder do **Scapy** para manipular pacotes na mão.

---

### 🚀 Pra que serve essa ferramenta?
Sabe quando você precisa descobrir quais portas estão abertas em um servidor, mas não quer fazer barulho? É aí que o PyShield entra. Ele faz o mapeamento de alvos usando a técnica de **Stealth SYN Scan**.

**Como ele funciona "por baixo do capô":**
Diferente de uma conexão normal, ele não completa o "aperto de mão" (Handshake) do TCP. 
1. Ele manda um sinal de **SYN**.
2. Se o alvo responde **SYN-ACK**, ele já sabe que a porta tá aberta.
3. Antes que o alvo registre a conexão, o script manda um **RST** (Reset) e desliga na cara. 
*Resultado:* Você descobre a brecha e o servidor alvo nem vê quem passou por lá. 🕵️‍♂️

---

### ⚙️ Como instalar no Kali Linux

Como a gente manipula pacotes na camada 3 (baixo nível), você vai precisar da biblioteca Scapy. No seu terminal do Kali, rode:

1. **Instale as dependências:**
```bash
sudo apt update && sudo apt install python3-scapy -y 

git clone [https://github.com/jcss191/pyshield-scanner.git](https://github.com/jcss191/pyshield-scanner.git)
cd pyshield-scanner

🛠️ Como usar na prática
1. Ajuste o alvo:
Abra o arquivo scanner.py e mude o IP do alvo lá no final do código. 🛠️
mousepad scanner.py

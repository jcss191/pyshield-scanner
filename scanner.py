import asyncio
import logging
import random
from typing import List, Optional
from scapy.all import IP, TCP, sr1, conf
from datetime import datetime

# Configuração de Logging Profissional
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)
logger = logging.getLogger(__name__)

# Desabilita avisos desnecessários do Scapy
conf.verb = 0

class StealthScanner:
    """
    Scanner de Rede de Alta Performance focado em técnicas Stealth (SYN Scan).
    Demonstra uso de AsyncIO, Scapy e Engenharia de Protocolos.
    """

    def __init__(self, target: str, timeout: float = 1.0, delay: float = 0.1):
        self.target = target
        self.timeout = timeout
        self.delay = delay
        self.results = []

    async def syn_scan(self, port: int) -> None:
        """
        Executa um TCP SYN Scan (Half-Open) em uma porta específica.
        Esta técnica é furtiva pois não completa o handshake TCP.
        """
        try:
            # Randomiza o delay para evitar assinaturas de IDS (Sistemas de Detecção)
            await asyncio.sleep(self.delay * random.uniform(0.5, 1.5))

            # Construção do pacote Camada 3 (IP) e Camada 4 (TCP)
            # Flag "S" = SYN
            packet = IP(dst=self.target) / TCP(dport=port, flags="S")
            
            # Executa a operação de rede em um thread pool para não bloquear o event loop
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None, 
                lambda: sr1(packet, timeout=self.timeout, verbose=0)
            )

            if response is None:
                logger.debug(f"Port {port}: Filtrada (Sem resposta)")
            elif response.haslayer(TCP):
                tcp_layer = response.getlayer(TCP)
                # 0x12 é a flag SYN-ACK (Porta Aberta)
                if tcp_layer.flags == 0x12:
                    logger.info(f"🔥 Porta {port} detectada como ABERTA em {self.target}")
                    self.results.append(port)
                    # Envia um RST para fechar a conexão imediatamente e manter a furtividade
                    rst_packet = IP(dst=self.target) / TCP(dport=port, flags="R")
                    await loop.run_in_executor(None, lambda: sr1(rst_packet, timeout=0.5, verbose=0))
                # 0x14 é a flag RST-ACK (Porta Fechada)
                elif tcp_layer.flags == 0x14:
                    logger.debug(f"Port {port}: Fechada")

        except Exception as e:
            logger.error(f"Erro ao escanear porta {port}: {str(e)}")

    async def run(self, port_range: List[int]):
        """Gerencia a execução assíncrona do scan"""
        start_time = datetime.now()
        logger.info(f"Iniciando Stealth Scan em {self.target} às {start_time}")
        
        # Randomiza a ordem das portas (Técnica Anti-Filtro)
        random.shuffle(port_range)
        
        tasks = [self.syn_scan(port) for port in port_range]
        await asyncio.gather(*tasks)
        
        duration = datetime.now() - start_time
        logger.info(f"Scan finalizado em {duration}. Portas abertas encontradas: {self.results}")

if __name__ == "__main__":
    # Exemplo de uso: Portas comuns de servidores
    TARGET_IP = "127.0.0.1" # Altere para o seu alvo de teste
    PORTS_TO_SCAN = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]

    scanner = StealthScanner(target=TARGET_IP, timeout=1.5, delay=0.2)
    
    try:
        asyncio.run(scanner.run(PORTS_TO_SCAN))
    except KeyboardInterrupt:
        logger.warning("Scan interrompido pelo usuário.")
